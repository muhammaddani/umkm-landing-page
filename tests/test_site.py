"""Test untuk UMKM landing page.

Memeriksa struktur, isi, dan konsistensi berkas statis. Test ini tidak
memerlukan browser; ia membaca berkas secara langsung.

Jalankan dengan:
    pytest -v
"""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
JS = (ROOT / "js" / "main.js").read_text(encoding="utf-8")


class TagCollector(HTMLParser):
    """Mengumpulkan id, tag, dan pasangan tag untuk pemeriksaan dasar."""

    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.anchor_hrefs: list[str] = []
        self.stack: list[str] = []
        self.unbalanced: list[str] = []
        self.tags: list[str] = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attrs_dict = dict(attrs)
        if "id" in attrs_dict:
            self.ids.append(attrs_dict["id"])
        if tag == "a" and "href" in attrs_dict:
            self.anchor_hrefs.append(attrs_dict["href"])
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            # Ada tag yang tidak ditutup sesuai urutan.
            while self.stack and self.stack[-1] != tag:
                self.unbalanced.append(self.stack.pop())
            if self.stack:
                self.stack.pop()


@pytest.fixture(scope="module")
def parsed() -> TagCollector:
    parser = TagCollector()
    parser.feed(HTML)
    parser.close()
    return parser


class TestFilesExist:
    def test_index_exists(self):
        assert (ROOT / "index.html").is_file()

    def test_stylesheet_exists(self):
        assert (ROOT / "css" / "style.css").is_file()

    def test_javascript_exists(self):
        assert (ROOT / "js" / "main.js").is_file()

    def test_favicon_exists(self):
        assert (ROOT / "assets" / "favicon.svg").is_file()

    def test_readme_exists(self):
        assert (ROOT / "README.md").is_file()


class TestHtmlStructure:
    def test_declares_html_lang(self):
        assert '<html lang="id">' in HTML

    def test_has_title(self):
        assert "<title>" in HTML

    def test_has_meta_viewport(self):
        assert 'name="viewport"' in HTML

    def test_has_meta_description(self):
        assert 'name="description"' in HTML

    def test_has_skip_link(self):
        assert "skip-link" in HTML

    def test_has_main_landmark(self):
        assert "<main" in HTML

    def test_has_semantic_sections(self):
        for section_id in ["produk", "tentang", "galeri", "kontak"]:
            assert f'id="{section_id}"' in HTML, f"Bagian {section_id} tidak ditemukan"

    def test_images_have_alt(self):
        # Semua <img> (jika ada) harus punya alt.
        for tag in re.findall(r"<img[^>]*>", HTML):
            assert "alt=" in tag, f"Tag img tanpa alt: {tag}"


class TestLinks:
    def test_internal_anchors_resolve(self, parsed):
        """Setiap tautan #harus mengarah ke id yang benar-benar ada."""
        broken = [
            href
            for href in parsed.anchor_hrefs
            if href.startswith("#") and len(href) > 1 and href[1:] not in parsed.ids
        ]
        assert broken == [], f"Anchor menuju id yang tidak ada: {broken}"

    def test_external_links_use_https(self):
        for href in re.findall(r'href="([^"]+)"', HTML):
            if href.startswith("http"):
                assert href.startswith("https://"), f"Tautan tidak aman: {href}"

    def test_external_links_have_rel_noopener(self):
        for tag in re.findall(r"<a [^>]*target=\"_blank\"[^>]*>", HTML):
            assert "noopener" in tag, f"Tautan _blank tanpa rel=noopener: {tag}"

    def test_whatsapp_link_present(self):
        assert "wa.me" in HTML


class TestAccessibility:
    def test_form_labels_present(self):
        for field_id in ["nama", "telepon", "pesan"]:
            assert f'for="{field_id}"' in HTML, f"Label untuk {field_id} tidak ada"
            assert f'id="{field_id}"' in HTML, f"Input {field_id} tidak ada"

    def test_nav_has_aria_label(self):
        assert 'aria-label="Navigasi utama"' in HTML

    def test_status_region_is_live(self):
        assert 'aria-live="polite"' in HTML

    def test_toggle_has_aria_controls(self):
        assert "aria-controls=" in HTML
        assert "aria-expanded=" in HTML


class TestCss:
    def test_defines_theme_variables(self):
        assert ":root" in CSS
        assert "--warna-utama" in CSS

    def test_has_responsive_media_queries(self):
        assert "@media" in CSS
        assert "max-width: 720px" in CSS

    def test_respects_reduced_motion(self):
        assert "prefers-reduced-motion" in CSS


class TestJavaScript:
    def test_is_strict_mode(self):
        assert '"use strict"' in JS

    def test_has_whatsapp_number_constant(self):
        assert "WHATSAPP_NUMBER" in JS

    def test_defines_expected_functions(self):
        for fn in [
            "initMobileMenu",
            "initScrollSpy",
            "initToTop",
            "initReveal",
            "initContactForm",
        ]:
            assert f"function {fn}" in JS, f"Fungsi {fn} tidak ditemukan"

    def test_has_validation_rules(self):
        assert "RULES" in JS

    def test_no_obvious_console_debug_left(self):
        assert "console.log" not in JS


class TestReadme:
    def test_mentions_test_command(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        assert "tasks.py test" in readme

    def test_mentions_customization(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        assert "menyesuaikan" in readme.lower() or "customiz" in readme.lower()