#!/usr/bin/env python3
# Arma el ZIP de la skill para subirlo a mano en Claude.ai (Personalizar → Skills). Solo para
# pruebas y el piloto: la distribución real es el plugin sincronizado desde este repo.
#   python3 tools/empaquetar-zip.py   → dist/neo-redes-<versión>.zip
import json
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "skills" / "neo-redes"
IGNORAR = {"__pycache__", ".DS_Store"}


def main() -> int:
    version = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text("utf-8"))["version"]
    destino = REPO / "dist" / f"neo-redes-{version}.zip"
    destino.parent.mkdir(exist_ok=True)
    archivos = sorted(p for p in SKILL.rglob("*")
                      if p.is_file() and not IGNORAR.intersection(p.relative_to(SKILL).parts))
    # la carpeta neo-redes/ va en la raíz del ZIP, con SKILL.md adentro
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for p in archivos:
            z.write(p, Path("neo-redes") / p.relative_to(SKILL))
    print(f"{destino.relative_to(REPO)}: {len(archivos)} archivos, {destino.stat().st_size / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
