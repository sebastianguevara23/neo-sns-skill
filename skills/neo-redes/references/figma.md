# Dibujar en Figma con el conector

El conector de Figma (`mcp.figma.com`) ejecuta código del Plugin API con `use_figma`, así que
se puede dibujar todo: Montserrat en todos sus pesos, degradados, desenfoques y dos colores
en un mismo texto. **Todavía no se probó escribiendo** (la cuenta de prueba no tenía puesto
Full): lo que sigue sale de la documentación de Figma. Anota lo que falle.

## Requisitos

- **Puesto Full** en el plan donde vive el archivo. Si `use_figma` responde «you'll need a
  Full seat», dilo, explica que lo asigna quien administra el plan de Figma y ofrece Canva.
  Para leer alcanza cualquier puesto.
- **Dónde dibujar:** el enlace del archivo y de la page que diga la persona
  (`figma.com/design/<fileKey>/...?node-id=<page>`). Si no tiene uno, crea un archivo con
  `create_new_file`.
- **Antes del primer `use_figma` de la conversación:** `create_session` con el `fileKey`, y
  leer la guía de Figma con `get_figma_skill` (`skill://figma/figma-use/SKILL.md`). Figma la
  exige; pasa `sessionId` y `skillNames: "resource:figma-use"` en cada llamada.

## Cada pieza: una llamada a `use_figma`

1. Cambia a la page con `await figma.setCurrentPageAsync(page)` (una vez por llamada) y
   busca espacio libre a la derecha de lo que ya haya.
2. Crea un **frame** del tamaño del formato con nombre «[Serie] · [persona o tema] ·
   [formato]». Para carruseles, un frame por lámina, uno al lado del otro con 80 px de
   separación.
3. **Fondo:**
   - Claro: relleno `GRADIENT_LINEAR` de `#E8F0FE` (arriba) a `#FFFFFF` (abajo), con
     `gradientTransform: [[0, 1, 0], [-1, 0, 1]]` para que vaya de arriba hacia abajo.
     Confírmalo en la captura.
   - Navy con luces: relleno `#000033` y dos elipses `#2D5BFF` (unas 650 px, opacidad 0.5 y
     0.38) en las esquinas superior derecha e inferior izquierda, con efecto
     `LAYER_BLUR` de unos 250 px. El frame recorta lo que sobra (`clipsContent = true`).
4. **Textos:** carga cada estilo antes de usarlo (`await figma.loadFontAsync({ family:
   "Montserrat", style })`). Los nombres exactos de estilo se confirman una vez con
   `figma.listAvailableFontsAsync()` (pueden ser «SemiBold» o «Semi Bold»). Para dos colores
   en un titular, un solo texto con `setRangeFills`. Textos que envuelven:
   `textAutoResize = "HEIGHT"` y ancho fijo con `resize()`.
5. **Logo:** lee el SVG de `assets/logo/` y pásalo como texto a `figma.createNodeFromSvg()`;
   ajusta el ancho y calcula el alto con la proporción ([marca.md](marca.md)).
6. **Formas:** rectángulos con `cornerRadius` para píldoras y tarjetas, elipses para círculos.
   Íconos y flecha del carrusel con `createNodeFromSvg` y el SVG de Lucide (`arrow-right`:
   `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF"
   stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path
   d="m12 5 7 7-7 7"/></svg>`).
7. **Espacios de foto:** rectángulo `#C5D5F7` llamado «Foto: [qué va]» con su texto de 24 px.
   No se generan imágenes.
8. Devuelve los IDs creados y una captura del frame (`await frame.screenshot()`).

Revisa la captura contra la lista de «Antes de entregar» de SKILL.md y corrige con una
llamada puntual. Entrega el enlace al frame (`...?node-id=<id del frame>`) y el texto
alternativo.

## Gasto

Leer la guía de Figma cuesta una vez por conversación. Después, cada pieza es una llamada
con el código completo de la pieza y una captura. Usa una sola llamada por pieza siempre que
sea seguro repetirla si falla.
