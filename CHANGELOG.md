# Cambios

## 0.2.0 (2026-11-09): versión de prueba con dibujo directo

- La skill dibuja la pieza directo en Canva o en Figma con los conectores oficiales, sin
  plantillas, sin archivos intermedios y sin Python ni `uv`.
- `references/`: marca, anatomía de las series y guías para dibujar en Canva (probada) y en
  Figma (según la documentación; falta probar con puesto Full).
- `assets/fondos/`: degradado claro y navy con luces en PNG, porque el conector de Canva
  solo pinta colores planos. Se regeneran con `tools/generar-fondos.py`.
- Repo público: se instala sin cuenta de GitHub.
- `scripts/redes.py` y `assets/fonts/` quedan del enfoque de PDF; esta versión no los usa.

## Sin publicar (enfoque de PDF, en pausa)

Fase 1, en curso: prueba de importación en Canva.

- `scripts/redes.py entorno`: revisa Python, librerías, fuentes y que se pueda generar y
  rasterizar un PDF; con `--json` para Claude.ai.
- `tests/prueba-canva/generar.py`: pieza y carrusel de prueba en tres variantes de PDF
  (ReportLab por párrafo, ReportLab por línea y skia-python).
- `tools/empaquetar-zip.py`: ZIP de la skill para probarla en Claude.ai.
- `plans/prueba-canva.md`: guía de la prueba y tabla de resultados.

Revisión con las piezas que marketing ya publica (carpeta de Drive «Estrategia de redes
sociales»):

- `plans/referencias-reales.md`: inventario, anatomía de cada serie, colores y tamaños
  medidos, correcciones y las seis decisiones que se tomaron después.
- Plans corregidos: fondo oscuro `#000033` y claro en degradado `#E8F0FE` → `#FFFFFF`,
  carruseles con botón de flecha en vez de numeración, degradado de foto como tratamiento
  principal, logo según el formato, cifras con fuente obligatoria, portadas de reel y de
  destacado, y `tools/medir-referencias.py` en lugar de `medir-brandbook.py`.
- Montserrat Light y Light Italic (300), que pide el Brandbook para citas.
- `plantillas/` fuera de git: más de 300 MB y fotos personales de colaboradores.

Decisiones tomadas después de la revisión:

- Catálogo v1 con las series reales (bienvenida individual y grupal, story de nuevo
  ingreso, día a día, Tech Update, cita, portada de reel y de destacado); las plantillas del
  Brandbook pasan a la v1.1.
- Entrega para Canva o Figma, según pida la persona: el destino entra en la ficha como
  dato obligatorio y, si el pedido no lo dice, Claude lo pregunta. La prueba de la fase 1
  suma Figma y decide si basta el PDF o hace falta un SVG con texto vivo.
- Mínimos de texto de 28 px para cuerpo y 24 px para secundarios.
- Sin emojis, sin dominio ni usuario de redes en las piezas, y recortes de personas en
  Canva.

## 0.1.0 — 2026-11-09

Fase 0: base del repo.

- Plugin y marketplace (`.claude-plugin/`) y `SKILL.md` inicial, marcado como en
  construcción para que Claude no improvise piezas todavía.
- Marca copiada de neo-design 1.2.0 (tokens y logos) con `tools/sincronizar-marca.py`.
- Montserrat 9.000 en TTF estática, de 400 a 900 con cursivas, generada con
  `tools/preparar-fuentes.py` desde Google Fonts.
- Plan del proyecto en `plans/`: decisiones, arquitectura e implementación.
