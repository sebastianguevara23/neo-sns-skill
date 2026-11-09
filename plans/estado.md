# Estado y pendientes

Dónde quedó el trabajo y cómo retomarlo en otra máquina. Se actualiza al cerrar cada sesión.
Última actualización: 2026-11-09.

## Dónde estamos

| Fase | Estado | Dónde |
|---|---|---|
| 0. Base del repo | Cerrada | `main` (versión 0.1.0) |
| 1. Prueba de importación en Canva y Figma, y de entornos | **En curso**: falta la parte manual | Rama **`fase-1`** |
| 2 en adelante | Sin empezar | — |

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
gh auth login                                    # con una cuenta que tenga acceso al repo privado
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

- [ ] **Importar en Canva Pro** los 6 PDF de `tests/prueba-canva/salida/` (están en el repo;
      no hace falta regenerarlos) y completar la tabla de 18 puntos, con capturas en
      `tests/prueba-canva/capturas/`. Necesita una cuenta de Canva Pro de marketing.
- [ ] **Importar en Figma** los mismos 6 PDF con el plugin pdf.to.design (Figma solo no los
      deja editables) y completar su tabla. Si el texto no llega editable, agregar la
      variante D (SVG con texto vivo) a `generar.py` y probarla.
- [ ] **Claude.ai:** subir `dist/neo-redes-0.1.0.zip` y pegar el resultado de
      `python3 scripts/redes.py entorno --json`, antes y después del `pip install`.
- [ ] **Mac y Windows:** instalar `uv` en una máquina sin Python y correr `entorno`. Anotar si
      pidió permisos de administrador y cuánto tardó la primera vez.
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

- **Cuentas de GitHub en la máquina original:** la cuenta activa de `gh` era **MrPepePollo**,
  que no tiene acceso al repo privado; por eso `npx skills add` y `git push` fallan con
  «Authentication failed». Opciones: `gh auth switch --user sebastianguevara23`, dar acceso a
  MrPepePollo, o anteponer `GH_TOKEN=$(gh auth token --user sebastianguevara23)` al comando.
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
