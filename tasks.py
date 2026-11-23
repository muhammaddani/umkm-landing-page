#!/usr/bin/env python3
"""Tugas pengembangan lintas-platform untuk UMKM landing page.

Contoh:
    python tasks.py          # tampilkan daftar tugas
    python tasks.py serve    # jalankan server lokal
    python tasks.py test     # jalankan test
"""

from __future__ import annotations

import http.server
import shutil
import socketserver
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _run(cmd: list[str]) -> int:
    print("$", " ".join(cmd))
    return subprocess.call(cmd, cwd=ROOT)


def install() -> int:
    """Pasang dependensi (pytest)."""
    code = _run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    if code:
        return code
    return _run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])


def test() -> int:
    """Jalankan seluruh test."""
    return _run([sys.executable, "-m", "pytest", "-v"])


def serve() -> int:
    """Jalankan server HTTP sederhana untuk melihat situs (port 8000)."""

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(ROOT), **kwargs)

    with socketserver.TCPServer(("127.0.0.1", 8000), Handler) as httpd:
        print("Server berjalan di http://127.0.0.1:8000 (Ctrl+C untuk berhenti)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dihentikan.")
        return 0


def clean() -> int:
    """Hapus artefak cache."""
    for target in [".pytest_cache", "__pycache__", "tests/__pycache__"]:
        shutil.rmtree(ROOT / target, ignore_errors=True)
    for pyc in ROOT.rglob("*.pyc"):
        pyc.unlink(missing_ok=True)
    print("Bersih.")
    return 0


TASKS = {
    "install": (install, "Pasang dependensi (pytest)"),
    "test": (test, "Jalankan seluruh test"),
    "serve": (serve, "Jalankan server lokal (port 8000)"),
    "clean": (clean, "Hapus cache"),
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in {"-h", "--help", "help"}:
        print("Tugas yang tersedia:\n")
        for name, (_, desc) in TASKS.items():
            print(f"  python tasks.py {name:<8} {desc}")
        return 0

    name = sys.argv[1]
    if name not in TASKS:
        print(f"Tugas tidak dikenal: {name}", file=sys.stderr)
        return 1
    return TASKS[name][0]()


if __name__ == "__main__":
    raise SystemExit(main())