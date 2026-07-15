#!/usr/bin/env python3
"""Migra referências internas SabVol/SabVolAudio para SabidosReceiver.

Cria backups .bak-migracao antes de alterar arquivos.
"""
from __future__ import annotations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REPLACEMENTS = (
    ("SabVolAudio.kicad_sch", "SabidosReceiver.kicad_sch"),
    ('(project "SabVolAudio"', '(project "SabidosReceiver"'),
    ('(project "SabVol"', '(project "SabidosReceiver"'),
)


def candidate(path: Path) -> bool:
    return path.is_file() and path.suffix in {".kicad_pro", ".kicad_sch", ".kicad_pcb", ".kicad_sym"}


def migrate(path: Path) -> bool:
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False
    updated = original
    for old, new in REPLACEMENTS:
        updated = updated.replace(old, new)
    if updated == original:
        return False
    backup = path.with_name(path.name + ".bak-migracao")
    if not backup.exists():
        backup.write_text(original, encoding="utf-8")
    path.write_text(updated, encoding="utf-8", newline="\n")
    print(f"atualizado: {path.relative_to(ROOT)}")
    return True


def main() -> int:
    total = sum(migrate(path) for path in sorted(ROOT.rglob("*")) if candidate(path))
    print(f"Arquivos atualizados: {total}")
    print("Abra o projeto no KiCad, salve as folhas e execute ERC/DRC.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
