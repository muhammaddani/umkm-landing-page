.PHONY: help install test serve clean

help:  ## Tampilkan daftar perintah
	@echo "Perintah yang tersedia:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-10s %s\n", $$1, $$2}'

install:  ## Pasang dependensi
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:  ## Jalankan seluruh test
	pytest -v

serve:  ## Jalankan server lokal
	python -m http.server 8000

clean:  ## Hapus cache
	python tasks.py clean