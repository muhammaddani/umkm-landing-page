# justfile -- alternatif ringkas jika kamu memakai `just`
# (https://github.com/casey/just). Pengguna Windows tanpa `just` bisa
# memakai `python tasks.py <tugas>`.

default:
    @just --list

install:
    python -m pip install --upgrade pip
    pip install -r requirements.txt

test:
    pytest -v

serve:
    python -m http.server 8000

clean:
    python tasks.py clean