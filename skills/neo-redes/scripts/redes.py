# /// script
# requires-python = ">=3.11"
# dependencies = ["reportlab>=4", "pypdfium2>=4", "pillow>=10", "svglib>=1.5", "skia-python>=87"]
# ///
# Punto de entrada único de la skill neo-redes.
#   uv run scripts/redes.py entorno           → revisa Python, librerías, fuentes y que se pueda generar
#   python3 scripts/redes.py entorno --json   → lo mismo en JSON (en Claude.ai, sin uv)
# Las dependencias de arriba son las candidatas de la fase 1 (ReportLab o skia-python); al elegir el
# renderizador se deja solo la que gane.
import argparse
import importlib
import json
import platform
import sys
import tempfile
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
FUENTES = SKILL / "assets" / "fonts"
PESOS = ["Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black"]
ESPERADAS = [f"Montserrat-{p}.ttf" for p in PESOS] + [
    "Montserrat-Italic.ttf" if p == "Regular" else f"Montserrat-{p}Italic.ttf" for p in PESOS]

# módulo → (paquete en PyPI, para qué se usa, obligatorio)
LIBRERIAS = {
    "reportlab": ("reportlab", "PDF (candidata)", False),
    "skia": ("skia-python", "PDF y PNG (candidata)", False),
    "pypdfium2": ("pypdfium2", "PNG desde el PDF", True),
    "PIL": ("pillow", "imágenes y vista previa", True),
    "svglib": ("svglib", "logos SVG en ReportLab", False),
}


def revisar_librerias() -> dict:
    estado = {}
    for modulo, (paquete, uso, obligatorio) in LIBRERIAS.items():
        try:
            importlib.import_module(modulo)
            estado[modulo] = {"ok": True, "version": version(paquete), "uso": uso}
        except (ImportError, PackageNotFoundError) as e:
            estado[modulo] = {"ok": False, "error": str(e).splitlines()[0], "uso": uso,
                              "paquete": paquete, "obligatorio": obligatorio}
    return estado


def prueba_reportlab(carpeta: Path) -> Path:
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas

    pdfmetrics.registerFont(TTFont("Montserrat-ExtraBold", str(FUENTES / "Montserrat-ExtraBold.ttf")))
    ruta = carpeta / "prueba-reportlab.pdf"
    c = canvas.Canvas(str(ruta), pagesize=(1080, 1350))
    c.setFillColorRGB(0.02, 0.035, 0.09)
    c.rect(0, 0, 1080, 1350, stroke=0, fill=1)
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Montserrat-ExtraBold", 72)
    c.drawString(96, 675, "Comunicación NEO")
    c.save()
    return ruta


def prueba_skia(carpeta: Path) -> Path:
    import skia

    ruta = carpeta / "prueba-skia.pdf"
    fuente = skia.Font(skia.Typeface.MakeFromFile(str(FUENTES / "Montserrat-ExtraBold.ttf")), 72)
    flujo = skia.FILEWStream(str(ruta))
    with skia.PDF.MakeDocument(flujo) as doc:
        with doc.page(1080, 1350) as lienzo:
            lienzo.clear(skia.Color(5, 9, 23))
            lienzo.drawString("Comunicación NEO", 96, 675, fuente, skia.Paint(Color=skia.ColorWHITE))
    flujo.flush()
    del flujo
    return ruta


def rasterizar(pdf: Path) -> tuple[int, int]:
    import pypdfium2 as pdfium

    doc = pdfium.PdfDocument(str(pdf))
    imagen = doc[0].render(scale=0.25).to_pil()
    claros = sum(1 for p in imagen.convert("L").getdata() if p > 200)
    doc.close()
    if claros == 0:
        raise RuntimeError("el PNG salió sin texto visible")
    return imagen.size


def entorno(como_json: bool) -> int:
    libs = revisar_librerias()
    fuentes_faltan = [f for f in ESPERADAS if not (FUENTES / f).is_file()]
    pruebas = {}
    with tempfile.TemporaryDirectory(prefix="neo-redes-") as tmp:
        for nombre, funcion, modulo in (("reportlab", prueba_reportlab, "reportlab"), ("skia", prueba_skia, "skia")):
            if not libs[modulo]["ok"] or fuentes_faltan:
                continue
            try:
                pdf = funcion(Path(tmp))
                tamano = rasterizar(pdf) if libs["pypdfium2"]["ok"] else None
                pruebas[nombre] = {"ok": True, "pdf_bytes": pdf.stat().st_size, "png": tamano}
            except Exception as e:  # se informa cualquier falla, no se detiene la revisión
                pruebas[nombre] = {"ok": False, "error": f"{type(e).__name__}: {e}"}

    faltan = [d["paquete"] for d in libs.values() if not d["ok"] and d["obligatorio"]]
    puede_pdf = any(p["ok"] for p in pruebas.values())
    listo = sys.version_info >= (3, 11) and not faltan and not fuentes_faltan and puede_pdf
    informe = {
        "listo": listo,
        "python": platform.python_version(),
        "sistema": f"{platform.system()} {platform.machine()}",
        "librerias": libs,
        "fuentes_faltan": fuentes_faltan,
        "pruebas": pruebas,
    }

    if como_json:
        print(json.dumps(informe, ensure_ascii=False, indent=2))
        return 0 if listo else 1

    print(f"Python {informe['python']} en {informe['sistema']}")
    for modulo, d in libs.items():
        marca = "✓" if d["ok"] else ("✗" if d["obligatorio"] else "·")
        detalle = d["version"] if d["ok"] else f"no está (pip install {d['paquete']})"
        print(f"  {marca} {modulo:<10} {detalle:<34} {d['uso']}")
    print(f"  ✓ Montserrat ({len(ESPERADAS)} TTF)" if not fuentes_faltan else "  ✗ Faltan fuentes: " + ", ".join(fuentes_faltan))
    for nombre, p in pruebas.items():
        print(f"  {'✓' if p['ok'] else '✗'} PDF de prueba con {nombre}" + ("" if p["ok"] else f": {p['error']}"))
    if listo:
        print("Listo para generar piezas.")
    else:
        motivos = faltan + (["fuentes"] if fuentes_faltan else []) + ([] if puede_pdf else ["ningún renderizador de PDF funciona"])
        print("Falta: " + ", ".join(motivos))
    return 0 if listo else 1


def main() -> int:
    p = argparse.ArgumentParser(prog="redes.py", description="Herramientas de la skill neo-redes.")
    sub = p.add_subparsers(dest="comando", required=True)
    e = sub.add_parser("entorno", help="revisa que el entorno pueda generar piezas")
    e.add_argument("--json", action="store_true", help="informe en JSON")
    args = p.parse_args()
    if args.comando == "entorno":
        return entorno(args.json)
    return 2


if __name__ == "__main__":
    sys.exit(main())
