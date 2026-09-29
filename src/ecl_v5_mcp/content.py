"""Read-only access to the ECL content shared with the Node stdio server.

Everything here mirrors the helpers in ``index.js`` so that both servers return
byte-identical tool output. Files are read on every call, so content edits are
visible without restarting the server.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote

DEFAULT_CONTENT_DIR = Path(__file__).resolve().parents[2]

# Keep in sync with `templateFamilies` in index.js (enforced by
# tests/test_parity.py). Prefix matching is deliberately avoided: it would make
# `file` include `file-upload` and expose the legacy EU footer through the EC
# `site-footer` family.
TEMPLATE_FAMILIES: dict[str, list[str]] = {
    "carousel": ["carousel.html.twig", "slider-pager.html.twig"],
    "category-filter": [
        "category-filter.html.twig",
        "category-filter-items.html.twig",
    ],
    "checkbox": ["checkbox-group.html.twig", "checkbox-item.html.twig"],
    "file": ["file.html.twig"],
    "file-upload": ["file-upload.html.twig", "file-upload-status.html.twig"],
    "gallery": [
        "gallery.html.twig",
        "gallery-item.html.twig",
        "gallery-overlay.html.twig",
    ],
    "highlighted-search": ["highlighted-search.html.twig"],
    "list-illustration": [
        "list-illustration.html.twig",
        "list-illustration-item.html.twig",
    ],
    "mega-menu": [
        "mega-menu.html.twig",
        "mega-menu-item.html.twig",
        "mega-menu-featured-item.html.twig",
    ],
    "menu": ["menu.html.twig", "menu-item.html.twig"],
    "navigation-list": [
        "navigation-list.html.twig",
        "navigation-list-item.html.twig",
    ],
    "page-header": ["page-header.html.twig", "page-header-expandable.html.twig"],
    "quiz": ["quiz.html.twig", "quiz-card.html.twig"],
    "radio": ["radio-group.html.twig", "radio-button.html.twig"],
    "site-footer": [
        "site-footer-ec.html.twig",
        "site-footer-ec-section.html.twig",
    ],
    "site-header": [
        "site-header.html.twig",
        "site-header-language-switcher.html.twig",
    ],
    "story-card": [
        "story-card.html.twig",
        "story-card-card.html.twig",
        "slider-pager.html.twig",
    ],
    "tag": ["tag.html.twig", "tag-set.html.twig"],
    "timeline": ["timeline.html.twig", "timeline-set.html.twig"],
}


class ContentError(Exception):
    """Raised with the exact user-facing message the Node server returns."""


def to_json(value: Any) -> str:
    """Serialise like ``JSON.stringify(value, null, 2)``."""
    return json.dumps(value, indent=2, ensure_ascii=False)


def encode_uri_component(value: str) -> str:
    """Equivalent of JavaScript's ``encodeURIComponent``."""
    return quote(value, safe="-_.!~*'()")


def _js_length(text: str) -> int:
    """Length in UTF-16 code units, like JavaScript's ``String.length``."""
    return len(text.encode("utf-16-le")) // 2


def _js_substring(text: str, end: int) -> str:
    """``text.substring(0, end)`` using UTF-16 code units."""
    return text.encode("utf-16-le")[: end * 2].decode("utf-16-le", errors="ignore")


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _read_dir(path: Path) -> list[str]:
    # libuv (Node's fs.readdir) returns entries sorted bytewise.
    return sorted(os.listdir(path))


@dataclass(frozen=True)
class Content:
    """ECL content rooted at ``root``.

    ``dir_placeholder`` replaces ``__DIR__`` in guides: a local path for
    stdio, or the public base URL when assets are served over HTTP.
    """

    root: Path
    dir_placeholder: str

    @property
    def guides_dir(self) -> Path:
        return self.root / "guides"

    @property
    def components_dir(self) -> Path:
        return self.root / "components"

    @property
    def skills_dir(self) -> Path:
        return self.root / "skills"

    @property
    def starter_template_path(self) -> Path:
        return self.root / "starter-template.html"

    def process_guide(self, text: str) -> str:
        return text.replace("__DIR__", self.dir_placeholder)

    # Guides ---------------------------------------------------------------

    def guide_files(self) -> list[str]:
        return [f for f in _read_dir(self.guides_dir) if f.endswith(".md")]

    def guide(self, topic: str) -> str:
        file = f"{topic}.md"
        if file not in self.guide_files():
            raise ContentError(
                f"Guide for topic '{topic}' not found. Please call the "
                "guide_list tool to see available guides."
            )
        try:
            return self.process_guide(_read(self.guides_dir / file))
        except OSError as error:
            raise ContentError(
                f"Guide for topic '{topic}' not found. Please call the "
                "guide_list tool to see available guides."
            ) from error

    def guide_list(self) -> list[dict[str, Any]]:
        try:
            guides = []
            for file in self.guide_files():
                content = _read(self.guides_dir / file)
                topic = file.replace(".md", "", 1)
                snippet = _js_substring(content, 120)
                guides.append(
                    {
                        "topic": topic,
                        "snippet": snippet
                        + ("..." if _js_length(content) > 120 else ""),
                        "call": {"tool": "guide", "parameters": {"topic": topic}},
                    }
                )
            return guides
        except OSError as error:
            raise ContentError(f"Failed to list guides: {error}") from error

    # Components -----------------------------------------------------------

    def component_files(self) -> list[str]:
        return _read_dir(self.components_dir)

    @staticmethod
    def html_files(files: list[str]) -> list[str]:
        return [f for f in files if f.endswith(".html") and not f.endswith(".twig")]

    @staticmethod
    def template_files(component_id: str, files: list[str]) -> list[str]:
        family = TEMPLATE_FAMILIES.get(component_id, [f"{component_id}.html.twig"])
        return [f for f in family if f in files]

    def component_ids(self) -> list[str]:
        return [
            f.replace(".html", "", 1) for f in self.html_files(self.component_files())
        ]

    def components_list(self) -> list[dict[str, Any]]:
        try:
            files = self.component_files()
        except OSError as error:
            raise ContentError(f"Failed to list components: {error}") from error
        components = []
        for file in self.html_files(files):
            component_id = file.replace(".html", "", 1)
            component: dict[str, Any] = {
                "id": component_id,
                "component_call": {
                    "tool": "component",
                    "parameters": {"id": component_id},
                },
            }
            if self.template_files(component_id, files):
                component["template_call"] = {
                    "tool": "component_template",
                    "parameters": {"id": component_id},
                }
            components.append(component)
        return components

    def component(self, component_id: str) -> str:
        message = (
            f"Component with id '{component_id}' not found. Please call the "
            "components_list tool to see available components."
        )
        try:
            if component_id not in self.component_ids():
                raise ContentError(message)
            return _read(self.components_dir / f"{component_id}.html")
        except OSError as error:
            raise ContentError(message) from error

    def component_template(self, component_id: str) -> dict[str, str]:
        prefix = f"Failed to get templates for component '{component_id}': "
        try:
            files = self.component_files()
            twig_files = self.template_files(component_id, files)
            if not twig_files:
                raise ContentError(
                    f"{prefix}No templates found for component '{component_id}'"
                )
            return {f: _read(self.components_dir / f) for f in twig_files}
        except OSError as error:
            raise ContentError(f"{prefix}{error}") from error

    # Starter template -----------------------------------------------------

    def starter_template(self) -> str:
        try:
            return _read(self.starter_template_path)
        except OSError as error:
            raise ContentError(f"Failed to read starter template: {error}") from error

    # Skills ---------------------------------------------------------------

    @staticmethod
    def _parse_frontmatter(content: str, fallback_id: str) -> dict[str, str]:
        frontmatter = re.match(r"---\s*\n([\s\S]*?)\n---", content)
        metadata = frontmatter.group(1) if frontmatter else ""

        def field(pattern: str) -> str | None:
            found = re.search(pattern, metadata, re.MULTILINE)
            return found.group(1).strip() if found else None

        return {
            "name": field(r"^name:\s*(.+)$") or fallback_id,
            "description": field(r"^description:\s*(.+)$") or "",
            "version": field(r"^\s+version:\s*(.+)$") or "1.0.0",
        }

    def skill_list(self) -> list[dict[str, Any]]:
        try:
            entries = _read_dir(self.skills_dir)
        except OSError:
            return []
        skills = []
        for skill_id in entries:
            if not (self.skills_dir / skill_id).is_dir():
                continue
            try:
                content = _read(self.skills_dir / skill_id / "SKILL.md")
            except OSError:
                # A skill directory without a readable SKILL.md is not advertised.
                continue
            metadata = self._parse_frontmatter(content, skill_id)
            skills.append(
                {
                    "id": skill_id,
                    "name": metadata["name"],
                    "description": metadata["description"],
                    "version": metadata["version"],
                    "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                    "file": "SKILL.md",
                    "resource": f"ecl://skill/{encode_uri_component(skill_id)}",
                    "call": {"tool": "skill_get", "parameters": {"id": skill_id}},
                }
            )
        return sorted(skills, key=lambda skill: skill["id"])

    def skill(self, skill_id: str) -> str:
        skill = next((s for s in self.skill_list() if s["id"] == skill_id), None)
        if skill is None:
            raise ContentError(
                f"Skill '{skill_id}' not found. Please call the skill_list tool "
                "to see available skills."
            )
        return _read(self.skills_dir / skill_id / skill["file"])
