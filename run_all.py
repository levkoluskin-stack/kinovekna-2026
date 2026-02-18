#!/usr/bin/env python3
"""
run_all.py — Запуск полного пайплайна:
  1. Очистка старых новостей
  2. Сбор новых с RSS
  3. Озвучка через TTS
  4. Сборка сайта
"""

import subprocess
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

steps = [
    ("🧹 Очистка",     [sys.executable, "scripts/cleanup.py"]),
    ("📡 Сбор RSS",     [sys.executable, "scripts/fetch_news.py"]),
    ("🔊 Озвучка TTS",  [sys.executable, "scripts/generate_audio.py"]),
    ("🏗️  Сборка HTML",  [sys.executable, "scripts/build_site.py"]),
]

print("\n" + "=" * 60)
print("🎬  КИНОВЕКНА 2026 — Полный запуск пайплайна")
print("=" * 60 + "\n")

for name, cmd in steps:
    print(f"\n{'─'*40}\n{name}\n{'─'*40}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"❌ Ошибка на шаге: {name}")
        sys.exit(1)

print("\n" + "=" * 60)
print("✅ Всё готово! Откройте index.html в браузере")
print("=" * 60 + "\n")
