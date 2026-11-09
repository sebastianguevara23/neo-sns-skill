# Estado y pendientes

Dónde quedó el trabajo y cómo retomarlo en otra máquina. Se actualiza al cerrar cada sesión.
Última actualización: 2026-11-09.

## Dónde estamos

| Fase | Estado | Dónde |
|---|---|---|
| 0. Base del repo | Cerrada | `main` (versión 0.1.0) |
| 1. Prueba de entrega en Canva y Figma | **En curso**: versión 0.2.0 de prueba (dibujo directo con conectores) | Rama **`fase-1`** |
| 2 en adelante | Sin empezar; se replantean según el resultado de la prueba | — |

**Giro del 2026-11-09: dibujo directo.** La persona no quiere subir ni importar archivos.
Se probaron los conectores oficiales: en Canva Claude puede dibujar una pieza completa
(páginas de tamaño exacto, fondos y logos subidos, formas y textos), pero no elegir
Montserrat ni sus pesos intermedios; en Figma puede leer, y escribir requiere puesto Full.
La versión 0.2.0 de la skill dibuja así, sin plantillas ni Python, para probarla con una
persona (`prueba-canva.md`, sección 4). `decisiones.md`, `arquitectura.md` y
`plan-implementacion.md` todavía describen el enfoque de PDF: se reescriben con los
resultados de esta prueba. El repo es público desde este día.

El contrato está en [`decisiones.md`](decisiones.md), el diseño en
[`arquitectura.md`](arquitectura.md), el orden en [`plan-implementacion.md`](plan-implementacion.md),
la prueba en curso en [`prueba-canva.md`](prueba-canva.md) y lo aprendido de las piezas que
marketing ya publica en [`referencias-reales.md`](referencias-reales.md).

**Revisión con piezas reales (2026-11-09):** se compararon los plans con la carpeta de Drive
«Estrategia de redes sociales». Ya se corrigieron los fondos (`#000033` y el degradado claro),
los pesos (se agregó Montserrat Light), los carruseles (flecha en vez de «2/7»), el
tratamiento de fotos, el logo por formato y la fuente obligatoria en las cifras, y se
agregaron dos formatos. Después se decidieron las seis preguntas que abrió la revisión:
catálogo v1 con las series reales, entrega para Canva **o Figma** según pida la persona
(Claude pregunta si no lo dice), mínimos de 28 y 24 px, sin emojis, sin dominio ni usuario
en el pie y recortes en Canva (`referencias-reales.md`). Para la fase 3 hace falta la
carpeta de Drive descomprimida en `plantillas/` (no se versiona).

## Retomar en otra máquina

```bash
gh auth login                                    # solo para hacer push; clonar no lo necesita
git clone https://github.com/sebastianguevara23/neo-sns-skill.git
cd neo-sns-skill
git switch fase-1                                # el trabajo en curso no está en main
```

Herramientas:

- **`uv`**: corre los scripts y trae Python y las librerías solo. Mac y Linux:
  `curl -LsSf https://astral.sh/uv/install.sh | sh`. Windows (PowerShell):
  `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`.
- **Node 18+**: solo para instalar la skill con `npx skills add`.
- **Clon de `neo-design-skill` en la carpeta vecina** (`../neo-design-skill`): solo para
  `tools/sincronizar-marca.py`. Las fuentes ya están en el repo; `tools/preparar-fuentes.py`
  no hace falta salvo que se quiera otra versión de Montserrat.

Comprobación rápida:

```bash
uv run skills/neo-redes/scripts/redes.py entorno   # debe terminar en «Listo para generar piezas»
uv run tests/prueba-canva/generar.py              # regenera los PDF de prueba
python3 tools/empaquetar-zip.py                   # arma dist/neo-redes-0.1.0.zip para Claude.ai
```

## Pendientes

### Fase 1 (bloquea la fase 2)

Detalle paso a paso en [`prueba-canva.md`](prueba-canva.md).

Dibujo directo (versión 0.2.0):

- [ ] **Prueba con una persona** en Claude Code, con Canva conectado (sección 4).
- [ ] **Montserrat en Canva:** probar si `replace_text` conserva la fuente en cajas de
      muestra del «Lienzo neo-redes».
- [ ] **Figma:** conseguir un puesto Full y probar `references/figma.md` (degradado, luces,
      pesos de Montserrat, logo SVG).
- [ ] **Decidir** el enfoque con los resultados y reescribir `decisiones.md`,
      `arquitectura.md` y `plan-implementacion.md`.

En pausa mientras se prueba el dibujo directo (enfoque de PDF):

- [ ] **Importar en Canva Pro** los 6 PDF de `tests/prueba-canva/salida/` (están en el repo;
      no hace falta regenerarlos) y completar la tabla de 18 puntos, con capturas en
      `tests/prueba-canva/capturas/`. Necesita una cuenta de Canva Pro de marketing.
- [ ] **Importar en Figma** los mismos 6 PDF con el plugin pdf.to.design (Figma solo no los
      deja editables) y completar su tabla. Si el texto no llega editable, agregar la
      variante D (SVG con texto vivo) a `generar.py` y probarla.
- [ ] **Claude.ai:** subir `dist/neo-redes-0.1.0.zip` y pegar el resultado de
      `python3 scripts/redes.py entorno --json`, antes y después del `pip install`.
- [ ] **Mac y Windows, con una persona en Claude Code:** instalar la skill con `npx` desde la
      rama `fase-1` y correr `entorno` en una máquina sin Python (guía en `prueba-canva.md`,
      sección 4). La instalación desde la rama ya se probó en Linux.
- [ ] **Decidir** el renderizador y el formato para Figma con el criterio de
      `prueba-canva.md`, y luego:
  - actualizar `arquitectura.md` §5.3 y §8;
  - dejar en `redes.py` solo las dependencias de la opción elegida;
  - marcar la fase 1 en `plan-implementacion.md`, anotarla en `CHANGELOG.md` y fusionar
    `fase-1` en `main`.

### Se puede adelantar sin esperar a Canva y Figma (fase 2)

Esto no depende de qué renderizador gane, porque la escena es independiente del PDF:

- `catalogo/formatos.json` con los 12 formatos, zonas seguras y mínimos de texto.
- Esquema de plantilla y su cargador.
- Composición: retícula, márgenes, zonas seguras, decoraciones y logo.
- Medición y corte de texto con las métricas de Montserrat (fontTools).
- Validador sobre la escena.
- `tools/medir-referencias.py` (es de la fase 3, pero tampoco depende de Canva).

Lo que sí espera el resultado: el renderizador, el formato para Figma, la holgura de las
cajas de texto (depende de cuánto recomponen Canva y Figma) y la forma de los espacios de
foto.

### Decisiones abiertas (no bloquean)

- Plan de Claude de NEO: Team o Enterprise. La sincronización automática funciona en ambos.
- A quién se deja la skill disponible y a quién instalada por defecto (fase 7).
- Archivos fuente de las piezas reales y del Brandbook, en Figma o Canva (los tiene
  marketing).
- Persona con Windows para las pruebas de las fases 1 y 6.

### Decisiones de la revisión de piezas reales (tomadas el 2026-11-09)

Detalle en [`referencias-reales.md`](referencias-reales.md).

- [x] **Catálogo v1:** las series reales (bienvenida individual y grupal, story de ingreso,
      día a día, Tech Update, cita, portada de reel y de destacado).
- [x] **Destino:** Canva o Figma, el que pida la persona; si no lo dice, Claude pregunta.
- [x] **Tamaño mínimo de texto:** 28 px para cuerpo y 24 px para secundarios.
- [x] **Emojis:** ninguno, tampoco en piezas de cultura.
- [x] **Pie de las piezas:** ni dominio ni usuario.
- [x] **Recortes de personas:** en Canva, con «Quitar fondo».

## Notas para no redescubrir

- **`git push` falla con «Authentication failed»:** la cuenta activa de `gh` no tiene permiso
  de escritura en el repo. Se cambia con `gh auth switch` o anteponiendo
  `GH_TOKEN=$(gh auth token --user <cuenta>)` al comando.
- **`uv` eligió Python 3.13** aunque el sistema tenía 3.14; ambas versiones tienen las ruedas
  de todas las librerías.
- **skia-python 144** en Linux imprime avisos de Fontconfig sobre
  `49-sansserif.conf`. Vienen de la configuración del sistema y no afectan el resultado.
- **ReportLab** no aplica interletraje (kerning). Para que no declare Helvetica sin incrustar
  hay que crear el lienzo con `initialFontName` y cambiar
  `reportlab.graphics.shapes.STATE_DEFAULTS["fontName"]` antes de dibujar SVG con svglib.
- **skia-python:** `FontCollection` solo tiene `setDefaultFontManager` (no
  `setAssetFontManager` ni `enableFontFallback`), y `SVGDOM` no conoce el tamaño de los logos
  porque solo traen `viewBox`: hay que leerlo del archivo.
- **Ambas librerías recortan la fuente** a los caracteres usados: no se puede incrustar
  completa.
- **Fuentes:** la cursiva variable de Google Fonts genera nombres internos incorrectos al
  instanciarla (`MontserratItalic-Italic`); `tools/preparar-fuentes.py` los reescribe a mano.
