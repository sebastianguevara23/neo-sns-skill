# /// script
# requires-python = ">=3.11"
# dependencies = ["reportlab>=4", "svglib>=1.5", "skia-python>=87", "pillow>=10", "pypdfium2>=4"]
# ///
# Fase 1: genera la pieza y el carrusel de prueba en tres variantes de PDF para importarlos en
# Canva y comparar cómo llega cada elemento. La escena se escribe a mano (todavía no hay motor).
#   uv run tests/prueba-canva/generar.py   → tests/prueba-canva/salida/
#
#   A  ReportLab, un objeto de texto por párrafo
#   B  ReportLab, un objeto de texto por línea
#   C  skia-python, párrafos con interletraje (kerning)
import re
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / "skills" / "neo-redes"
FUENTES = SKILL / "assets" / "fonts"
LOGOS = SKILL / "assets" / "logo"
AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / "salida"
W, H = 1080, 1350

PESOS = {"Regular": 400, "Medium": 500, "SemiBold": 600, "Bold": 700, "ExtraBold": 800, "Black": 900}

# Tokens de neo-tokens.json usados en la prueba
NIGHT_GROUND, NIGHT_RAISED = "#050917", "#191F2F"
NAVY_800, NAVY_600, NAVY_450, NAVY_300, NAVY_100 = "#000033", "#223C63", "#527198", "#8DA3C0", "#E1E6EE"
AZUL, AZUL_SUAVE, AZUL_800 = "#2D5BFF", "#7E99FE", "#172A91"
TENUE_OSCURO, BLANCO = "#C1C6D2", "#FFFFFF"


def archivo_fuente(estilo: str) -> Path:
    return FUENTES / f"Montserrat-{estilo}.ttf"


# ---------- recursos raster (se generan, no se descargan) ----------

def preparar_recursos(carpeta: Path) -> dict:
    carpeta.mkdir(parents=True, exist_ok=True)
    # Luz difusa: círculo azul desenfocado sobre transparente
    luz = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(luz).ellipse((620, 640, 1180, 1200), fill=(45, 91, 255, 150))
    luz = luz.filter(ImageFilter.GaussianBlur(120))
    luz.save(carpeta / "luz-difusa.png")
    # Foto de prueba: fachada abstracta (no es una foto real; solo ocupa el lugar)
    foto = Image.new("RGB", (1080, 560))
    d = ImageDraw.Draw(foto)
    for y in range(560):
        t = y / 560
        d.line([(0, y), (1080, y)], fill=(int(150 - 90 * t), int(160 - 90 * t), int(175 - 80 * t)))
    for col in range(9):
        x0 = 60 + col * 112
        for fila in range(6):
            y0 = 60 + fila * 80
            gris = 70 + ((col * 7 + fila * 13) % 5) * 22
            d.rectangle((x0, y0, x0 + 80, y0 + 52), fill=(gris, gris + 8, gris + 20))
    foto.save(carpeta / "foto-prueba.jpg", quality=90)
    return {"luz": carpeta / "luz-difusa.png", "foto": carpeta / "foto-prueba.jpg"}


# ---------- escena ----------
# Coordenadas desde la esquina superior izquierda, en px (1 px = 1 pt en el PDF).
# En los textos, "y" es la línea base de la primera línea.

def linea(*runs):
    return list(runs)


def escena_pieza(r: dict) -> list:
    return [
        {"tipo": "rect", "nombre": "Fondo", "x": 0, "y": 0, "w": W, "h": H, "relleno": NIGHT_GROUND},
        {"tipo": "imagen", "nombre": "Luz difusa", "x": 0, "y": 0, "w": W, "h": H, "archivo": r["luz"]},
        {"tipo": "imagen", "nombre": "Foto", "x": 0, "y": 0, "w": 1080, "h": 560, "archivo": r["foto"]},
        {"tipo": "rect", "nombre": "Duotono", "x": 0, "y": 0, "w": 1080, "h": 560, "relleno": AZUL, "opacidad": 0.55},
        {"tipo": "rect", "nombre": "Barra de acento", "x": 96, "y": 640, "w": 8, "h": 40, "relleno": AZUL, "radio": 3},
        {"tipo": "texto", "nombre": "Kicker", "x": 124, "y": 672, "px": 32, "espaciado": 0.08,
         "lineas": [linea(("CASO DE ÉXITO", "SemiBold", AZUL_SUAVE))]},
        {"tipo": "texto", "nombre": "Cifra", "x": 88, "y": 860, "px": 200,
         "lineas": [linea(("-40 %", "ExtraBold", BLANCO))]},
        {"tipo": "texto", "nombre": "Titular", "x": 96, "y": 950, "px": 64,
         "lineas": [linea(("en tiempo de ", "ExtraBold", BLANCO), ("soporte", "ExtraBoldItalic", AZUL_SUAVE))]},
        {"tipo": "degradado", "nombre": "Divisor", "x": 96, "y": 996, "w": 420, "h": 6,
         "desde": AZUL, "hasta": NIGHT_GROUND, "direccion": "horizontal"},
        {"tipo": "texto", "nombre": "Cuerpo", "x": 96, "y": 1070, "px": 34, "interlineado": 1.4,
         "lineas": [linea(("Automatización de la mesa de ayuda", "Regular", TENUE_OSCURO)),
                    linea(("de un banco regional.", "Regular", TENUE_OSCURO))]},
        {"tipo": "svg", "nombre": "Logo", "x": 96, "y": 1226, "h": 60, "archivo": LOGOS / "neo-25-white.svg"},
        {"tipo": "circulo", "nombre": "Botón", "cx": 944, "cy": 1256, "r": 40, "relleno": AZUL},
        {"tipo": "trazo", "nombre": "Ícono flecha", "x": 920, "y": 1232, "escala": 2, "color": BLANCO, "ancho": 4,
         "lineas": [[(5, 12), (19, 12)], [(12, 5), (19, 12), (12, 19)]]},
    ]


def numeracion(n: int, total: int, color: str) -> dict:
    return {"tipo": "texto", "nombre": "Numeración", "x": 900, "y": 1268, "px": 32,
            "lineas": [linea((f"{n}/{total}", "SemiBold", color))]}


def escena_carrusel() -> list:
    portada = [
        {"tipo": "rect", "nombre": "Fondo", "x": 0, "y": 0, "w": W, "h": H, "relleno": BLANCO},
        {"tipo": "texto", "nombre": "Kicker", "x": 96, "y": 220, "px": 32, "espaciado": 0.08,
         "lineas": [linea(("GUÍA", "SemiBold", AZUL))]},
        {"tipo": "texto", "nombre": "Titular", "x": 96, "y": 360, "px": 88, "interlineado": 1.15,
         "lineas": [linea(("Tres claves para", "ExtraBold", NAVY_800)),
                    linea(("implementar", "ExtraBold", NAVY_800)),
                    linea(("agentes", "ExtraBoldItalic", AZUL), (" de IA", "ExtraBold", NAVY_800))]},
        {"tipo": "degradado", "nombre": "Divisor", "x": 96, "y": 640, "w": 420, "h": 6,
         "desde": AZUL, "hasta": BLANCO, "direccion": "horizontal"},
        {"tipo": "svg", "nombre": "Logo", "x": 96, "y": 1226, "h": 60, "archivo": LOGOS / "neo-25-navy.svg"},
        numeracion(1, 3, NAVY_450),
    ]
    lamina = [
        {"tipo": "rect", "nombre": "Fondo", "x": 0, "y": 0, "w": W, "h": H, "relleno": BLANCO},
        {"tipo": "texto", "nombre": "Kicker", "x": 96, "y": 180, "px": 32, "espaciado": 0.08,
         "lineas": [linea(("CLAVE 1", "SemiBold", AZUL))]},
        {"tipo": "texto", "nombre": "Titular", "x": 96, "y": 270, "px": 64,
         "lineas": [linea(("Define fronteras claras", "ExtraBold", NAVY_800))]},
        {"tipo": "texto", "nombre": "Cuerpo", "x": 96, "y": 350, "px": 36, "interlineado": 1.4,
         "lineas": [linea(("Decide qué puede hacer un agente solo", "Regular", NAVY_600)),
                    linea(("y en qué momento ", "Regular", NAVY_600), ("pide aprobación", "SemiBold", NAVY_800)),
                    linea(("a una persona.", "Regular", NAVY_600))]},
        {"tipo": "rect", "nombre": "Espacio de foto", "x": 96, "y": 520, "w": 888, "h": 620, "relleno": NAVY_100,
         "radio": 6, "borde": {"color": NAVY_300, "ancho": 3, "guiones": [14, 10]}},
        {"tipo": "texto", "nombre": "Etiqueta de foto", "x": 470, "y": 842, "px": 32,
         "lineas": [linea(("Foto", "SemiBold", NAVY_450))]},
        {"tipo": "svg", "nombre": "Logo", "x": 96, "y": 1226, "h": 60, "archivo": LOGOS / "neo-25-navy.svg"},
        numeracion(2, 3, NAVY_450),
    ]
    cierre = [
        {"tipo": "degradado", "nombre": "Fondo", "x": 0, "y": 0, "w": W, "h": H,
         "desde": AZUL, "hasta": AZUL_800, "direccion": "diagonal"},
        {"tipo": "texto", "nombre": "Titular", "x": 96, "y": 560, "px": 96,
         "lineas": [linea(("Conversemos", "ExtraBold", BLANCO))]},
        {"tipo": "texto", "nombre": "Llamada a la acción", "x": 96, "y": 650, "px": 36,
         "lineas": [linea(("Conoce más en ", "Regular", BLANCO), ("neoconsulting.ai", "SemiBold", BLANCO))]},
        {"tipo": "svg", "nombre": "Logo", "x": 96, "y": 1226, "h": 60, "archivo": LOGOS / "neo-25-white.svg"},
        numeracion(3, 3, BLANCO),
    ]
    return [portada, lamina, cierre]


# ---------- ReportLab (variantes A y B) ----------

def pdf_reportlab(paginas: list, ruta: Path, por_linea: bool) -> None:
    from reportlab.graphics import renderPDF, shapes
    from reportlab.lib.colors import HexColor
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    from svglib.svglib import svg2rlg

    for f in FUENTES.glob("Montserrat-*.ttf"):
        if f.stem not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(f.stem, str(f)))

    # Sin esto, ReportLab (al abrir cada página) y renderPDF (al dibujar cada SVG) declaran
    # Helvetica sin incrustar en objetos de texto vacíos, y el importador de Canva podría
    # tomarla como una fuente faltante.
    shapes.STATE_DEFAULTS["fontName"] = "Montserrat-Regular"
    c = canvas.Canvas(str(ruta), pagesize=(W, H), initialFontName="Montserrat-Regular")
    c.setTitle(ruta.stem)
    c.setAuthor("NEO Consulting")
    for capas in paginas:
        for k in capas:
            t = k["tipo"]
            c.saveState()
            if t == "rect":
                c.setFillColor(HexColor(k["relleno"]))
                if "opacidad" in k:
                    c.setFillAlpha(k["opacidad"])
                borde = k.get("borde")
                if borde:
                    c.setStrokeColor(HexColor(borde["color"]))
                    c.setLineWidth(borde["ancho"])
                    c.setDash(*borde["guiones"])
                c.roundRect(k["x"], H - k["y"] - k["h"], k["w"], k["h"], k.get("radio", 0),
                            stroke=1 if borde else 0, fill=1)
            elif t == "degradado":
                x, y0, w, h = k["x"], H - k["y"] - k["h"], k["w"], k["h"]
                p = c.beginPath()
                p.rect(x, y0, w, h)
                c.clipPath(p, stroke=0, fill=0)
                fin = (x + w, y0) if k["direccion"] == "horizontal" else (x + w, y0)
                inicio = (x, y0) if k["direccion"] == "horizontal" else (x, y0 + h)
                c.linearGradient(*inicio, *fin, (HexColor(k["desde"]), HexColor(k["hasta"])), extend=False)
            elif t == "imagen":
                c.drawImage(ImageReader(str(k["archivo"])), k["x"], H - k["y"] - k["h"], k["w"], k["h"], mask="auto")
            elif t == "texto":
                px, alto = k["px"], k["px"] * k.get("interlineado", 1.2)
                espaciado = k.get("espaciado", 0) * px
                if por_linea:
                    for i, runs in enumerate(k["lineas"]):
                        to = c.beginText(k["x"], H - (k["y"] + i * alto))
                        to.setCharSpace(espaciado)
                        for texto, estilo, color in runs:
                            to.setFont(f"Montserrat-{estilo}", px)
                            to.setFillColor(HexColor(color))
                            to.textOut(texto)
                        c.drawText(to)
                else:
                    to = c.beginText(k["x"], H - k["y"])
                    to.setLeading(alto)
                    to.setCharSpace(espaciado)
                    for runs in k["lineas"]:
                        for texto, estilo, color in runs:
                            to.setFont(f"Montserrat-{estilo}", px, leading=alto)
                            to.setFillColor(HexColor(color))
                            to.textOut(texto)
                        to.textLine("")
                    c.drawText(to)
            elif t == "svg":
                d = svg2rlg(str(k["archivo"]))
                s = k["h"] / d.height
                d.width, d.height = d.width * s, d.height * s
                d.scale(s, s)
                renderPDF.draw(d, c, k["x"], H - k["y"] - k["h"])
            elif t == "circulo":
                c.setFillColor(HexColor(k["relleno"]))
                c.circle(k["cx"], H - k["cy"], k["r"], stroke=0, fill=1)
            elif t == "trazo":
                c.setStrokeColor(HexColor(k["color"]))
                c.setLineWidth(k["ancho"])
                c.setLineCap(1)
                c.setLineJoin(1)
                for puntos in k["lineas"]:
                    p = c.beginPath()
                    for i, (px_, py_) in enumerate(puntos):
                        X, Y = k["x"] + px_ * k["escala"], H - (k["y"] + py_ * k["escala"])
                        p.moveTo(X, Y) if i == 0 else p.lineTo(X, Y)
                    c.drawPath(p, stroke=1, fill=0)
            c.restoreState()
        c.showPage()
    c.save()


# ---------- skia-python (variante C) ----------

def pdf_skia(paginas: list, ruta: Path) -> None:
    import skia

    tl = skia.textlayout
    proveedor = tl.TypefaceFontProvider()
    for f in FUENTES.glob("Montserrat-*.ttf"):
        proveedor.registerTypeface(skia.Typeface.MakeFromFile(str(f)), "Montserrat")
    coleccion = tl.FontCollection()
    coleccion.setDefaultFontManager(proveedor)
    unicode = skia.Unicode.ICU_Make()

    def color(hexa: str, alfa: float = 1.0) -> int:
        h = hexa.lstrip("#")
        return skia.Color(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), round(255 * alfa))

    def estilo_texto(px, estilo, hexa, interlineado, espaciado):
        cursiva = estilo.endswith("Italic")
        base = estilo[:-6] if cursiva else estilo
        peso = PESOS.get(base or "Regular", 400)
        ts = tl.TextStyle()
        ts.setFontFamilies(["Montserrat"])
        ts.setFontSize(px)
        ts.setFontStyle(skia.FontStyle(peso, skia.FontStyle.kNormal_Width,
                                       skia.FontStyle.kItalic_Slant if cursiva else skia.FontStyle.kUpright_Slant))
        ts.setColor(color(hexa))
        ts.setHeight(interlineado)
        ts.setHeightOverride(True)
        ts.setLetterSpacing(espaciado)
        return ts

    flujo = skia.FILEWStream(str(ruta))
    doc = skia.PDF.MakeDocument(flujo, Title=ruta.stem, Author="NEO Consulting")
    for capas in paginas:
        lienzo = doc.beginPage(W, H)
        for k in capas:
            t = k["tipo"]
            if t == "rect":
                rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(k["x"], k["y"], k["w"], k["h"]),
                                           k.get("radio", 0), k.get("radio", 0))
                lienzo.drawRRect(rr, skia.Paint(Color=color(k["relleno"], k.get("opacidad", 1)), AntiAlias=True))
                borde = k.get("borde")
                if borde:
                    trazo = skia.Paint(Color=color(borde["color"]), Style=skia.Paint.kStroke_Style,
                                       StrokeWidth=borde["ancho"], AntiAlias=True,
                                       PathEffect=skia.DashPathEffect.Make(borde["guiones"], 0))
                    lienzo.drawRRect(rr, trazo)
            elif t == "degradado":
                x, y, w, h = k["x"], k["y"], k["w"], k["h"]
                fin = (x + w, y) if k["direccion"] == "horizontal" else (x + w, y + h)
                sombra = skia.GradientShader.MakeLinear([(x, y), fin], [color(k["desde"]), color(k["hasta"])])
                lienzo.drawRect(skia.Rect.MakeXYWH(x, y, w, h), skia.Paint(Shader=sombra))
            elif t == "imagen":
                img = skia.Image.open(str(k["archivo"]))
                lienzo.drawImageRect(img, skia.Rect.MakeXYWH(k["x"], k["y"], k["w"], k["h"]),
                                     skia.SamplingOptions(skia.FilterMode.kLinear))
            elif t == "texto":
                px = k["px"]
                interlineado = k.get("interlineado", 1.2)
                ps = tl.ParagraphStyle()
                b = tl.ParagraphBuilder(ps, coleccion, unicode)
                ultima = len(k["lineas"]) - 1
                for i, runs in enumerate(k["lineas"]):
                    for j, (texto, estilo, hexa) in enumerate(runs):
                        b.pushStyle(estilo_texto(px, estilo, hexa, interlineado, k.get("espaciado", 0) * px))
                        # el salto va dentro del último tramo, para que tome su tamaño y no el del párrafo
                        b.addText(texto + ("\n" if j == len(runs) - 1 and i < ultima else ""))
                        b.pop()
                p = b.Build()
                p.layout(W * 2)
                p.paint(lienzo, k["x"], k["y"] - p.AlphabeticBaseline)
            elif t == "svg":
                dom = skia.SVGDOM.MakeFromStream(skia.Stream.MakeFromFile(str(k["archivo"])))
                # los logos solo traen viewBox: el tamaño intrínseco sale de ahí
                caja = re.search(r'viewBox="([^"]+)"', k["archivo"].read_text("utf-8")).group(1)
                ancho, alto = (float(v) for v in caja.split()[2:])
                s = k["h"] / alto
                lienzo.save()
                lienzo.translate(k["x"], k["y"])
                lienzo.scale(s, s)
                dom.setContainerSize(skia.Size(ancho, alto))
                dom.render(lienzo)
                lienzo.restore()
            elif t == "circulo":
                lienzo.drawCircle(k["cx"], k["cy"], k["r"], skia.Paint(Color=color(k["relleno"]), AntiAlias=True))
            elif t == "trazo":
                pintura = skia.Paint(Color=color(k["color"]), Style=skia.Paint.kStroke_Style, StrokeWidth=k["ancho"],
                                     StrokeCap=skia.Paint.kRound_Cap, StrokeJoin=skia.Paint.kRound_Join, AntiAlias=True)
                for puntos in k["lineas"]:
                    trazo = skia.Path()
                    for i, (px_, py_) in enumerate(puntos):
                        X, Y = k["x"] + px_ * k["escala"], k["y"] + py_ * k["escala"]
                        trazo.moveTo(X, Y) if i == 0 else trazo.lineTo(X, Y)
                    lienzo.drawPath(trazo, pintura)
        doc.endPage()
    doc.close()
    flujo.flush()
    del flujo


# ---------- PNG y hoja de contacto ----------

def rasterizar(pdf: Path) -> list[Path]:
    import pypdfium2 as pdfium

    doc = pdfium.PdfDocument(str(pdf))
    rutas = []
    for i in range(len(doc)):
        ruta = pdf.with_name(f"{pdf.stem}-{i + 1}.png" if len(doc) > 1 else f"{pdf.stem}.png")
        doc[i].render(scale=1).to_pil().save(ruta)
        rutas.append(ruta)
    doc.close()
    return rutas


def hoja(pngs: dict, ruta: Path) -> None:
    # una fila por variante: pieza y las tres láminas del carrusel, a 270 px de ancho
    ancho, alto, margen = 270, 338, 24
    filas = list(pngs.items())
    columnas = max(len(v) for _, v in filas)
    lienzo = Image.new("RGB", (margen + columnas * (ancho + margen) + 60, margen + len(filas) * (alto + margen)), "white")
    d = ImageDraw.Draw(lienzo)
    for f, (variante, rutas) in enumerate(filas):
        y = margen + f * (alto + margen)
        d.text((8, y + alto // 2), variante, fill="black")
        for c, r in enumerate(rutas):
            lienzo.paste(Image.open(r).resize((ancho, alto)), (60 + c * (ancho + margen), y))
    lienzo.save(ruta)


def main() -> None:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    recursos = preparar_recursos(SALIDA / "recursos")
    pieza, carrusel = [escena_pieza(recursos)], escena_carrusel()
    pngs = {}
    for variante, generar in (
        ("A", lambda p, r: pdf_reportlab(p, r, por_linea=False)),
        ("B", lambda p, r: pdf_reportlab(p, r, por_linea=True)),
        ("C", pdf_skia),
    ):
        rutas = []
        for nombre, paginas in (("pieza", pieza), ("carrusel", carrusel)):
            pdf = SALIDA / f"{variante}-{nombre}.pdf"
            generar(paginas, pdf)
            rutas += rasterizar(pdf)
        pngs[variante] = rutas
        print(f"Variante {variante}: {', '.join(r.name for r in rutas)}")
    hoja(pngs, SALIDA / "hoja-variantes.png")
    print(f"Listo en {SALIDA.relative_to(REPO)}")


if __name__ == "__main__":
    main()
