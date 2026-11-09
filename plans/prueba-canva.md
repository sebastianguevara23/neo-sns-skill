# Fase 1: prueba de importación en Canva y de entornos

Guía y registro de la prueba que decide el renderizador y cómo se escribe el texto en el
PDF (`arquitectura.md` §5.3 y §8). Hasta completarla no se construye el motor.

## Qué se probó ya (2026-11-09)

**Archivos de prueba.** `uv run tests/prueba-canva/generar.py` deja en
`tests/prueba-canva/salida/` una pieza 4:5 oscura y un carrusel claro de 3 láminas, cada uno
en tres variantes, más `hoja-variantes.png` con todas las vistas previas.

| Variante | Cómo escribe el texto | Lo que se ve por dentro |
|---|---|---|
| **A** ReportLab por párrafo | Un objeto de texto por bloque; los tramos con otro peso o color van dentro del mismo objeto | Texto como cadenas normales, fuentes TrueType recortadas con tabla Unicode. Sin interletraje |
| **B** ReportLab por línea | Un objeto de texto por línea | Igual que A, pero el cuerpo de dos líneas son dos objetos |
| **C** skia-python | Párrafos con el motor de texto de skia | Fuentes CID con tabla Unicode, con interletraje, pero **cada letra va posicionada por separado**. Es la que más riesgo tiene de llegar a Canva como letras sueltas |

En las tres variantes el texto se extrae correcto, con tildes, y las únicas fuentes declaradas
son las cuatro Montserrat usadas. A y B declaraban además Helvetica sin incrustar en objetos
de texto vacíos; se corrigió en el generador porque Canva podría tomarla como fuente faltante.
A simple vista, las tres variantes se ven iguales en el PNG.

**Entorno Linux.** `uv run skills/neo-redes/scripts/redes.py entorno`: `uv` trajo Python 3.13
y las cinco librerías, y ambos renderizadores generan y rasterizan un PDF. Con el Python del
sistema y sin `uv`, el comando informa qué falta y cómo instalarlo.

## Qué falta (lo hace una persona)

### 1. Importar en Canva

Con una cuenta de Canva Pro, importa los 6 PDF de `tests/prueba-canva/salida/` (`A-pieza.pdf`,
`A-carrusel.pdf`, `B-…`, `C-…`). En la página de inicio de Canva: **Subir** (o arrastra el PDF
a la ventana) y ábrelo como diseño editable. Ten a mano `hoja-variantes.png` para comparar.

Para cada variante, revisa y anota en la tabla de resultados:

| # | Qué mirar | Cómo |
|---|---|---|
| 1 | Tamaño del diseño | ¿Canva lo abre en 1080 × 1350 px? |
| 2 | Texto editable | Doble clic en el titular: ¿se puede escribir? |
| 3 | Cuadros de texto | El cuerpo de dos líneas, ¿llega en **un** cuadro o en dos? ¿Alguna palabra o letra llega suelta? |
| 4 | Fuente | ¿Dice Montserrat con el peso correcto (SemiBold, ExtraBold, Regular)? ¿Avisa de fuentes faltantes? |
| 5 | Cursiva y color mixtos | «soporte» en cursiva azul dentro del titular blanco: ¿se mantiene en el mismo cuadro? |
| 6 | Espaciado del kicker | «CASO DE ÉXITO» con letras separadas: ¿se conserva? |
| 7 | Colores | Selecciona el titular y el fondo: ¿los HEX son `#FFFFFF` y `#050917`? |
| 8 | Duotono | La capa azul sobre la foto: ¿es una forma con transparencia que se puede editar o borrar? |
| 9 | Foto | ¿Se puede reemplazar arrastrando otra imagen encima? |
| 10 | Luz difusa | ¿Llega como imagen con transparencia, sin fondo negro? |
| 11 | Divisor degradado | ¿Forma con degradado editable, imagen o se perdió? |
| 12 | Logo | ¿Vector con color editable, imagen o muchas piezas sueltas? |
| 13 | Ícono y botón | La flecha y el círculo azul: ¿formas editables? |
| 14 | Reflujo | Agrega dos palabras al cuerpo: ¿el cuadro se ajusta bien? Compara saltos de línea con el PNG |
| 15 | Nombres de capas | En el panel de capas, ¿aparece algún nombre útil? |
| 16 | Carrusel | ¿Crea un diseño de 3 páginas? |
| 17 | Espacio de foto (lámina 2) | Arrastra una foto sobre el recuadro punteado: ¿lo reemplaza, queda encima o hay que borrarlo primero? |
| 18 | Fondo degradado (lámina 3) | ¿Llega como degradado editable o como imagen? |

Captura de pantalla de cada variante abierta en Canva, con el panel de capas visible si se
puede, y déjalas en `tests/prueba-canva/capturas/`.

**Opcional, LinkedIn:** sube `A-carrusel.pdf` como documento en una publicación nueva, mira
la vista previa y descártala sin publicar.

### 2. Entorno de Claude.ai

1. `python3 tools/empaquetar-zip.py` arma `dist/neo-redes-0.1.0.zip`.
2. En Claude.ai, activa *Configuración → Capacidades → Ejecución de código y creación de
   archivos* y sube el ZIP en *Personalizar → Skills*.
3. En un chat nuevo: «Corre `python3 scripts/redes.py entorno --json` de la skill neo-redes y
   muéstrame el resultado completo. Después intenta
   `pip install reportlab pypdfium2 svglib skia-python` y vuelve a correrlo».
4. Pega aquí ambos resultados.

### 3. Entorno local en Mac y Windows

En una máquina sin Python, con el ZIP descomprimido:

- **Mac:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Windows (PowerShell):** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Luego, en una terminal nueva: `uv run neo-redes/scripts/redes.py entorno`. Anota si pidió
permisos de administrador, cuánto tardó la primera vez y el resultado.

## Resultados

### Canva

| # | A (por párrafo) | B (por línea) | C (skia) |
|---|---|---|---|
| 1 Tamaño | | | |
| 2 Texto editable | | | |
| 3 Cuadros de texto | | | |
| 4 Fuente | | | |
| 5 Cursiva y color mixtos | | | |
| 6 Espaciado del kicker | | | |
| 7 Colores | | | |
| 8 Duotono | | | |
| 9 Foto | | | |
| 10 Luz difusa | | | |
| 11 Divisor degradado | | | |
| 12 Logo | | | |
| 13 Ícono y botón | | | |
| 14 Reflujo | | | |
| 15 Nombres de capas | | | |
| 16 Carrusel | | | |
| 17 Espacio de foto | | | |
| 18 Fondo degradado | | | |

### Entornos

| Entorno | Resultado |
|---|---|
| Linux (uv) | Listo: Python 3.13, ReportLab 5.1, skia-python 144.1, pypdfium2 5.15, Pillow 13, svglib 2.4 |
| Claude.ai | Pendiente |
| Mac (uv desde cero) | Pendiente |
| Windows (uv desde cero) | Pendiente |

## Cómo se decide

En este orden:

1. **Texto editable en un cuadro por párrafo** (o, como mínimo, por línea) con Montserrat
   reconocida.
2. **Formas, colores y transparencias editables**, y una forma cómoda de reemplazar fotos.
3. **Corre en Claude.ai** sin instalar nada, o con un `pip install` que funcione.
4. Fidelidad visual (interletraje).

Si gana A o B, se elige ReportLab y skia-python sale de las dependencias. Si solo C deja el
texto bien, se elige skia-python. Si ninguna deja el texto editable, se detiene el proyecto y
se replantea la salida con el equipo (`plan-implementacion.md`, fase 1).

## Decisión

Pendiente de los resultados.
