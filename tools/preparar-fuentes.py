# /// script
# requires-python = ">=3.11"
# dependencies = ["fonttools>=4.47"]
# ///
# Descarga Montserrat (variable) del repositorio oficial de Google Fonts y genera las TTF
# estáticas que usa la skill: los renderizadores de PDF no aceptan fuentes variables, y
# neo-design solo trae woff2 recortadas.
#   uv run tools/preparar-fuentes.py
import json
import shutil
import sys
import tempfile
import urllib.request
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

REPO = Path(__file__).resolve().parent.parent
DESTINO = REPO / "skills" / "neo-redes" / "assets" / "fonts"
BASE = "https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/"
VARIABLES = {"": "Montserrat%5Bwght%5D.ttf", "Italic": "Montserrat-Italic%5Bwght%5D.ttf"}
PESOS = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold", 900: "Black"}


def descargar(nombre: str, carpeta: Path) -> Path:
    ruta = carpeta / nombre.replace("%5B", "[").replace("%5D", "]")
    with urllib.request.urlopen(BASE + nombre, timeout=60) as r, open(ruta, "wb") as f:
        shutil.copyfileobj(r, f)
    return ruta


def nombre_estatico(peso: int, cursiva: str) -> str:
    if not cursiva:
        return f"Montserrat-{PESOS[peso]}"
    return "Montserrat-Italic" if peso == 400 else f"Montserrat-{PESOS[peso]}Italic"


def fijar_nombres(fuente: TTFont, peso: int, cursiva: bool) -> None:
    # La instancia hereda nombres de la variable (la cursiva sale como «MontserratItalic-Italic»).
    # Se reescriben con la convención de familias estáticas: Regular y Bold (y sus cursivas)
    # forman la familia «Montserrat»; los demás pesos son familias propias con el nombre
    # tipográfico (16 y 17) en común, como las publica Google Fonts.
    estilo = PESOS[peso]
    ribbi = peso in (400, 700)
    tipografico = ("Italic" if peso == 400 else f"{estilo} Italic") if cursiva else estilo
    if ribbi:
        sub = " ".join(p for p in ("Bold" if peso == 700 else "", "Italic" if cursiva else "") if p) or "Regular"
    else:
        sub = "Italic" if cursiva else "Regular"
    ps = nombre_estatico(peso, "Italic" if cursiva else "")
    tabla = fuente["name"]
    version = tabla.getDebugName(5)
    tabla.removeNames(platformID=1)
    for nid in (1, 2, 3, 4, 6, 16, 17, 25):
        tabla.removeNames(nameID=nid)
    registros = {1: "Montserrat" if ribbi else f"Montserrat {estilo}", 2: sub, 3: f"{version};{ps}",
                 4: f"Montserrat {tipografico}", 6: ps, 16: "Montserrat", 17: tipografico}
    for nid, texto in registros.items():
        tabla.setName(texto, nid, 3, 1, 0x409)

    os2 = fuente["OS/2"]
    os2.usWeightClass = peso
    sel = os2.fsSelection & ~0b1100001  # bits de cursiva (0), negrita (5) y regular (6)
    if cursiva:
        sel |= 1
    if peso == 700:
        sel |= 1 << 5
    if not cursiva and peso != 700:
        sel |= 1 << 6
    os2.fsSelection = sel
    fuente["head"].macStyle = (1 if peso == 700 else 0) | (2 if cursiva else 0)


def main() -> int:
    DESTINO.mkdir(parents=True, exist_ok=True)
    generadas = {}
    with tempfile.TemporaryDirectory(prefix="montserrat-") as tmp:
        carpeta = Path(tmp)
        shutil.copyfile(descargar("OFL.txt", carpeta), DESTINO / "OFL.txt")
        for cursiva, archivo in VARIABLES.items():
            variable = descargar(archivo, carpeta)
            for peso in PESOS:
                fuente = instancer.instantiateVariableFont(TTFont(variable), {"wght": peso})
                fijar_nombres(fuente, peso, bool(cursiva))
                nombre = nombre_estatico(peso, cursiva)
                fuente.save(DESTINO / f"{nombre}.ttf")
                generadas[f"{nombre}.ttf"] = fuente["name"].getDebugName(5)

    registro = {"fuente": BASE, "licencia": "SIL Open Font License 1.1 (OFL.txt)", "archivos": generadas}
    (DESTINO / "FUENTES.json").write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(f"{len(generadas)} fuentes en {DESTINO.relative_to(REPO)} ({next(iter(generadas.values()))}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
