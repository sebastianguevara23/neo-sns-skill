---
name: neo-redes
description: Piezas de redes sociales y comunicación interna con la marca NEO Consulting. Úsala cuando se pida un post, carrusel o story para Instagram o LinkedIn, una bienvenida de nuevo ingreso, un «día a día» de un colaborador, un Tech Update, una cita, una portada de reel o de destacado, un banner de correo, un fondo para Teams o Zoom, una pieza para pantallas, o «una pieza con la marca NEO». Entrega archivos para editar en Canva o Figma, y PNG. No es para software (eso es neo-design) ni para presentaciones.
user-invocable: true
---

# neo-redes — piezas de redes y comunicación interna NEO

> **Estado: en construcción (versión 0.1.0, fase 0).** Todavía no genera piezas: el motor,
> las plantillas y los scripts llegan en las fases siguientes (`plans/plan-implementacion.md`
> en el repo). Si alguien pide una pieza, dile que la skill aún no está lista y **no
> improvises una pieza a mano**: saldría fuera de la línea gráfica y sin el paquete
> editable para Canva.

## Qué hará

1. Leer el pedido y reducirlo a una ficha (formato, mensaje y destino son lo único
   obligatorio). Si el pedido no dice si la pieza se va a editar en Canva o en Figma,
   preguntarlo; nunca suponerlo.
2. Preguntar una sola vez si falta un dato de contenido. **Nunca inventar** cifras, fechas,
   nombres, citas ni enlaces.
3. Proponer 3 opciones (al menos una clara y una oscura) con las plantillas de NEO, basadas
   en las piezas que marketing ya publica y en el Brandbook.
4. Entregar la elegida con el archivo para la herramienta que pidió la persona (Canva o
   Figma, o las dos si lo pidió) y en PNG, con su texto alternativo. Sin emojis, sin
   dominio ni usuario de redes en las piezas.

## Lo que ya está en esta carpeta

- `tokens/neo-tokens.json`: colores y tipografía, copiados de neo-design (no se editan a
  mano; los trae `tools/sincronizar-marca.py`). `tokens/ORIGEN.json` dice de qué versión.
- `assets/logo/`: lockup «NEO | 25 años», NEO e isotipo, en navy y blanco.
- `assets/fonts/`: Montserrat TTF estática (OFL), de 300 a 900 con sus cursivas.
- `scripts/redes.py entorno`: revisa que este entorno pueda generar piezas (Python,
  librerías, fuentes y un PDF de prueba). En Claude Code se corre con
  `uv run <skill>/scripts/redes.py entorno`; en Claude.ai, con `python3` y, si falta algo,
  `pip install` de lo que indique. Agrega `--json` para el informe completo.
