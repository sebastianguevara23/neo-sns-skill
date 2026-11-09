#!/usr/bin/env python3
# Copia la marca desde neo-design (tokens y logos) y registra de qué versión vino.
#   python3 tools/sincronizar-marca.py                        → copia desde ../neo-design-skill
#   python3 tools/sincronizar-marca.py --desde <ruta>         → copia desde otro clon
#   python3 tools/sincronizar-marca.py --revisar              → solo compara; sale con 1 si hay diferencias
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "skills" / "neo-redes"

# origen (relativo a skills/neo-design del otro repo) → destino (relativo a skills/neo-redes)
ARCHIVOS = {
    "tokens/neo-tokens.json": "tokens/neo-tokens.json",
    "assets/logo/neo-25-navy.svg": "assets/logo/neo-25-navy.svg",
    "assets/logo/neo-25-white.svg": "assets/logo/neo-25-white.svg",
    "assets/logo/neo-navy.svg": "assets/logo/neo-navy.svg",
    "assets/logo/neo-white.svg": "assets/logo/neo-white.svg",
    "assets/logo/neo-isotipo-navy.svg": "assets/logo/neo-isotipo-navy.svg",
    "assets/logo/neo-isotipo-white.svg": "assets/logo/neo-isotipo-white.svg",
}


def sha256(ruta: Path) -> str:
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def git(origen: Path, *args: str) -> str | None:
    try:
        r = subprocess.run(["git", "-C", str(origen), *args], capture_output=True, text=True, check=True)
        return r.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def main() -> int:
    p = argparse.ArgumentParser(description="Copia tokens y logos desde neo-design.")
    p.add_argument("--desde", type=Path, default=REPO.parent / "neo-design-skill",
                   help="clon del repo neo-design-skill (por defecto, ../neo-design-skill)")
    p.add_argument("--revisar", action="store_true", help="solo compara, sin copiar")
    args = p.parse_args()

    origen = args.desde.resolve() / "skills" / "neo-design"
    if not (origen / "tokens" / "neo-tokens.json").is_file():
        print(f"No encuentro neo-design en {origen}. Indica el clon con --desde.", file=sys.stderr)
        return 2

    faltan = [o for o in ARCHIVOS if not (origen / o).is_file()]
    if faltan:
        print("En neo-design faltan: " + ", ".join(faltan), file=sys.stderr)
        return 2

    distintos = [d for o, d in ARCHIVOS.items()
                 if not (SKILL / d).is_file() or sha256(origen / o) != sha256(SKILL / d)]

    version = json.loads((origen / "tokens" / "neo-tokens.json").read_text("utf-8"))["$extensions"]["neo"]["version"]

    if args.revisar:
        if distintos:
            print(f"Desactualizado respecto de neo-design {version}: " + ", ".join(distintos))
            return 1
        print(f"Al día con neo-design {version}.")
        return 0

    for o, d in ARCHIVOS.items():
        (SKILL / d).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(origen / o, SKILL / d)

    commit = git(origen, "rev-parse", "HEAD")
    sucio = git(origen, "status", "--porcelain", "--", "skills/neo-design/tokens", "skills/neo-design/assets/logo")
    registro = {
        "fuente": "neo-design-skill",
        "version": version,
        "commit": commit,
        "cambios_sin_commit": bool(sucio),
        "fecha": date.today().isoformat(),
        "archivos": {d: sha256(SKILL / d) for d in ARCHIVOS.values()},
    }
    (SKILL / "tokens" / "ORIGEN.json").write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", "utf-8")

    estado = f"{len(distintos)} archivo(s) actualizado(s)" if distintos else "sin cambios"
    print(f"Marca sincronizada desde neo-design {version} ({(commit or 'sin git')[:7]}): {estado}.")
    if sucio:
        print("Aviso: neo-design tiene cambios sin commit en tokens o logos; se copiaron igual.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
