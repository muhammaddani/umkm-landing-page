# UMKM Landing Page

[![CI](https://github.com/muhammaddani/umkm-landing-page/actions/workflows/ci.yml/badge.svg)](https://github.com/muhammaddani/umkm-landing-page/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Situs profil (landing page) untuk usaha kecil dan menengah (UMKM).
Responsif, cepat, dan tanpa framework — cukup HTML, CSS, dan JavaScript
murni. Cocok dijadikan contoh kerja untuk klien UMKM yang butuh kehadiran
online sederhana namun profesional.

Proyek ini dibuat sebagai **template yang bisa langsung dipakai dan
disesuaikan**: ganti nama usaha, menu, dan kontak, lalu situs siap dipakai.

## Fitur

- Desain responsif (mobile-first), rapi di ponsel maupun desktop
- Bagian: hero, produk/menu, tentang, galeri, kontak, dan jam operasional
- Navigasi yang tetap terlihat saat menggulir, dengan penanda bagian aktif
- Menu mobile (hamburger) dengan animasi
- Formulir kontak dengan validasi di sisi klien
- Tautan langsung ke WhatsApp untuk pemesanan
- Tombol "kembali ke atas"
- Animasi muncul saat menggulir (menggunakan `IntersectionObserver`)
- Ringan: tanpa dependensi, tanpa proses build
- Aksesibel: struktur semantik, atribut ARIA, dan kontras warna yang layak

## Cara melihat

Cukup buka `index.html` di browser.

Atau jalankan server lokal:

```bash
python tasks.py serve
# buka http://127.0.0.1:8000
```

## Cara menyesuaikan untuk klien lain

1. Ganti nama usaha, tagline, dan logo di `index.html`.
2. Sesuaikan daftar produk/menu (bagian `#produk`).
3. Ganti nomor WhatsApp dan alamat di bagian kontak serta `js/main.js`
   (konstanta `WHATSAPP_NUMBER`).
4. Sesuaikan warna di `css/style.css` (variabel CSS di `:root`).

## Menjalankan test

```bash
python tasks.py test
```

Test memeriksa hal penting:

- Berkas wajib ada (HTML, CSS, JS).
- Halaman utama memuat elemen penting (judul, navigasi, produk, kontak).
- Tidak ada tautan rusak di dalam halaman (semua anchor `#` mengarah ke id yang ada).
- JavaScript memiliki fungsi yang diharapkan.
- Validasi HTML dasar (tag berpasangan seimbang).

## Struktur proyek

```
umkm-landing-page/
├── index.html             # halaman utama
├── css/
│   └── style.css          # seluruh gaya
├── js/
│   └── main.js            # interaksi (menu, validasi, animasi)
├── assets/                # gambar/ilustrasi
├── tests/
│   └── test_site.py       # test struktur & isi situs
├── .github/workflows/
│   └── ci.yml             # CI: jalankan test di setiap push
├── tasks.py               # tugas lintas-platform
├── Makefile               # alternatif GNU make
├── requirements.txt
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Lisensi

MIT — lihat [LICENSE](LICENSE).