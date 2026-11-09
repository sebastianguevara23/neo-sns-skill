---
name: neo-redes
description: Piezas de redes sociales y comunicación interna con la marca NEO Consulting, dibujadas directo en Canva o en Figma con sus conectores. Úsala cuando se pida un post, carrusel o story para Instagram o LinkedIn, una bienvenida de nuevo ingreso, un «día a día» de un colaborador, un Tech Update, una cita, una portada de reel o de destacado, o «una pieza con la marca NEO». No es para software (eso es neo-design) ni para presentaciones.
user-invocable: true
---

# neo-redes: piezas de redes y comunicación interna NEO

> **Versión de prueba (0.2.0).** Claude dibuja la pieza directo en Canva o en Figma con
> los conectores oficiales, sin plantillas, sin archivos intermedios y sin instalar nada.
> Es una prueba: si algo sale mal, dilo con claridad y anota qué pasó.

## Antes de dibujar

1. **Arma la ficha.** Lo único obligatorio es el **formato**, el **mensaje** y el
   **destino** (Canva o Figma). Si el pedido no dice el destino, pregúntalo; nunca lo
   supongas.
2. **Pregunta una sola vez** por lo que falte del contenido. **Nunca inventes** cifras,
   fechas, nombres, cargos, citas, fuentes ni enlaces. Una cifra externa siempre lleva
   «Fuente: …» y la fuente la da la persona.
3. **Revisa el conector del destino.** Canva: herramientas `copy-design`, `edit-design`,
   `create-upload-url`. Figma: `use_figma`. Si aparecen como herramientas diferidas,
   cárgalas con ToolSearch. Si no están, explica cómo conectarlo (abajo) y detente.
4. **Propón hasta 3 opciones en palabras**, una línea cada una (composición y si es clara u
   oscura; por ejemplo «clara, titular arriba y palabra gigante al pie»). Dibuja solo la
   que elija la persona; si quiere ver otra, la dibujas después. Así no se gasta de más.

## Dibujar

- **Canva:** sigue [references/canva.md](references/canva.md).
- **Figma:** sigue [references/figma.md](references/figma.md).

Las reglas de marca están en [references/marca.md](references/marca.md) y la anatomía de
cada serie (qué lleva, dónde y a qué tamaño) en [references/series.md](references/series.md).
Léelas antes de la primera pieza de la conversación.

## Antes de entregar

Revisa la vista previa contra esta lista y corrige lo que falle:

- Textos de al menos **28 px** (cuerpo) y **24 px** (secundarios) en lienzos de 1080 px.
- Nada se sale del margen ni de la zona segura del formato; nada se encima.
- Logo según el formato (stories sin logo); sin emojis; sin dominio ni usuario al pie.
- Colores solo de la paleta; el azul suave `#7E99FE` nunca como texto sobre blanco.
- Ningún dato inventado.

Entrega con: el enlace al diseño, el **texto alternativo** de la pieza, lo que la persona
tiene que terminar a mano (fotos, recortes y, en Canva, la tipografía; ver la guía) y
cualquier cosa que no salió como se esperaba.

## Conectar Canva o Figma

- **Claude Code (terminal):** `claude mcp add --transport http canva https://mcp.canva.com/mcp`
  o `claude mcp add --transport http figma https://mcp.figma.com/mcp`; luego `/mcp` para
  iniciar sesión.
- **App de escritorio o Claude.ai:** activar el conector de Canva o de Figma en
  Conectores e iniciar sesión.
- **Figma** solo deja dibujar con un **puesto Full** en el plan donde está el archivo. Con
  otro puesto, Claude puede leer pero no escribir: dilo y ofrece Canva.

## Qué hay en esta carpeta

- `references/`: marca, series y cómo dibujar en Canva y en Figma.
- `assets/logo/`: «NEO | 25 años», NEO e isotipo, en navy y blanco (SVG).
- `assets/fondos/`: degradado claro y navy con luces en PNG, para Canva (en Figma se dibujan).
- `tokens/neo-tokens.json`: colores y tipografía de neo-design (no se editan aquí).
- `assets/fonts/` y `scripts/redes.py`: del motor de PDF anterior. Esta versión no los usa.
