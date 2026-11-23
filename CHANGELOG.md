# Changelog

Semua perubahan penting pada proyek ini didokumentasikan di file ini.

Format mengikuti [Keep a Changelog](https://keepachangelog.com/) dan proyek ini
menganut [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-11-23

### Ditambahkan
- Landing page responsif untuk UMKM (contoh: kedai kopi).
- Bagian: hero, menu produk, tentang, galeri, kontak, dan footer.
- Navigasi dengan penanda bagian aktif (scroll-spy) dan menu mobile.
- Formulir kontak dengan validasi sisi klien dan integrasi WhatsApp.
- Tombol kembali ke atas dan animasi muncul saat menggulir.
- Aksesibilitas dasar: skip link, landmark semantik, ARIA, dan dukungan
  `prefers-reduced-motion`.
- Test struktur & isi situs (pytest).
- CI GitHub Actions pada Python 3.10–3.12.
- `tasks.py` lintas-platform dan `Makefile`.