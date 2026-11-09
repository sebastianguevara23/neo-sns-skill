# neo-redes

**Piezas de redes y comunicación interna con la marca NEO.** Una skill para Claude que
convierte un pedido en lenguaje simple («post de LinkedIn: buscamos ingenieros de IA,
híbrido») en opciones con la línea gráfica NEO, y entrega la elegida en **PDF para editar en
Canva** y en PNG.

- **Formatos:** posts, carruseles y stories de Instagram; posts y carruseles de LinkedIn;
  banners de correo, fondos para Teams o Zoom y pantallas.
- **Marca:** la de neo-design (azul #2D5BFF, Montserrat), con el sistema de redes del
  Brandbook.
- **Editable:** textos vivos, formas y colores editables y espacios marcados para las fotos.

> **Estado: en construcción (0.1.0).** Dónde quedó el trabajo, qué falta y cómo retomarlo
> en otra máquina: [`plans/estado.md`](plans/estado.md). El plan completo está en
> [`plans/`](plans/): [decisiones](plans/decisiones.md), [arquitectura](plans/arquitectura.md)
> y [plan de implementación](plans/plan-implementacion.md).

## Instalación (mientras se construye)

El repo es privado: necesitas acceso de lectura a `sebastianguevara23/neo-sns-skill`, git
autenticado con GitHub (`gh auth login` alcanza) y Node 18 o superior.

```bash
npx skills add sebastianguevara23/neo-sns-skill -g --all   # para tu usuario, en todos tus agentes
npx skills update                                           # trae la última versión
npx skills remove neo-redes                                 # la quita
```

Cuando la v1 esté lista, la distribuye el propietario de la organización en Claude desde
este repo, y llega sola (y actualizada) a Claude.ai, Cowork y Claude Code.

## Qué hay adentro

```
.claude-plugin/              plugin y marketplace (versión)
skills/neo-redes/
├── SKILL.md                 punto de entrada de la skill
├── tokens/neo-tokens.json   colores y tipografía, copiados de neo-design (no editar)
├── tokens/ORIGEN.json       de qué versión de neo-design vienen
├── assets/logo/             «NEO | 25 años», NEO e isotipo, en navy y blanco
├── assets/fonts/            Montserrat TTF estática, 400 a 900 con cursivas (OFL)
└── scripts/redes.py         punto de entrada (por ahora, `entorno`)
tools/                       mantenimiento: marca, fuentes y ZIP de prueba para Claude.ai
tests/prueba-canva/          generador de la prueba de importación en Canva (fase 1)
plans/                       decisiones, arquitectura, plan y resultados de la prueba
```

## Mantener la skill

- **Marca:** los tokens y logos se copian **solo** desde neo-design, nunca se editan aquí.
  ```bash
  python3 tools/sincronizar-marca.py            # copia desde ../neo-design-skill
  python3 tools/sincronizar-marca.py --revisar  # avisa si neo-design cambió
  ```
- **Fuentes:** las TTF salen de la Montserrat variable de Google Fonts, porque los
  generadores de PDF no aceptan fuentes variables y neo-design solo trae woff2.
  ```bash
  uv run tools/preparar-fuentes.py
  ```
- **Versiones:** cada cambio sube la versión en `.claude-plugin/plugin.json` y
  `.claude-plugin/marketplace.json` y se anota en [`CHANGELOG.md`](CHANGELOG.md).
- **Ramas:** una rama por fase y fusión a `main` al cerrarla. `main` es lo que se instala,
  así que siempre tiene que funcionar.

## Licencias

Montserrat se distribuye bajo la SIL Open Font License 1.1
([`OFL.txt`](skills/neo-redes/assets/fonts/OFL.txt)).
