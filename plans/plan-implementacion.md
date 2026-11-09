# Plan de implementación de neo-redes

Orden de trabajo para construir la v1. El contrato está en `decisiones.md` y el diseño
técnico en `arquitectura.md`. Las fases van en orden: cada una cierra con su criterio de
terminado antes de empezar la siguiente. Sin plazos prefijados.

**Forma de trabajo:** una rama por fase y fusión a `main` al cerrarla. `main` es lo que
instala `npx skills add` en la etapa 1 y lo que sincroniza la organización en la etapa 2,
así que siempre tiene que funcionar.

---

## Fase 0. Base del repo

**Objetivo:** el repo existe, se instala con `npx skills add` y trae la marca de neo-design.

- [x] `git init` local y `.gitignore`.
- [x] `plans/` con decisiones, arquitectura y este plan.
- [x] Crear el repo `sebastianguevara23/neo-sns-skill` y subir `main` (privado al inicio,
      público desde el 2026-11-09).
- [x] Base de la estructura de `arquitectura.md` §3, con `.claude-plugin/plugin.json` y
      `marketplace.json` (versión `0.1.0`) y un `SKILL.md` mínimo. Las demás carpetas se
      crean en la fase que les da contenido.
- [x] `tools/sincronizar-marca.py`: copia `neo-tokens.json` y los logos desde
      `../neo-design-skill` y escribe `tokens/ORIGEN.json` con la versión de origen
      (1.2.0). Con `--revisar` avisa si neo-design cambió.
- [x] Montserrat TTF estática con `OFL.txt`, generada por `tools/preparar-fuentes.py` desde
      la variable del repositorio oficial de Google Fonts (versión 9.000): de 300 a 900,
      cada peso con su cursiva (Light se agregó tras revisar las piezas reales).
- [x] `README.md` para quien mantiene la skill y `CHANGELOG.md`.

**Terminado cuando:** `npx skills add sebastianguevara23/neo-sns-skill -g --all` instala
`neo-redes` y Claude Code la reconoce.

---

## Fase 1. Prueba de importación en Canva y Figma, y de entornos

**Objetivo:** confirmar con archivos reales cómo llega cada elemento a Canva y a Figma, y en
qué entornos corren los scripts, antes de construir el motor. **Es la puerta del
proyecto.**

**Pieza de prueba:** una «cifra» 4:5 en oscuro, con kicker, cifra, titular, cuerpo de dos
líneas, logo, barra de acento, divisor degradado, luz difusa, una foto con duotono y un
espacio de foto vacío. Se escribe la escena a mano (todavía no hay motor), más un carrusel
de 3 láminas.

Tareas:

- [x] Generar variantes del PDF con `tests/prueba-canva/generar.py`:
  - A. ReportLab, un objeto de texto por párrafo.
  - B. ReportLab, un objeto por línea.
  - C. skia-python.
  - Ninguna de las dos librerías permite incrustar la fuente completa: ambas la recortan a
    los caracteres usados, así que esa comparación no se hace.
- [x] Revisar los PDF por dentro: fuentes, tabla Unicode y objetos de texto
      (`prueba-canva.md`).
- [ ] Importar cada variante en una cuenta de Canva Pro y registrar, elemento por
      elemento:
  - ¿El texto es editable? ¿Llega en un cuadro por párrafo o por línea?
  - ¿Reconoce Montserrat y sus pesos?
  - ¿Se mantienen transparencias y degradados?
  - ¿Logo e íconos llegan como vectores con color editable?
  - ¿Cuál es la forma más cómoda de reemplazar el espacio de foto: forma, imagen neutra
    u otra?
  - ¿Cuánto se mueven los saltos de línea al recomponer?
- [ ] Importar el carrusel: ¿Canva crea un diseño de varias páginas? Subir el mismo PDF
      como documento a LinkedIn (sin publicar) para ver la vista previa.
- [ ] Importar los mismos PDF en Figma con el plugin pdf.to.design (la importación nativa
      no deja capas editables) y registrar lo mismo. Si el texto no llega editable, agregar
      a `generar.py` una variante **D** en SVG con texto vivo (un archivo por lámina) y
      probarla.
- [x] `scripts/redes.py entorno` y `tools/empaquetar-zip.py` para la prueba en Claude.ai.
- [ ] Entorno de Claude.ai: subir el ZIP y registrar qué librerías trae, si permite
      `pip install` y si puede rasterizar el PDF.
- [ ] Entorno local: instalar `uv` y correr el script en Mac y en Windows, partiendo de una
      máquina sin Python. (Linux ya pasó.)
- [x] `plans/prueba-canva.md` con la guía paso a paso y la tabla de resultados.
- [ ] Completar los resultados y las capturas, decidir, y actualizar `arquitectura.md` §5.3
      (renderizador y formato para Figma elegidos) y §8 (cómo llega cada elemento).

**Terminado cuando:** hay una variante de PDF que llega a Canva con texto editable en
Montserrat y formas editables, hay un archivo (el mismo PDF o un SVG) que llega igual a
Figma, el renderizador está elegido y los scripts corren en Claude.ai, Mac y Windows.

**Si falla:** si ninguna variante deja el texto editable en Canva, se detiene el proyecto
y se replantea la salida con el equipo antes de seguir. No se construye el motor sobre un
supuesto falso. Si solo falla Figma, se sigue con Canva y se busca otra salida para Figma
(`arquitectura.md` §12) antes de la fase 4.

---

## Fase 2. Motor con una plantilla

**Objetivo:** el flujo completo de pieza a PDF y PNG, con validación, usando una sola
plantilla («cita») en todas las familias de proporción.

- [ ] `scripts/redes.py` con metadatos PEP 723 y los subcomandos `entorno`, `generar` y
      `validar`.
- [ ] `catalogo/formatos.json` con los 12 formatos de `decisiones.md` (incluidas las
      portadas de reel y de destacado), sus zonas seguras y sus mínimos de texto.
- [ ] Esquema de plantilla (`arquitectura.md` §4.4) y su cargador, con mensajes de error
      claros.
- [ ] Composición: retícula, márgenes, zonas seguras, decoraciones y logo.
- [ ] Texto: métricas de Montserrat, corte de línea equilibrado, sin huérfanas en títulos,
      holgura para Canva y error de desborde con los caracteres que sobran.
- [ ] Escena y renderizador elegido en la fase 1; PNG rasterizado desde el PDF.
- [ ] Fotos: encaje por recorte con punto de interés (`"foco": [x, y]` en la pieza),
      degradado inferior como capa aparte (tratamiento principal), tarjeta redondeada y
      espacio vacío marcado.
- [ ] Validador con todas las reglas de `arquitectura.md` §5.4 y un reporte legible por
      Claude.
- [ ] `redes-tokens.json` inicial (escala tipográfica y retícula provisionales).
- [ ] Autotest para «cita», con casos que deben fallar.

**Terminado cuando:** `redes.py generar` produce PDF y PNG de «cita» en todos los
formatos, en claro y oscuro; el validador detecta todos los casos malos; el autotest pasa
en Linux, Mac y Windows; y una pieza generada se importa bien en Canva y en Figma.

---

## Fase 3. Catálogo v1

**Objetivo:** las 8 plantillas de la v1 (las series que marketing ya publica,
`decisiones.md`), con sus carruseles y las piezas internas, fieles a las piezas reales y al
Brandbook (`referencias-reales.md`).

- [ ] `tools/medir-referencias.py`: extrae posiciones, tamaños y márgenes normalizados a
      1080 px de las piezas reales (PDF de Figma y Canva en `plantillas/`, sin versionar) y,
      para los formatos sin pieza real, de las miniaturas del Brandbook (páginas 18 a 20).
- [ ] Cerrar `redes-tokens.json` con lo medido: escala tipográfica (con Light para citas y
      titulares de contraste), retícula, fondos (`#000033` y el degradado claro
      `#E8F0FE` → `#FFFFFF`), degradados (página 10), luces difusas y divisores (página 13).
- [ ] Biblioteca: formas de marca, divisores, luces difusas, botón de flecha, píldoras de
      hora y de etiqueta, comillas degradadas, burbuja con isotipo, lockup con etiqueta
      («NEO | New Hire») y subconjunto de íconos Lucide.
- [ ] Plantillas de la v1, por familia de proporción, en claro y oscuro, con una segunda
      variante donde las piezas reales o el Brandbook la muestren: bienvenida individual,
      bienvenida grupal, story de nuevo ingreso, día a día, Tech Update, cita, portada de
      reel y portada de destacado.
- [ ] Carruseles con las láminas de cada serie y botón de flecha en todas menos la última;
      PDF de varias páginas (o el archivo para Figma, según el destino) y un PNG por
      lámina.
- [ ] Piezas internas: banner de correo y pantallas horizontal y vertical con la cita, la
      bienvenida y Tech Update; fondo para Teams o Zoom (marca, con el centro libre para la
      persona).
- [ ] Datos obligatorios de cada plantilla (nombre y cargo en bienvenida y story de ingreso,
      hora y texto en cada lámina de día a día, fuente en toda cifra externa de Tech Update,
      autor y cargo en cita…).
- [ ] Catálogo visual: un PNG con todas las combinaciones.
- [ ] Revisión del catálogo con marketing; ajustes.

**Terminado cuando:** el autotest pasa con todas las combinaciones y marketing aprueba el
catálogo visual.

---

## Fase 4. Vista previa, dispositivos y kit de Canva y Figma

**Objetivo:** que la persona elija viendo las piezas como se verán publicadas, y que tenga
en Canva y en Figma todo lo necesario para editarlas.

- [ ] Dispositivos genéricos (celular, laptop, monitor, pantalla vertical) en SVG, sin
      logos de fabricantes.
- [ ] Feed simplificado de la cuenta NEO para Instagram y LinkedIn.
- [ ] `redes.py comparar`: hoja de comparación con las opciones dentro de su dispositivo.
- [ ] Dispositivo como elemento del post: decoración con la pantalla como espacio de foto,
      lista para caso de éxito y comunicado cuando lleguen en la v1.1.
- [ ] `redes.py entregar`: carpeta de entrega de `arquitectura.md` §5.6, solo con el
      archivo del destino pedido (Canva, Figma o los dos).
- [ ] `redes.py kit` y las guías de carga en el Kit de marca de Canva y en Figma.
- [ ] `references/canva.md`: importar el PDF, editar textos, reemplazar fotos, quitar el
      fondo de una foto para los recortes y usar el kit.
- [ ] `references/figma.md`: instalar el plugin de importación si la fase 1 eligió PDF,
      importar el archivo, editar textos, reemplazar fotos y usar el kit.

**Terminado cuando:** la hoja de comparación se lee bien en la pantalla del chat y alguien
de marketing carga el kit y edita una pieza importada, en Canva y en Figma, siguiendo solo
las guías.

---

## Fase 5. La skill en Claude

**Objetivo:** que cualquier pedido, simple o enrevesado, termine en buenas opciones sin
inventar nada.

- [ ] `SKILL.md`: descripción con las frases que la activan («post», «pieza», «Instagram»,
      «LinkedIn», «story», «carrusel», «bienvenida», «nuevo ingreso», «día a día», «Tech
      Update», «portada de reel», «destacado», «banner de correo», «fondo de Teams»…) y lo
      que no cubre (software: neo-design; presentaciones); reglas no negociables; flujo de
      `arquitectura.md` §9; instalación de `uv` por sistema.
- [ ] `references/ficha.md`: cómo armar la ficha, qué datos exige cada tipo, cómo formular
      la ronda de preguntas cerradas, cuándo usar marcas `[DATO]` y cómo preguntar el
      destino (Canva o Figma) cuando el pedido no lo dice, sin agregar una ronda.
- [ ] `references/plantillas.md`: qué plantilla según el contenido, campos, límites y cómo
      combinar las 3 opciones.
- [ ] `references/formatos.md` y `references/voz.md` (español neutro con «tú», sin emojis
      en piezas, texto alternativo, descripción y hashtags cuando se pidan).
- [ ] Fotos: leer adjuntos en Claude.ai y la carpeta `fotos/` en Claude Code.
- [ ] Pruebas con cuatro pedidos, en Claude Code y en Claude.ai:
  1. Simple, sin destino: «story de bienvenida para [nombre], Consultora de Growth».
  2. Largo con «metodología» y rol, para Figma.
  3. Incompleto: un Tech Update con una cifra sin fuente, para Canva.
  4. Fuera de marca: «con degradado arcoíris y emojis».

**Terminado cuando:** en los cuatro pedidos Claude pregunta solo lo necesario (el destino,
solo cuando no se dijo), no inventa datos, respeta la marca, entrega 3 opciones válidas y
el paquete de la elegida para el destino pedido.

---

## Fase 6. Piloto

**Objetivo:** usarla con pedidos reales antes del lanzamiento.

- [ ] Versión `0.9.0`.
- [ ] 2 o 3 personas de marketing y comunicación interna. Se instalan con `npx skills add`
      si tienen acceso al repo, o con el ZIP en Claude.ai si no (se acepta solo durante el
      piloto).
- [ ] Al menos una persona en Windows.
- [ ] Registro en `plans/piloto.md`:
  - pedido,
  - opciones generadas,
  - cuál eligió,
  - qué tuvo que corregir en Canva o Figma,
  - fallas.
- [ ] Corregir lo encontrado y repetir el autotest.

**Terminado cuando:** las piezas del piloto se publicaron o se aprobaron con cambios
menores en Canva o Figma, sin datos inventados ni fallas de importación abiertas. Versión
`1.0.0`.

---

## Fase 7. Lanzamiento

**Objetivo:** que toda la organización la tenga y la reciba actualizada sin hacer nada.

- [ ] Confirmar el plan de Claude de NEO (Team o Enterprise) y quién es el propietario de
      la organización.
- [ ] El propietario conecta el repo: *Configuración de la organización → Plugins y skills →
      Agregar → Sincronizar desde GitHub*, con «Sincronizar automáticamente» y la app de
      GitHub de Claude instalada en el repo (la instalas tú, como administrador del repo).
- [ ] Decidir a quién se deja disponible y a quién instalada por defecto.
- [ ] Verificar que aparece en Claude.ai, Cowork y Claude Code para alguien sin GitHub.
- [ ] Publicar una versión de prueba (`1.0.1`) y confirmar que llega sola.
- [ ] `README.md` para usuarios: cómo pedir una pieza (cinco ejemplos cortos), cómo
      importarla en Canva o Figma y cómo cargar el kit.

**Terminado cuando:** una persona de marketing sin GitHub usa la skill en Claude.ai y en
Claude Code, y recibe una actualización sin hacer nada.

---

## Después de la v1

- **v1.1:** cifra suelta, evento, vacante, caso de éxito, comunicado, concepto tipográfico,
  álbum de evento, lista de consejos, pregunta o artículo, foto con titular, persona o
  speaker y cuenta regresiva (`decisiones.md`).
- **Medidas oficiales:** reemplazar las medidas tomadas de las piezas exportadas y del
  Brandbook por las de los archivos fuente de marketing.
- **Figma con Auto Layout:** `arquitectura.md` §12.

## Qué se necesita de otras personas

| Fase | Quién | Qué |
|---|---|---|
| 0 | Tú | Crear el repo privado en GitHub |
| 1 | Marketing | Una cuenta de Canva Pro y una de Figma para la prueba de importación |
| 1 y 6 | Alguien con Windows | Probar la instalación con `uv` y el uso en Claude Code |
| 3 | Marketing | Revisar y aprobar el catálogo visual |
| 6 | Marketing y comunicación interna | 2 o 3 personas para el piloto |
| 7 | Propietario de la organización en Claude | Conectar el repo y definir la disponibilidad |
| Cuando estén | Marketing | Archivos fuente de las piezas y del Brandbook (Figma o Canva) |
