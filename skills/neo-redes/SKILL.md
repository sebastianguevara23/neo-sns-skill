---
name: neo-redes
description: Piezas de redes sociales y comunicación interna con la marca NEO Consulting. Úsala cuando se pida un post, carrusel o story para Instagram o LinkedIn, un banner de correo, un fondo para Teams o Zoom, una pieza para pantallas, un comunicado interno, o «una pieza con la marca NEO». Entrega PDF para editar en Canva y PNG. No es para software (eso es neo-design) ni para presentaciones.
user-invocable: true
---

# neo-redes — piezas de redes y comunicación interna NEO

> **Estado: en construcción (versión 0.1.0, fase 0).** Todavía no genera piezas: el motor,
> las plantillas y los scripts llegan en las fases siguientes (`plans/plan-implementacion.md`
> en el repo). Si alguien pide una pieza, dile que la skill aún no está lista y **no
> improvises una pieza a mano**: saldría fuera de la línea gráfica y sin el paquete
> editable para Canva.

## Qué hará

1. Leer el pedido y reducirlo a una ficha (formato y mensaje son lo único obligatorio).
2. Preguntar una sola vez si falta un dato de contenido. **Nunca inventar** cifras, fechas,
   nombres, citas ni enlaces.
3. Proponer 3 opciones (al menos una clara y una oscura) con las plantillas del Brandbook.
4. Entregar la elegida en PDF (para importar en Canva) y PNG, con su texto alternativo.

## Lo que ya está en esta carpeta

- `tokens/neo-tokens.json`: colores y tipografía, copiados de neo-design (no se editan a
  mano; los trae `tools/sincronizar-marca.py`). `tokens/ORIGEN.json` dice de qué versión.
- `assets/logo/`: lockup «NEO | 25 años», NEO e isotipo, en navy y blanco.
- `assets/fonts/`: Montserrat TTF estática (OFL), de 400 a 900 con sus cursivas.
