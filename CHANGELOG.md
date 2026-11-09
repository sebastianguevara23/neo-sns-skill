# Cambios

## Sin publicar

Fase 1, en curso: prueba de importación en Canva.

- `scripts/redes.py entorno`: revisa Python, librerías, fuentes y que se pueda generar y
  rasterizar un PDF; con `--json` para Claude.ai.
- `tests/prueba-canva/generar.py`: pieza y carrusel de prueba en tres variantes de PDF
  (ReportLab por párrafo, ReportLab por línea y skia-python).
- `tools/empaquetar-zip.py`: ZIP de la skill para probarla en Claude.ai.
- `plans/prueba-canva.md`: guía de la prueba y tabla de resultados.

## 0.1.0 — 2026-11-09

Fase 0: base del repo.

- Plugin y marketplace (`.claude-plugin/`) y `SKILL.md` inicial, marcado como en
  construcción para que Claude no improvise piezas todavía.
- Marca copiada de neo-design 1.2.0 (tokens y logos) con `tools/sincronizar-marca.py`.
- Montserrat 9.000 en TTF estática, de 400 a 900 con cursivas, generada con
  `tools/preparar-fuentes.py` desde Google Fonts.
- Plan del proyecto en `plans/`: decisiones, arquitectura e implementación.
