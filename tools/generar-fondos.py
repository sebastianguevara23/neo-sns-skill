# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Fondos NEO en PNG para dibujar piezas en Canva.

El conector de Canva solo pinta colores planos: el degradado claro y el navy con luces
difusas entran como imagen de fondo. En Figma no hacen falta (se dibujan nativos).

Uso: uv run tools/generar-fondos.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

REPO = Path(__file__).resolve().parent.parent
SALIDA = REPO / "skills" / "neo-redes" / "assets" / "fondos"
TAMANOS = [(1080, 1080), (1080, 1350), (1080, 1920)]

CLARO_ARRIBA = "#E8F0FE"
CLARO_ABAJO = "#FFFFFF"
NAVY = "#000033"
AZUL = "#2D5BFF"
# Luces: centro (fracción del ancho y del alto), radio (fracción del ancho) e intensidad.
LUCES = [((0.92, 0.06), 0.30, 0.50), ((0.04, 0.96), 0.32, 0.38)]


def rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def claro(w: int, h: int) -> Image.Image:
    a, b = rgb(CLARO_ARRIBA), rgb(CLARO_ABAJO)
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / (h - 1)
        d.line([(0, y), (w, y)], fill=tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3)))
    return img


def navy_luces(w: int, h: int) -> Image.Image:
    img = Image.new("RGB", (w, h), rgb(NAVY))
    azul = Image.new("RGB", (w, h), rgb(AZUL))
    for (cx, cy), r, k in LUCES:
        mascara = Image.new("L", (w, h), 0)
        x, y, rr = cx * w, cy * h, r * w
        ImageDraw.Draw(mascara).ellipse([x - rr, y - rr, x + rr, y + rr], fill=round(255 * k))
        mascara = mascara.filter(ImageFilter.GaussianBlur(w * 0.16))
        img = Image.composite(azul, img, mascara)
    return img


def main() -> None:
    SALIDA.mkdir(parents=True, exist_ok=True)
    for w, h in TAMANOS:
        for nombre, dibujar in (("claro", claro), ("navy-luces", navy_luces)):
            ruta = SALIDA / f"{nombre}-{w}x{h}.png"
            dibujar(w, h).save(ruta, optimize=True)
            print(f"{ruta.relative_to(REPO)}  {ruta.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
