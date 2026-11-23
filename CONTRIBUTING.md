# Contributing

Terima kasih atas minatmu! Repo ini adalah proyek portofolio, tetapi kontribusi
tetap diterima.

## Menjalankan proyek secara lokal

```bash
git clone https://github.com/muhammaddani/umkm-landing-page.git
cd umkm-landing-page
python tasks.py install
python tasks.py test
python tasks.py serve   # buka http://127.0.0.1:8000
```

## Alur kontribusi

1. Buat branch baru: `git checkout -b feat/nama-fitur`
2. Lakukan perubahan dan tambahkan test bila perlu.
3. Pastikan semua test lulus: `python tasks.py test`
4. Commit dengan pesan yang jelas (lihat gaya di bawah).
5. Buka Pull Request.

## Gaya commit

- `feat: ...` — fitur baru
- `fix: ...` — perbaikan bug
- `docs: ...` — perubahan dokumentasi
- `style: ...` — perubahan tampilan tanpa mengubah perilaku
- `test: ...` — menambah atau memperbaiki test
- `chore: ...` — pekerjaan rumah tangga

## Prinsip

- Utamakan aksesibilitas: kontras warna, label formulir, dan atribut ARIA.
- Jaga agar situs tetap ringan (tanpa dependensi tambahan).
- Perubahan tampilan sebaiknya diuji di layar kecil dan besar.