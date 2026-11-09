# Dibujar en Canva con el conector

Probado el 2026-11-09 con el conector oficial (`mcp.canva.com`). Lo marcado «a verificar»
todavía no se probó.

## Qué se puede y qué no

| Se puede | No se puede |
|---|---|
| Copiar un diseño o algunas de sus páginas (`copy-design`) | Crear un diseño en blanco (solo copiando uno) |
| Agregar páginas del tamaño exacto, con color de fondo (`add_page`) | Elegir la tipografía: los textos nuevos salen en la letra por defecto de Canva |
| Agregar textos (`add_text`) y darles tamaño, color, negrita, cursiva, alineación e interlineado (`format_text`) | Pesos intermedios (Light, SemiBold, ExtraBold, Black): solo normal o negrita |
| Formas con trazo SVG, color, borde y esquinas redondas (`insert_shape`) | Degradados y desenfoques: solo colores planos (por eso los fondos van como PNG) |
| Subir archivos de la computadora (`create-upload-url`) e insertarlos (`insert_fill`) | Dos colores dentro de una misma caja de texto (van en cajas separadas) |
| Mover, cambiar tamaño, ordenar capas, opacidad, borrar | Duplicar un elemento |

## Una sola vez por persona: el lienzo

Canva no deja crear un diseño en blanco desde el conector, así que se trabaja copiando un
**lienzo**.

1. Busca con `search-designs` un diseño llamado **«Lienzo neo-redes»**.
2. Si no existe, pide a la persona que cree en Canva un diseño vacío de **1080 × 1350** con
   ese nombre (Crear un diseño → Tamaño personalizado). Es el único paso a mano.
3. Ábrelo (`read-design` con `open_transaction`) y agrega dos páginas con `add_page`:
   1080 × 1920 (título «Story 9:16») y 1080 × 1080 («Cuadrado 1:1»). Muestra la vista previa
   y guarda con `commit` cuando la persona diga que sí.

**Opcional, para que el texto salga en Montserrat (a verificar):** si la persona pone en cada
página del lienzo algunas cajas de texto de muestra ya en Montserrat (por ejemplo «Black»,
«ExtraBold», «Bold», «Regular», «Italic», «Light», dos de cada una), usa esas cajas con
`replace_text` en lugar de `add_text`, muévelas y cámbiales tamaño y color, y borra las que
sobren. Comprueba en el documento que devuelve `edit-design` que el `fontRef` no cambió.

## Cada pieza

1. **Copia la página del formato:** `copy-design` del lienzo con `page_numbers` de la
   página cuyo tamaño coincide (léelo de `page_metadata`, no lo supongas). La copia es la
   pieza; el lienzo no se toca. Para carruseles, agrega en la copia una página por lámina
   con `add_page` del mismo tamaño.
2. **Ponle nombre:** `update_title` con «[Serie] · [persona o tema] · [formato]».
3. **Sube lo que vaya a usar.** Por cada archivo: `create-upload-url` y luego, desde la
   terminal,

   ```bash
   curl -sS -X POST -H "Content-Type: application/octet-stream" --data-binary @"<ruta>" "<upload_url>"
   ```

   En PowerShell, escribe `curl.exe` (ahí `curl` es otro comando). La respuesta trae
   `mediaId`, que se usa como `asset_id`. Cada URL sirve una sola vez.
   Rutas dentro de la skill: `assets/fondos/claro-<ancho>x<alto>.png`,
   `assets/fondos/navy-luces-<ancho>x<alto>.png` y `assets/logo/*.svg` (el SVG funciona).
   Para el navy plano no hace falta subir nada: usa el color de fondo de la página.
4. **Dibuja en este orden**, agrupando operaciones en pocas llamadas a `edit-design`:
   1. Fondo: `insert_fill` en 0, 0 con el tamaño completo de la página.
   2. Formas: píldoras, líneas, círculos, tarjetas y espacios de foto (`insert_shape`).
   3. Logo: `insert_fill` con **ancho y alto en la proporción del SVG**; si das solo uno,
      Canva lo recorta.
   4. Textos: `add_text` con `left`, `top` y `width` (salen a 16 px).
   5. En la llamada siguiente, `format_text` de cada texto y, con las alturas que devuelve el
      documento, `position_element` para apilarlos.
5. **Revisa la miniatura** que devuelve cada `edit-design` y el documento (posiciones y
   alturas) contra la lista de «Antes de entregar» de SKILL.md. Corrige con operaciones
   puntuales; no redibujes todo.
6. **Muestra la vista previa y pide permiso para guardar.** Guarda con `commit` solo con el
   sí de la persona. Si dice que no, `cancel`.

## Recetas de formas

`insert_shape` usa un trazo SVG con `view_box_width` y `view_box_height` iguales al tamaño.
Solo acepta los comandos M, L, H, V, C, S, A y Z.

- **Píldora o tarjeta:** `M0 0 H<w> V<h> H0 Z` con `corner_rounding` (la mitad del alto para
  píldora). Borde con `stroke_color` y `stroke_weight`; relleno con `color`.
- **Círculo de diámetro d:** `M0 <r> A<r> <r> 0 1 0 <d> <r> A<r> <r> 0 1 0 0 <r> Z`.
- **Línea:** un rectángulo de 4 a 6 px de alto.
- **Flecha del carrusel (a verificar):** un círculo azul de 90 px y encima un trazo
  `M5 12 H19 M12 5 L19 12 L12 19` en una caja de 24 × 24 escalada a 40 px, con
  `stroke_color` blanco y `stroke_weight` 2.5. Si Canva rellena el trazo, usa un texto «→»
  blanco Bold 44 px centrado en el círculo.

## Al entregar

Dile a la persona qué falta terminar a mano y cómo:

- **Tipografía:** seleccionar todos los textos y elegir Montserrat; después, los que deben ir
  en otro peso (dale la lista: «nombre → Black», «kicker → ExtraBold», «subtítulo → Light»).
  Si se usaron las cajas de muestra del lienzo, esto no hace falta.
- **Fotos:** arrastrarlas sobre los espacios marcados; para recortes, «Quitar fondo».
- El enlace al diseño (`edit_url`) y el texto alternativo.

## Gasto

Cada `edit-design` devuelve el documento completo de la página y una miniatura. Agrupa
operaciones (una llamada para fondo, formas y textos; otra para formato y posiciones) y no
pidas lecturas que no necesitas.
