# Decisiones acordadas (sesión de grilling, 2026-11-08 y 2026-11-09)

Contrato del producto. Lo complementan `arquitectura.md` (cómo se construye) y
`plan-implementacion.md` (en qué orden). Donde haya conflicto, manda este documento.

## Producto

- **Qué es:** la skill `neo-redes`, para que marketing y comunicación interna de NEO
  creen piezas con la marca NEO desde Claude. Repo **privado**
  `sebastianguevara23/neo-sns-skill`.
- **Relación con neo-design:** es su hermana. neo-design aplica la marca a software;
  neo-redes la aplica a piezas. Son proyectos separados. De neo-design solo se copian
  tokens (color y tipografía), logos y fuentes. No depende de neo-design, impeccable ni
  ninguna otra skill para funcionar.
- **Autoridad visual:** la línea de neo-design. Azul canónico **#2D5BFF** (el #2B5BFC del
  Brandbook es heredado). El catálogo de piezas sale de las páginas 18 a 20 del Brandbook
  («Sistema de Instagram», «Instagram Stories», «Sistema de LinkedIn»).
- **Fuera de alcance:** presentaciones y cualquier pieza para imprimir.

## Formatos

| Formato | Lienzo (px) | Notas |
|---|---|---|
| Post de Instagram | 1080 × 1350 (4:5) | El perfil recorta a 3:4: unos 34 px por lado |
| Carrusel de Instagram | 1080 × 1350, hasta 20 láminas | |
| Story | 1080 × 1920 (9:16) | Zonas seguras: 250 px arriba, 340 px abajo |
| Post de LinkedIn | 1080 × 1080 (1:1, el del Brandbook) y 1080 × 1350 (4:5) | |
| Carrusel de LinkedIn | PDF de documento, en 1:1 o 4:5 | |
| Banner de correo | 1200 × 400 | Se ve a 600 × 200 |
| Fondo para Teams o Zoom | 1920 × 1080 | |
| Pantalla horizontal o vertical | 1920 × 1080 o 1080 × 1920 | |

## Catálogo

- **v1:** cita, cifra, evento, vacante, caso de éxito y comunicado, en todos los formatos
  donde tengan sentido.
- **v1.1:** lista de consejos, pregunta o artículo, foto con titular, persona o speaker,
  cuenta regresiva y manifiesto o marca.
- **Carruseles:** portada (titular fuerte), láminas internas de dos tipos (texto o lista, y
  cifra), cierre con llamada a la acción y logo, numeración «2/7». Sin láminas que
  continúen la imagen de una a otra en la v1.
- **Medidas:** se toman del PDF del Brandbook (sus miniaturas tienen texto vivo y se miden
  con precisión). Cuando marketing entregue los archivos fuente, se reemplazan.
- **Plantillas nuevas:** las agrega solo el equipo que mantiene la skill, con aprobación de
  marketing o diseño. Marketing puede pedirlas, no agregarlas por su cuenta.

## Salida y edición

- **Destino: solo Canva.** Figma queda para el futuro.
- **Paquete de cada pieza:** **PDF** con texto vivo y Montserrat incrustada (para importar
  en Canva y, en carruseles, para subir a LinkedIn) y **PNG** (vista previa o publicación
  directa). Sin PPTX.
- **Sin envío directo** por conectores (ni a Canva ni a Figma): solo archivos. El envío
  directo a Figma se descartó por el costo en tokens de cada pieza.
- **Tokens:** Claude escribe una especificación corta por pieza; los scripts generan todos
  los archivos sin gastar tokens adicionales por formato.
- **Muy editable:** textos vivos, cada forma y color editable, capas con nombres en español
  («Título», «Kicker», «Foto»), espacios para fotos marcados y fáciles de reemplazar. En
  Canva el espacio de foto llega como forma, no como marco.
- **Tratamiento de fotos:** el duotono va como una capa de color con transparencia encima
  de la foto, no aplicado sobre la imagen, para que se conserve al reemplazarla. Los
  efectos complejos (luces difusas, cristal) van como imagen en su propia capa.
- **Kit de recursos para Canva:** paleta en HEX, logos, isotipo, íconos, dispositivos y
  formas de marca. Las cuentas de Canva son **Pro individuales**: cada persona lo carga una
  vez en su Kit de marca, con una guía corta. Montserrat ya viene en Canva.
- **Fotos:** nunca generadas con IA. Si la persona las comparte (adjuntas en Claude.ai o en
  la carpeta `fotos/` en Claude Code), Claude las coloca; si no, quedan los espacios
  marcados para ponerlas en Canva.
- **Dispositivos:** vista previa de cada opción en celular, laptop o monitor, con un feed
  simplificado de la cuenta NEO. También se pueden usar como elemento dentro de un post
  (por ejemplo, una laptop que muestra un sistema), con la pantalla como espacio de foto.
  Dibujos genéricos, sin logos de fabricantes.

## Comportamiento de Claude

- **Opciones:** 3 por defecto, o las que pida el prompt (de 1 a 5). Siempre al menos una
  clara y una oscura. Se muestran juntas en una hoja de comparación y el paquete editable se
  genera solo para la elegida, salvo que se pidan todas.
- **Ficha del pedido:** cualquier prompt, corto o con «metodologías», se reduce a la misma
  ficha. Solo son obligatorios el **formato** y el **mensaje principal**.
- **Claude decide el diseño, nunca inventa contenido.** Cifras, fechas, nombres, citas
  atribuidas a personas, enlaces y datos de eventos vienen de la persona. Si falta un dato,
  o si Claude escribió el texto en lugar de recibirlo, hace **una sola ronda** de preguntas
  cerradas antes de generar. Si la persona pide velocidad («hazlo ya»), deja marcas
  visibles como `[FECHA]`. El diseño nunca se pregunta.
- **Texto literal:** lo que va entre comillas se usa tal cual. Si un texto propio de Claude
  no cabe, Claude lo acorta; si no cabe un texto literal de la persona, Claude busca otra
  plantilla donde quepa y, si no la hay, le propone una versión corta y pregunta. Nunca se
  achica la letra por debajo de la escala.
- **Marca primero:** si el pedido choca con la marca, gana la marca y Claude lo explica.
- **Textos del post:** el texto alternativo de la imagen va siempre. La descripción y los
  hashtags, solo si se piden.
- **Idioma:** solo español neutro con «tú». **Sin emojis** en las piezas (íconos Lucide).
  En la descripción del post, como máximo uno o dos si se pide.
- **Grilla de Instagram:** la skill no lleva registro de lo publicado en la v1.

## Validación

- Texto de **mínimo 32 px** en lienzos de 1080 px de ancho (unos 12 px en la pantalla del
  teléfono, el mismo mínimo de neo-design). Los demás formatos tienen su propio mínimo
  equivalente.
- Zonas seguras por formato, paleta de la marca, contraste AA, límite de caracteres por
  campo y nada de texto fuera de su caja.

## Plataforma y distribución

- **Dónde se usa:** Claude Code (la app de escritorio) como experiencia principal, más
  Claude.ai y Cowork. Una sola skill para todos.
- **Scripts en Python.** En las laptops (Mac y Windows), la primera vez Claude instala `uv`
  por su cuenta y la persona solo pulsa «Permitir»; `uv` trae Python y las librerías. En
  Claude.ai no hay nada que instalar.
- **Etapa 1 (hasta terminar la v1):** instalación con
  `npx skills add sebastianguevara23/neo-sns-skill`, igual que neo-design. Solo para quien
  prueba la skill.
- **Etapa 2 (lanzamiento):** plugin sincronizado desde el repo privado por el propietario
  de la organización en Claude (funciona en Team y en Enterprise). Cada push a la rama
  principal llega solo a Claude.ai, Cowork y Claude Code. Nadie de marketing necesita
  GitHub ni subir ZIP. Si resultaran ser cuentas individuales, cada persona agrega el
  marketplace una vez y activa la sincronización automática.

## Pendientes

- Confirmar el plan de Claude de NEO (Team o Enterprise). No bloquea la construcción.
- A quién se deja la skill disponible y a quién instalada por defecto (se decide en la
  etapa 2).
- Archivos fuente de las plantillas del Brandbook (los tiene marketing).

## Descartado y por qué

| Descartado | Motivo |
|---|---|
| SVG como formato para Canva | Canva lo trata como un solo gráfico: el texto no se edita y no se puede desagrupar |
| PPTX | Fuera de alcance: solo posts y piezas, nada de presentaciones |
| Envío directo a Figma con `use_figma` | Cada pieza costaría tokens en escribir el código de las capas |
| Figma en la v1 | Se prioriza Canva; la arquitectura deja lista la extensión |
| Depender de impeccable o design-taste-frontend | Empujan decisiones de diseño web que chocan con el Brandbook |
| Imágenes generadas con IA | El Brandbook pide fotografía auténtica |
| Impresión | No se necesita |
| ZIP como distribución | Actualizar a mano no escala; se usa la sincronización del plugin |
