# Decisiones acordadas (sesión de grilling, 2026-11-08 y 2026-11-09; revisadas con las piezas reales el 2026-11-09)

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
  Brandbook es heredado; las piezas que marketing publica hoy ya usan #2D5BFF). Fondo oscuro
  **#000033** y fondo claro en degradado vertical **#E8F0FE → #FFFFFF**, como en las piezas
  reales.
- **Referencias de diseño** (revisión del 2026-11-09, detalle en `referencias-reales.md`):
  1. Las piezas que marketing ya publica (carpeta de Drive «Estrategia de redes sociales»):
     mandan en composición, series y tratamientos.
  2. El Brandbook: paleta, degradados, tipografía y, para los formatos sin pieza real
     (LinkedIn, banner de correo, fondos y pantallas), las páginas 18 a 20.
- **Marca en las piezas:** posts y carruseles llevan el lockup «NEO | 25 años» arriba
  (centrado en posts sueltos, a la izquierda en láminas internas); las series pueden usar la
  variante con etiqueta («NEO | New Hire»). Las stories van sin logo. Las portadas de reel
  llevan el isotipo dentro de una burbuja azul. **Sin dominio ni usuario de redes** en las
  piezas (decidido el 2026-11-09).
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
| Portada de reel | 1080 × 1920 (9:16) | El perfil la recorta a 3:4 (1080 × 1440 al centro): el texto va en esa zona |
| Portada de destacado | 1080 × 1080 (1:1) | Instagram la muestra en un círculo: el ícono va centrado, dentro del 60 % del ancho |

## Catálogo

- **v1: las series que marketing ya publica** (decidido el 2026-11-09; anatomía de cada una
  en `referencias-reales.md`):

  | Plantilla | Formato principal |
  |---|---|
  | Bienvenida individual («New Hire») | Carrusel de 3 láminas |
  | Bienvenida grupal («New Hires») | Carrusel: portada y una lámina por persona |
  | Story de nuevo ingreso | Story |
  | Día a día de un colaborador | Carrusel de 9 a 11 láminas |
  | Tech Update | Serie de 4 stories (portada, cifra, lista, qué hacer) |
  | Cita | Post |
  | Portada de reel | 9:16 |
  | Portada de destacado | 1:1 |

  Cada una va también en los demás formatos donde tenga sentido (por ejemplo, la cita y la
  bienvenida en LinkedIn). Las piezas internas (banner de correo y pantallas) usan la cita,
  la bienvenida y Tech Update en su proporción; el fondo de Teams o Zoom lleva solo la marca.
- **v1.1:** las del Brandbook que todavía no se publican (cifra suelta, evento, vacante, caso
  de éxito y comunicado), más concepto tipográfico o manifiesto, álbum de evento (fotos en
  polaroid, como Halloween), lista de consejos, pregunta o artículo, foto con titular,
  persona o speaker y cuenta regresiva.
- **Carruseles:** cada serie define sus láminas (Día a día: portada, «Un poco sobre mí» y
  láminas de horario; bienvenida: portada, «Sobre ella» y cierre). Para indicar que hay más
  láminas se usa un **botón circular azul con flecha** abajo en todas menos la última, como
  en las piezas reales; sin numeración «2/7». Sin láminas que continúen la imagen de una a
  otra en la v1.
- **Cifras con fuente:** toda cifra que no sea de NEO lleva «Fuente: …» al pie, dada por la
  persona; si falta, se pregunta como cualquier otro dato.
- **Medidas:** se toman de las piezas reales de marketing (1080 px de ancho, PDF de Figma y
  de Canva) y, para los formatos sin pieza real, de las miniaturas del Brandbook. Cuando
  marketing entregue los archivos fuente, se reemplazan.
- **Plantillas nuevas:** las agrega solo el equipo que mantiene la skill, con aprobación de
  marketing o diseño. Marketing puede pedirlas, no agregarlas por su cuenta.

## Salida y edición

- **Destino: Canva o Figma, el que pida la persona** (decidido el 2026-11-09: marketing
  trabaja en los dos; seis de los ocho PDF reales salieron de Figma). La skill sabe
  entregar para los dos, pero cada pieza se entrega solo para el destino que se pidió, o
  para ambos si la persona lo pide así. **Si el pedido no lo dice, Claude pregunta**; nunca
  lo supone.
- **Paquete de cada pieza:** el archivo del destino elegido y **PNG** (vista previa o
  publicación directa). Para Canva, **PDF** con texto vivo y Montserrat incrustada. Para
  Figma, el formato se elige en la fase 1: el mismo PDF importado con el plugin
  pdf.to.design (Figma por sí solo no deja editable un PDF) o, si no conserva el texto, un
  SVG con texto vivo. Los carruseles de LinkedIn llevan siempre el PDF,
  que es lo que se sube como documento. Sin PPTX.
- **Sin envío directo** por conectores (ni a Canva ni a Figma): solo archivos. El envío
  directo a Figma se descartó por el costo en tokens de cada pieza.
- **Tokens:** Claude escribe una especificación corta por pieza; los scripts generan todos
  los archivos sin gastar tokens adicionales por formato.
- **Muy editable:** textos vivos, cada forma y color editable, capas con nombres en español
  («Título», «Kicker», «Foto»), espacios para fotos marcados y fáciles de reemplazar. En
  Canva el espacio de foto llega como forma, no como marco.
- **Tratamiento de fotos:** el principal es un **degradado** desde la foto hacia azul o navy
  debajo del texto, como capa aparte, no aplicado sobre la imagen, para que se conserve al
  reemplazarla. También se usan tarjetas de foto con esquinas redondeadas, marcos de
  polaroid y recortes de personas sin fondo (el recorte se hace en Canva con «Quitar
  fondo»). El duotono queda como alternativa, también como capa. Los efectos complejos
  (luces difusas, cristal) van como imagen en su propia capa.
- **Kit de recursos para Canva y Figma:** paleta en HEX, logos, isotipo, íconos,
  dispositivos y formas de marca. Las cuentas de Canva son **Pro individuales**: cada persona
  lo carga una vez en su Kit de marca, con una guía corta. En Figma, el mismo kit sirve para
  crear los estilos de color y los componentes de logo. Montserrat ya viene en los dos.
- **Fotos:** nunca generadas con IA. Si la persona las comparte (adjuntas en Claude.ai o en
  la carpeta `fotos/` en Claude Code), Claude las coloca; si no, quedan los espacios
  marcados para ponerlas en Canva o Figma. Los recortes de personas sin fondo los hace la
  persona en Canva («Quitar fondo»): la skill no quita fondos.
- **Dispositivos:** vista previa de cada opción en celular, laptop o monitor, con un feed
  simplificado de la cuenta NEO. También se pueden usar como elemento dentro de un post
  (por ejemplo, una laptop que muestra un sistema), con la pantalla como espacio de foto.
  Dibujos genéricos, sin logos de fabricantes.

## Comportamiento de Claude

- **Opciones:** 3 por defecto, o las que pida el prompt (de 1 a 5). Siempre al menos una
  clara y una oscura. Se muestran juntas en una hoja de comparación y el paquete editable se
  genera solo para la elegida, salvo que se pidan todas.
- **Ficha del pedido:** cualquier prompt, corto o con «metodologías», se reduce a la misma
  ficha. Solo son obligatorios el **formato**, el **mensaje principal** y el **destino**
  (Canva o Figma). Si falta el destino, Claude lo pregunta como una pregunta cerrada más en
  la ronda de preguntas o, si no hay ronda, junto con la hoja de comparación, porque el
  paquete editable solo se arma después de que la persona elige. Así no se agrega una ronda.
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
- **Idioma:** solo español neutro con «tú». **Sin emojis** en las piezas, tampoco en las de
  cultura o celebración: si hace falta un gesto (como la carita de «Bienvenido»), se usa un
  ícono Lucide. En la descripción del post, como máximo uno o dos si se pide.
- **Grilla de Instagram:** la skill no lleva registro de lo publicado en la v1.

## Validación

- En lienzos de 1080 px de ancho, **cuerpo de mínimo 28 px** y **textos secundarios**
  (fuentes, pies de foto, etiquetas) **de mínimo 24 px**: unos 10 y 9 px en la pantalla de
  un teléfono de 390 px. Queda por debajo de los 12 px de neo-design y se acepta así para
  seguir lo que ya usa marketing (decidido el 2026-11-09). Los demás formatos tienen su
  propio mínimo equivalente (`arquitectura.md` §4.3).
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
- Archivos fuente de las piezas reales y del Brandbook, en Figma o Canva (los tiene
  marketing).
- Las seis preguntas que abrió la revisión de piezas reales (catálogo v1, destino, tamaño
  mínimo de texto, emojis, pie y recortes) quedaron decididas el 2026-11-09 y están
  aplicadas arriba.

## Descartado y por qué

| Descartado | Motivo |
|---|---|
| SVG como formato para Canva | Canva lo trata como un solo gráfico: el texto no se edita y no se puede desagrupar |
| PPTX | Fuera de alcance: solo posts y piezas, nada de presentaciones |
| Envío directo a Figma con `use_figma` | Cada pieza costaría tokens en escribir el código de las capas |
| Emojis en piezas de cultura o celebración | Se mantiene la regla de marca: íconos Lucide en su lugar |
| Dominio y usuario de redes en el pie | Decidido el 2026-11-09: las piezas no los llevan |
| Quitar el fondo de las fotos dentro de la skill | Exige un modelo de recorte; se hace en Canva con «Quitar fondo» |
| Depender de impeccable o design-taste-frontend | Empujan decisiones de diseño web que chocan con el Brandbook |
| Imágenes generadas con IA | El Brandbook pide fotografía auténtica |
| Impresión | No se necesita |
| ZIP como distribución | Actualizar a mano no escala; se usa la sincronización del plugin |
