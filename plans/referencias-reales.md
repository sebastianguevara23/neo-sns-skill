# Referencias reales: cómo publica hoy marketing

Revisión del 2026-11-09 de las piezas que marketing ya publicó, comparadas con el Brandbook y
con lo acordado en `decisiones.md`. Sirve de base para las plantillas de la fase 3. Las
correcciones que se desprenden ya están aplicadas en los demás documentos (ver
[Qué se corrigió](#qué-se-corrigió)), igual que las seis decisiones que se tomaron después
de la revisión (ver [Decisiones tomadas](#decisiones-tomadas-2026-11-09)).

## Fuentes

| Material | Dónde | Notas |
|---|---|---|
| Piezas publicadas | Carpeta de Drive «Estrategia de redes sociales» (descarga del 2026-11-09), copiada en `plantillas/` del repo **sin versionar** | 119 archivos, 318 MB. Incluye fotos personales de colaboradores: no se sube a git (`.gitignore`) |
| Brandbook | `Brandbook.pdf`, v1.0, 24 páginas, 17 de agosto de 2026 | Es el mismo que citan los plans (páginas 18 a 20). No hay una versión más nueva en la carpeta de Drive |
| «Design System Neo Consulting.pdf» | 27 de julio de 2026 | Versión anterior del mismo Brandbook, con otro nombre. No usar |

## Inventario

| Serie | Formato | Piezas | Hecho en |
|---|---|---|---|
| Día a día de un colaborador | Carrusel 4:5, 9 a 11 láminas | 4 (Andrea, Daniel, Jurgita, Meilin) | Figma |
| Bienvenida individual («New Hire») | Carrusel 4:5, 3 láminas | 1 | Figma |
| Bienvenida grupal («New Hires») | Carrusel 4:5, portada + una lámina por persona | 1 | Canva |
| Story de nuevo ingreso | Story 9:16 | 8, más una de bienvenida genérica | Sin datos (PNG) |
| Tech Update (seguridad e IA) | Serie de 4 stories por tema | 4 temas, 16 stories | Sin datos (PNG) |
| Cita | Post 4:5 | 1 (Daniel Falcón, CEO) | Sin datos (PNG) |
| Concepto tipográfico | Post 4:5 | 1 («Análisis > Decisión») | Sin datos (PNG) |
| Cultura y eventos | Carrusel 4:5 con fotos | 1 (Halloween, 6 láminas) | Canva |
| Portada de reel | 9:16 | 4 (NEO Eventos, NEO Talks, NEO Workshops) | Sin datos (PNG) |
| Portada de destacado | 1:1 | 8 íconos | Sin datos (PNG) |

No hay piezas de LinkedIn, banners de correo, fondos de Teams ni pantallas: para esos formatos
el Brandbook sigue siendo la única referencia.

## Lo que confirman

- **Azul `#2D5BFF`.** Es el que usan las piezas recientes (Tech Update, destacados, New Hires,
  cierre de la bienvenida individual), igual que neo-design. El `#2B5BFC` del Brandbook solo
  aparece en la plantilla de Día a día, mezclado con `#2D5BFF`.
- **Montserrat** en todas las piezas, sin otra familia.
- **Fotos reales** de colaboradores y de la oficina. Nada generado con IA.
- **Español con «tú»** («Compártelo con tu equipo», «¿Sabes qué es un deepfake?»).
- **Claro y oscuro alternados** dentro de una misma serie (Tech Update: clara, oscura, oscura,
  clara).
- **Íconos lineales tipo Lucide** con trazo redondeado (destacados, flecha de los botones).
- **Formatos:** post 1080 × 1350, story 1080 × 1920 y carruseles de 4:5.

## Lo que difiere de los plans

| Tema | Plan anterior | Piezas reales |
|---|---|---|
| Referencia de medidas | Miniaturas del Brandbook | Las piezas reales están a 1080 px y son más fieles a cómo se publica; el Brandbook queda para lo que no tiene pieza real |
| Fondo oscuro | Candidatos `#000033` o `#050917` | **`#000033`** plano, o con luces difusas azules encima. `#050917` no aparece |
| Fondo claro | Sin definir | **Degradado vertical `#E8F0FE` → `#FFFFFF`** («Soft Atmosphere», página 10 del Brandbook) en todas las láminas claras |
| Pesos tipográficos | 400 a 900 | También **Light (300)**: «Decisión» en Light Italic, «Bienvenida al equipo», «Sobre ella», «New Hire». El Brandbook pide Light Italic para citas |
| Carruseles | Numeración «2/7» | **Botón circular azul con flecha** abajo, en todas las láminas menos la última. Sin numeración |
| Tratamiento de fotos | Duotono como capa | **Degradado** desde la foto hacia azul o navy, debajo del texto; tarjetas de foto con esquinas redondeadas; recortes de personas sin fondo; marco de polaroid. No se ve duotono plano |
| Logo | Variante y posición por plantilla | Posts y carruseles: lockup **«NEO \| 25 años»** arriba (centrado en posts sueltos, a la izquierda en láminas internas). Stories: **sin logo**. Reels: isotipo dentro de una burbuja de chat azul. Variante «NEO \| New Hire» (logo, separador y etiqueta) |
| Kicker | SemiBold con espaciado amplio | **ExtraBold en mayúsculas, azul**, sin espaciado amplio («RUMBO A LA OFICINA», «EXPLORANDO IA»). El espaciado amplio se usa en subtítulos de reels y de New Hires |
| Cifras | Sin fuente | Cada cifra externa lleva **«Fuente: …»** al pie (Kaspersky, IBM, capacitación de NEO) |
| Formatos | Sin portadas | También **portadas de reel** (9:16) y **de destacado** (1:1) |
| Emojis | Prohibidos | Aparecen en Halloween (pies de foto) y como carita dentro de «Bienvenido». Se mantienen prohibidos |
| Tamaño mínimo de texto | 32 px | El cuerpo real está entre 28 y 34 px, y las fuentes y etiquetas entre 20 y 28 px. Nuevo mínimo: 28 y 24 px |
| Pie | Sin definir | Algunas piezas llevan «@neo_digital», «neoconsulting.ai» o «neoconsulting.com». Se quitan: las piezas no llevan dominio ni usuario |

## Anatomía de las series

Medidas aproximadas en un lienzo de 1080 px de ancho, estimadas sobre los PNG y PDF
(±10 %). Se cierran con `tools/medir-referencias.py` en la fase 3.

### Día a día (carrusel 4:5)

1. **Portada:** foto del colaborador a sangre con luz difusa azul detrás, «Un día con» en
   Regular, nombre en Black y cargo en Regular, abajo a la izquierda, con una línea azul corta
   debajo. Logo arriba a la izquierda.
2. **«Un poco sobre mí»:** columna azul a la izquierda con titular ExtraBold y cuerpo de
   unos 28 px en blanco; foto a sangre a la derecha.
3. **Láminas de horario (6 a 8):** fondo claro degradado; píldora blanca con la hora
   («07:30»), kicker ExtraBold azul de unos 44 px, cuerpo navy de unos 30 px, foto en
   tarjeta redondeada. Alternan foto arriba, a la izquierda o a la derecha. Botón de flecha
   abajo a la derecha.

### Bienvenida individual (carrusel 4:5)

1. Fondo navy con luz azul, lockup «NEO | New Hire» centrado, «Bienvenida al equipo,» en
   Light azul, nombre en ExtraBold blanco, línea azul y cargo en cursiva. Recorte de la persona
   a la derecha.
2. «Sobre ella» en Light (unos 62 px) y viñetas de unos 29 px con palabras clave en negrita.
3. Cierre claro: «Estamos para apoyar tu crecimiento» y «¡Bienvenida, [nombre]!» en Black azul.
   La pieza real lleva el dominio al pie; la plantilla no lo lleva.

### Bienvenida grupal (carrusel 4:5)

1. Portada clara: recortes de las personas en tarjetas azules redondeadas, «BIENVENIDOS AL
   EQUIPO» en Black azul (unos 93 px), píldora navy «NEOs!» y nombres separados por «✦».
2. Una lámina por persona: foto a sangre con degradado oscuro abajo, nombre en Black
   mayúsculas, cargo en cursiva y una línea en mayúsculas espaciadas de unos 26 px («Y NUESTRO
   GROWTH PARTNER»).

### Story de nuevo ingreso (9:16)

Foto a sangre (frente al letrero «Think, Question, Explore, Repeat»), nombre en ExtraBold
blanco en dos líneas, cargo en cursiva, línea blanca fina y franja degradada a azul al pie.
Sin logo.

### Tech Update (serie de 4 stories)

1. **Portada clara:** etiqueta «TECH UPDATE» en píldora con borde, pregunta como titular
   (navy con la última parte en azul, unos 90 px), cuerpo corto y una palabra gigante de
   marca de agua azul muy pálida al pie («DEEP FAKE», «PHISHING»).
2. **Cifra oscura:** cifra gigante de marca de agua detrás, la misma cifra en Black (unos
   200 px), frase en unos 38 px, texto secundario y «Fuente: …» de unos 26 px.
3. **Lista oscura:** titular en dos tonos y tres puntos con línea de tiempo vertical
   numerada (título de unos 35 px y descripción de unos 28 px).
4. **Qué hacer, clara:** titular en dos tonos, pasos «01, 02, 03» separados por líneas y
   botón azul «Compártelo con tu equipo →». Marca de agua al pie.

La etiqueta «TECH UPDATE» mide unos 20 px: en la plantilla sube a 24 px, el mínimo para
textos secundarios.

### Cita (post 4:5)

Fondo navy con luces difusas azules, comillas gigantes con degradado azul, texto en Regular
con fragmentos en Bold y «— Nombre, cargo.» Logo arriba centrado.

### Concepto tipográfico (post 4:5)

Fondo `#000033` plano, palabra en ExtraBold muy grande, divisor de flecha («——— > ———»),
segunda palabra en Light Italic azul claro y párrafo con palabras destacadas en Bold azul
claro. La pieza real lleva al pie «@neo_digital» y «neoconsulting.ai»; la plantilla, no.
Queda para la v1.1.

### Portada de reel (9:16)

Foto a sangre con degradado a azul abajo, burbuja con el isotipo, nombre de la serie en
ExtraBold («Eventos», «Talks», «Workshops»), línea blanca y subtítulo en mayúsculas muy
espaciadas. El bloque de texto queda en el centro vertical, dentro del recorte 3:4 del perfil.

### Portada de destacado (1:1)

Ícono lineal azul `#2D5BFF` centrado sobre el degradado claro. Íconos usados: equipo,
calendario, estrella, micrófono, cohete, paleta de ping-pong y rompecabezas.

## Colores medidos

| Uso | HEX | Token |
|---|---|---|
| Azul principal (botones, kickers, íconos, titulares azules) | `#2D5BFF` | `color.brand.royal-blue` |
| Fondo oscuro y texto oscuro sobre claro | `#000033` | `color.brand.deep-navy` |
| Fondo claro (degradado vertical) | `#E8F0FE` → `#FFFFFF` | No existe como token de color: va en `redes-tokens.json` como degradado |
| Azul claro de acento sobre oscuro («Decisión», palabras destacadas, tarjetas) | `#7694FF` | No es token. El más cercano es `color.brand.blue-soft` `#7E99FE` |

## Qué se corrigió

| Documento | Cambio |
|---|---|
| `decisiones.md` | Autoridad visual y medidas desde las piezas reales; marca en las piezas (logo por formato); portadas de reel y de destacado; carruseles con flecha; tratamiento de fotos; cifras con fuente |
| `arquitectura.md` | Fondo oscuro `#000033` y fondo claro degradado; Montserrat Light; `medir-referencias.py`; tratamientos de foto y logo en el esquema de plantilla |
| `plan-implementacion.md` | Fase 3 mide sobre las piezas reales; plantillas con sus datos obligatorios (fuente en cifras); carruseles con flecha |
| `estado.md` | Esta revisión y las decisiones tomadas |
| Fuentes | Montserrat Light y Light Italic (300) en `assets/fonts/` y en `tools/preparar-fuentes.py` |
| `.gitignore` | `plantillas/` fuera de git |

`tests/prueba-canva/` sigue usando `#050917` de fondo. No se cambió porque la prueba mide cómo
llega cada elemento a Canva, no el color exacto; el motor usará `#000033`.

## Decisiones tomadas (2026-11-09)

| # | Pregunta | Decisión | Dónde quedó |
|---|---|---|---|
| 1 | Catálogo v1 | **Las series reales:** bienvenida individual, bienvenida grupal, story de nuevo ingreso, día a día, Tech Update, cita, portada de reel y portada de destacado. Cifra suelta, evento, vacante, caso de éxito y comunicado pasan a la v1.1, con el concepto tipográfico y el álbum de evento | `decisiones.md` (Catálogo), `plan-implementacion.md` (fase 3) |
| 2 | Canva o Figma | **El que pida la persona.** La skill sabe entregar para los dos, pero cada pieza va solo para el destino pedido; si el pedido no lo dice, Claude pregunta. El formato para Figma (el mismo PDF o un SVG con texto vivo) se elige en la fase 1 | `decisiones.md` (Salida y Ficha), `arquitectura.md` §4.1, §5.3, §5.6, §8 y §9, `prueba-canva.md` |
| 3 | Tamaño mínimo de texto | **28 px para cuerpo y 24 px para secundarios** en lienzos de 1080 px | `decisiones.md` (Validación), `arquitectura.md` §4.3 |
| 4 | Emojis | **Sin emojis**, tampoco en piezas de cultura; un ícono Lucide si hace falta un gesto | `decisiones.md` (Idioma) |
| 5 | Pie de las piezas | **Ni dominio ni usuario** | `decisiones.md` (Marca en las piezas) |
| 6 | Recortes de personas | **En Canva**, con «Quitar fondo». La plantilla deja el espacio marcado como «Recorte» | `decisiones.md` (Fotos), `arquitectura.md` §4.4 |
