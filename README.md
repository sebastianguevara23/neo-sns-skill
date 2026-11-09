# neo-redes

**Piezas de redes y comunicación interna con la marca NEO.** Una skill para Claude que
convierte un pedido en lenguaje simple («story de Tech Update sobre phishing, para Canva»)
en una pieza con la línea gráfica NEO, **dibujada directo en Canva o en Figma** con sus
conectores oficiales. No hay que subir ni importar nada. Si no dices la herramienta, Claude
te pregunta.

- **Formatos:** posts, carruseles y stories de Instagram y LinkedIn; portadas de reel y de
  destacado.
- **Series:** las que marketing ya publica (bienvenidas, story de ingreso, día a día, Tech
  Update, cita y portadas).
- **Marca:** la de neo-design (azul #2D5BFF, navy #000033, Montserrat), con las piezas reales
  de marketing y el Brandbook como referencia.
- **Editable:** el resultado es un diseño normal de Canva o de Figma.

> **Estado: versión de prueba (0.2.0).** Se está probando el dibujo directo con los
> conectores. Dónde quedó el trabajo y cómo retomarlo: [`plans/estado.md`](plans/estado.md).
> La guía para quien prueba: [`plans/prueba-canva.md`](plans/prueba-canva.md), sección 4.

## Instalación

El repo es público: para instalar solo hace falta Node 18 o superior (no se necesita cuenta
de GitHub).

```bash
npx skills add sebastianguevara23/neo-sns-skill -g --all   # para tu usuario, en todos tus agentes
npx skills update                                           # trae la última versión
npx skills remove neo-redes                                 # la quita
```

Eso instala `main`. Para probar la rama en curso (`fase-1`), se usa la URL con la rama:

```bash
npx skills add https://github.com/sebastianguevara23/neo-sns-skill/tree/fase-1 -g --skill neo-redes --agent claude-code -y
```

Para traer cambios nuevos de la rama, se repite el mismo comando.

## Conectar Canva o Figma

La skill dibuja con los conectores oficiales; hace falta conectar al menos uno:

```bash
claude mcp add --transport http canva https://mcp.canva.com/mcp
```

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

Después, en Claude Code, `/mcp` para iniciar sesión en cada uno. En la app de escritorio y en
Claude.ai se activan desde Conectores. Figma solo deja dibujar con un **puesto Full**.

## Qué hay adentro

```
.claude-plugin/              plugin y marketplace (versión)
skills/neo-redes/
├── SKILL.md                 punto de entrada de la skill
├── references/              marca, series y cómo dibujar en Canva y en Figma
├── assets/logo/             «NEO | 25 años», NEO e isotipo, en navy y blanco (SVG)
├── assets/fondos/           degradado claro y navy con luces (PNG, para Canva)
├── tokens/neo-tokens.json   colores y tipografía, copiados de neo-design (no editar)
├── assets/fonts/            Montserrat TTF (OFL), del motor de PDF anterior
└── scripts/redes.py         del motor de PDF anterior; la versión 0.2.0 no lo usa
tools/                       mantenimiento: marca, fuentes, fondos y ZIP para Claude.ai
tests/prueba-canva/          prueba de importación de PDF (enfoque anterior)
plans/                       decisiones, arquitectura, plan y pruebas
```

## Mantener la skill

- **Marca:** los tokens y logos se copian **solo** desde neo-design, nunca se editan aquí.
  ```bash
  python3 tools/sincronizar-marca.py            # copia desde ../neo-design-skill
  python3 tools/sincronizar-marca.py --revisar  # avisa si neo-design cambió
  ```
- **Fondos para Canva:** `uv run tools/generar-fondos.py` regenera los PNG de
  `assets/fondos/`.
- **Versiones:** cada cambio sube la versión en `.claude-plugin/plugin.json` y
  `.claude-plugin/marketplace.json` y se anota en [`CHANGELOG.md`](CHANGELOG.md).
- **Ramas:** una rama por fase y fusión a `main` al cerrarla. `main` es lo que se instala,
  así que siempre tiene que funcionar.

## Licencias

Montserrat se distribuye bajo la SIL Open Font License 1.1
([`OFL.txt`](skills/neo-redes/assets/fonts/OFL.txt)).
