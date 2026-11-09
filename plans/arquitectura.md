# Arquitectura de neo-redes

Cómo se construye la skill. El qué y el porqué están en `decisiones.md`; el orden de
trabajo, en `plan-implementacion.md`.

## 1. Principios

1. **Claude escribe contenido, los scripts dibujan.** Claude nunca escribe coordenadas,
   SVG ni PDF. Elige una plantilla y llena sus campos en una especificación corta; un motor
   determinista resuelve la composición y genera los archivos. Así el resultado es
   consistente, cumple la marca y cuesta pocos tokens.
2. **La skill pone el criterio, el prompt pone el contenido.** La calidad no depende de cómo
   escriba el pedido la persona.
3. **Editable en Canva por diseño.** Todo lo que se dibuja se elige pensando en cómo llega a
   Canva: texto vivo, formas simples, una capa por elemento, nombres legibles.
4. **Neutral respecto del destino.** El motor produce una escena independiente del formato
   de archivo. Hoy se exporta a PDF y PNG; mañana se agrega un exportador para Figma sin
   tocar plantillas ni lógica.
5. **Misma marca que neo-design.** Colores, tipografía y logos vienen de neo-design por
   sincronización, nunca escritos a mano.
6. **Corre igual en todas partes.** Los mismos scripts funcionan en Claude Code (Mac,
   Windows, Linux) y en el entorno de código de Claude.ai.

## 2. Vista general

```
 Pedido (cualquier prompt)
        │
        ▼
 ┌──────────────┐   falta un dato o Claude escribió el texto
 │ 1. Ficha     │ ─────────────────────────────────────────► una ronda de preguntas
 └──────┬───────┘
        ▼
 ┌──────────────┐   Claude elige plantilla, variante y tema
 │ 2. Piezas    │   y llena los campos (N opciones, 3 por defecto)
 │   (JSON)     │
 └──────┬───────┘
        ▼                                     ── todo esto lo hacen los scripts ──
 ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐
 │ 3. Motor de  │ ─► │ 4. Escena    │ ─► │ 5. Validador │ ─► │ 6. Hoja de       │
 │   composición│    │  (capas)     │    │              │    │   comparación    │
 └──────────────┘    └──────┬───────┘    └──────┬───────┘    └────────┬─────────┘
                            │                   │ errores → Claude     │
                            │                   │ corrige la pieza     ▼
                            │                                    la persona elige
                            ▼                                          │
                     ┌──────────────┐                                  ▼
                     │ 7. Render    │ ─► PDF (Canva, LinkedIn) + PNG ─► paquete de entrega
                     └──────────────┘
```

## 3. Estructura del repo

```
neo-sns-skill/
├── .claude-plugin/
│   ├── plugin.json              versión y metadatos del plugin
│   └── marketplace.json         un solo plugin con "source": "./" (como neo-design)
├── skills/neo-redes/            ← lo único que necesita quien usa la skill
│   ├── SKILL.md                 flujo, reglas no negociables, cuándo usar cada comando
│   ├── references/
│   │   ├── ficha.md             cómo leer un pedido y qué preguntar
│   │   ├── formatos.md          lienzos, zonas seguras, mínimos y dónde se ve cada uno
│   │   ├── plantillas.md        qué plantilla según el contenido, campos y límites
│   │   ├── voz.md               voz NEO para piezas, texto alternativo y del post
│   │   └── canva.md             cómo importar, editar y reemplazar fotos en Canva
│   ├── catalogo/
│   │   ├── formatos.json        registro de formatos
│   │   └── plantillas/*.json    una definición por plantilla
│   ├── tokens/
│   │   ├── neo-tokens.json      copia de neo-design (no se edita a mano)
│   │   ├── redes-tokens.json    escala tipográfica, retícula y degradados propios de piezas
│   │   └── ORIGEN.json          versión de neo-design de la que se copió
│   ├── assets/
│   │   ├── logo/                copia de neo-design
│   │   ├── fonts/               Montserrat TTF estática + OFL.txt
│   │   ├── iconos/              subconjunto de Lucide (SVG) + licencia
│   │   ├── formas/              geometría de marca, divisores, luces difusas (PNG con alfa)
│   │   └── dispositivos/        celular, laptop, monitor, pantalla vertical
│   └── scripts/
│       ├── redes.py             punto de entrada único (subcomandos)
│       └── neo_redes/           paquete: pieza, composición, texto, escena,
│                                render_pdf, render_png, validador, comparación, kit
├── tools/                       mantenimiento (no lo usa marketing)
│   ├── sincronizar-marca.py     copia tokens y logos desde neo-design
│   └── medir-brandbook.py       extrae medidas de las miniaturas del Brandbook
├── tests/                       piezas de ejemplo, casos que deben fallar, autotest
├── plans/
├── README.md
└── CHANGELOG.md
```

Restricción de la sincronización de plugins: **no puede existir una carpeta `bin/` en la
raíz**. Los ejecutables van en `skills/neo-redes/scripts/`.

## 4. Modelo de datos

### 4.1 Ficha del pedido

Claude la arma en su razonamiento a partir de cualquier prompt; no hace falta guardarla
en un archivo. Campos:

| Campo | Obligatorio | Ejemplo |
|---|---|---|
| `formatos` | Sí | `["ig-post", "li-post"]` |
| `mensaje` | Sí | «Lanzamos el Summit de Transformación Agéntica» |
| `tipo` | No (Claude lo deduce) | `evento` |
| `textos_literales` | No | lo que vino entre comillas |
| `datos` | Según el tipo | fecha, hora, lugar, cifra, cargo, enlace |
| `cta` | No | «Regístrate» |
| `fotos` | No | archivos adjuntos o en `fotos/` |
| `opciones` | No (3) | de 1 a 5 |
| `extras` | No | descripción del post, hashtags |

Cada plantilla declara qué `datos` exige. Si falta uno, se pregunta o se marca como
`[DATO]`; nunca se inventa.

### 4.2 Pieza (lo único que escribe Claude)

```json
{
  "formato": "ig-post",
  "plantilla": "cifra",
  "variante": "a",
  "tema": "oscuro",
  "campos": {
    "kicker": "Caso de éxito",
    "cifra": "-40 %",
    "titulo": "en tiempo de soporte",
    "cuerpo": "Automatización de la mesa de ayuda de un banco."
  },
  "foto": null,
  "alt": "Cifra de -40 % en tiempo de soporte sobre fondo azul noche, con el logo de NEO."
}
```

Con foto, el campo es `{"archivo": "fotos/equipo.jpg", "foco": [0.5, 0.3]}`: el foco
(proporciones de ancho y alto) indica qué punto de la imagen debe quedar visible al
recortarla. Sin archivo, la plantilla deja el espacio de foto marcado.

Un carrusel es una pieza con `"formato": "ig-carrusel"` y una lista `laminas`, cada una con
su `plantilla` (`portada`, `lamina-texto`, `lamina-cifra`, `cierre`) y sus `campos`.

Una pieza ocupa unos cientos de tokens. Tres opciones cuestan menos que una respuesta
larga de chat.

### 4.3 Formato (`catalogo/formatos.json`)

```json
{
  "id": "ig-story",
  "nombre": "Story de Instagram",
  "ancho": 1080, "alto": 1920,
  "familia": "alta",
  "margen": 96,
  "zona_segura": { "arriba": 250, "abajo": 340, "izquierda": 64, "derecha": 64 },
  "texto_minimo": 32,
  "dispositivo": "celular",
  "plantillas": ["cita", "cifra", "evento", "vacante", "caso-exito", "comunicado"]
}
```

Familias de proporción: `vertical` (4:5), `cuadrada` (1:1), `alta` (9:16), `horizontal`
(16:9) y `franja` (3:1). Las plantillas definen su composición por familia, no por
formato, así un formato nuevo con una proporción conocida no exige rediseñar.

Mínimos de texto iniciales, a validar en la fase 3:

| Formato | Mínimo | Por qué |
|---|---|---|
| Posts, Stories y carruseles (1080 de ancho) | 32 px | Unos 12 px en un teléfono de 390 px |
| Banner de correo (1200 × 400) | 24 px | Se ve a la mitad: 12 px |
| Fondos y pantallas (1920 de ancho) | 32 px | Se leen a distancia |

### 4.4 Plantilla (`catalogo/plantillas/<id>.json`)

Define, por familia de proporción y por variante:

- **Regiones** en unidades de la retícula (12 columnas, ritmo 12/24/48 del Brandbook
  escalado al lienzo), no en píxeles.
- **Campos:** estilo tipográfico (token), alineación, máximo de líneas y de caracteres,
  si es obligatorio, y qué dato representa.
- **Decoraciones:** formas de la biblioteca (barra de acento, divisor degradado, geometría
  de marca, luz difusa), con su posición.
- **Tema:** qué token de color toma cada elemento en claro y en oscuro.
- **Foto:** si lleva espacio de foto, su región y el tratamiento (duotono, máscara).
- **Logo:** variante y posición.

Las plantillas no llevan colores ni tamaños sueltos: solo nombres de tokens.

### 4.5 Escena (salida del motor)

Lista ordenada de capas con posición absoluta, independiente del archivo final:

```json
{
  "lienzo": { "ancho": 1080, "alto": 1350 },
  "capas": [
    { "nombre": "Fondo", "tipo": "rect", "x": 0, "y": 0, "w": 1080, "h": 1350, "relleno": "#050917" },
    { "nombre": "Kicker", "tipo": "texto", "x": 96, "y": 120, "w": 888,
      "lineas": ["CASO DE ÉXITO"], "fuente": "Montserrat-SemiBold", "px": 32,
      "interlineado": 1.3, "espaciado": 0.08, "color": "#2D5BFF" },
    { "nombre": "Foto", "tipo": "foto", "x": 0, "y": 0, "w": 1080, "h": 640, "archivo": null },
    { "nombre": "Duotono", "tipo": "rect", "relleno": "#2D5BFF", "opacidad": 0.55 }
  ]
}
```

Tipos de capa: `rect` (con radio), `texto`, `foto` (archivo o espacio vacío), `imagen`
(raster de la biblioteca), `vector` (trazos de un SVG de la biblioteca), `degradado`
(lineal o radial). La escena es el contrato entre el motor y los renderizadores.

## 5. Componentes del motor

### 5.1 Composición

Resuelve la plantilla en el lienzo del formato: convierte regiones de retícula a píxeles,
respeta márgenes y zonas seguras, coloca decoraciones y logo, y pasa los campos al módulo
de texto.

### 5.2 Texto

- Mide con las métricas reales de Montserrat (las TTF de la skill).
- Corta líneas de forma equilibrada y sin palabras huérfanas en títulos.
- Si el texto no cabe en el máximo de líneas, **no achica la letra**: devuelve un error
  con cuántos caracteres sobran, para que Claude acorte o cambie de plantilla.
- Deja un margen de holgura en el ancho de cada caja, porque Canva vuelve a componer el
  texto con su propio motor al importar.

### 5.3 Renderizadores

| Salida | Para qué | Cómo |
|---|---|---|
| PDF | Importar en Canva; carrusel de LinkedIn | Texto vivo con Montserrat incrustada, un objeto por capa, una página por lámina |
| PNG | Vista previa y publicación directa | Se rasteriza **desde el PDF**, así el PNG es idéntico a lo que se importa |

La librería se elige en la fase 1 según cómo llega cada variante a Canva. Candidatas:

| Opción | A favor | En contra |
|---|---|---|
| ReportLab + pypdfium2 | Muy probado, transparencias y degradados en PDF, ruedas para Mac y Windows | Sin interletraje (kerning) por defecto: se nota en titulares grandes |
| skia-python | Interletraje, desenfoque y degradados nativos; PDF y PNG con el mismo código | Rueda pesada; hay que confirmar que esté o se pueda instalar en Claude.ai |

### 5.4 Validador

Revisa la escena y la pieza, y devuelve un reporte que Claude puede leer y corregir:

| Regla | Severidad |
|---|---|
| Texto por debajo del mínimo del formato | Error |
| Texto fuera de su caja o con más líneas de las permitidas | Error |
| Elemento en zona segura (salvo fondos y decoraciones marcadas como sangrado) | Error |
| Color fuera de los tokens | Error |
| Contraste por debajo de AA (4.5:1, o 3:1 en texto grande) | Error |
| Campo obligatorio vacío | Error |
| Marca `[DATO]` sin completar | Aviso (se informa a la persona) |
| Espacio de foto sin foto | Aviso |
| Falta el texto alternativo | Error |
| Capa sin nombre | Error |

### 5.5 Hoja de comparación

Un PNG con todas las opciones lado a lado, cada una dentro de su dispositivo (celular,
laptop o monitor, según el formato) y con un feed simplificado de la cuenta NEO. Claude la
mira **una sola vez** para revisar y se la muestra a la persona. No se abren los PNG uno
por uno, para ahorrar tokens de imagen.

### 5.6 Paquete de entrega

En Claude Code, dentro de la carpeta de trabajo:

```
piezas/2026-11-12-summit-ai-lab/
├── opciones.png                         hoja de comparación
├── opciones/opcion-1.json …             piezas de cada opción
└── entrega/                             solo la opción elegida
    ├── summit-ai-lab-ig-post.pdf        → importar en Canva
    ├── summit-ai-lab-ig-post.png
    ├── texto-alternativo.txt
    ├── texto-post.md                    solo si se pidió
    └── pieza.json                       para regenerar o ajustar después
```

En Claude.ai los mismos archivos se entregan como descargas. Los carruseles llevan un PDF
de varias páginas y un PNG por lámina.

### 5.7 Kit de Canva

`redes.py kit` arma una carpeta lista para cargar una vez en el Kit de marca de cada
cuenta: paleta en HEX con sus nombres, logos e isotipo (SVG y PNG), íconos, dispositivos y
formas de marca, más una guía de carga. Montserrat no se incluye porque ya está en Canva.

## 6. Entornos de ejecución

Un solo punto de entrada con subcomandos:

| Subcomando | Qué hace |
|---|---|
| `entorno` | Revisa Python, librerías y fuentes; dice qué falta y cómo resolverlo |
| `generar` | Pieza(s) → escena → validación → PDF y PNG |
| `validar` | Solo valida, sin generar archivos |
| `comparar` | Hoja de comparación de varias opciones |
| `entregar` | Arma el paquete de la opción elegida |
| `kit` | Kit de recursos para Canva |

`redes.py` declara sus dependencias en el propio archivo (metadatos PEP 723), así que:

- **Claude Code en Mac o Windows:** `uv run scripts/redes.py …`. `uv` descarga Python y
  las librerías la primera vez, sin permisos de administrador. Si `uv` no está, el
  `SKILL.md` le indica a Claude el comando de instalación según el sistema y Claude lo
  ejecuta; la persona solo pulsa «Permitir».
- **Claude.ai:** `python3 scripts/redes.py …` en su entorno de código. Si falta una
  librería, `pip install`. Qué trae instalado ese entorno se confirma en la fase 1.

Rutas y archivos se manejan con `pathlib`, sin comandos de shell, para que funcione igual
en Windows.

## 7. Marca

| Qué | Fuente | Cómo llega |
|---|---|---|
| Colores, pesos tipográficos | `neo-design/tokens/neo-tokens.json` | `tools/sincronizar-marca.py`, que registra la versión en `ORIGEN.json` |
| Logos e isotipo | `neo-design/assets/logo/` | Mismo script |
| Montserrat | Repositorio oficial de Google Fonts (OFL) | TTF estáticas incluidas en la skill. neo-design solo trae woff2 recortadas, que no sirven para generar PDF |
| Escala tipográfica, retícula y degradados de piezas | Brandbook, páginas 10, 13 y 18 a 20 | `redes-tokens.json`, propio de esta skill; las medidas salen de `tools/medir-brandbook.py` |
| Íconos | Lucide, trazo 2 px | Subconjunto en SVG con su licencia |

Pendiente de medir en la fase 3: el fondo oscuro exacto de las piezas del Brandbook
(candidatos `#000033` y `#050917`) y la construcción de sus degradados.

## 8. Cómo llega cada elemento a Canva

Supuestos que la fase 1 confirma o corrige. Si alguno falla, se registra aquí la
alternativa elegida.

| Elemento | En el PDF | En Canva se espera |
|---|---|---|
| Titular, kicker, cuerpo | Texto vivo, un objeto por bloque | Cuadro de texto editable en Montserrat |
| Fondos, tarjetas, barra de acento | Rectángulos vectoriales | Forma con color editable |
| Divisor y fondos degradados | Degradado vectorial | Forma con degradado o imagen; a confirmar |
| Luz difusa (blob) | PNG con transparencia | Imagen que se mueve o se borra |
| Duotono | Rectángulo con transparencia sobre la foto | Forma semitransparente editable |
| Espacio de foto | Forma marcada «Foto» | Forma que se reemplaza por una imagen; a confirmar cómo |
| Logo e íconos | Trazos vectoriales | Gráfico vectorial con color editable |

Preguntas abiertas de la prueba: si Canva junta las líneas de un párrafo en un solo cuadro
o las separa, si reconoce Montserrat por su nombre, si respeta transparencias y degradados,
y cuál es la forma más cómoda de reemplazar un espacio de foto.

## 9. Comportamiento de Claude (`SKILL.md`)

1. **Leer el pedido y armar la ficha.** Se ignoran instrucciones de rol o de método que no
   aportan contenido; si contradicen la marca, gana la marca.
2. **Completar el contenido.** Si falta un dato que exige la plantilla, o Claude escribió el
   texto, una sola ronda: la ficha resumida más preguntas cerradas. Si se pidió velocidad,
   marcas `[DATO]`. El diseño no se pregunta.
3. **Escribir las opciones.** Por defecto 3, combinando plantilla, variante y tema, con al
   menos una clara y una oscura.
4. **Generar y validar.** `redes.py generar`; si hay errores, Claude corrige la pieza (acorta
   su propio texto, cambia de plantilla o pregunta si el texto era literal) y vuelve a
   generar.
5. **Mostrar la hoja de comparación** y esperar la elección o los ajustes.
6. **Entregar** el paquete, con una línea sobre cómo importarlo en Canva y los avisos
   pendientes (fotos o datos por completar).

El `SKILL.md` contiene las reglas no negociables y el flujo; el detalle va en
`references/`, que Claude lee solo cuando lo necesita, para no cargar contexto de más.

## 10. Distribución y versiones

| Etapa | Cómo se instala | Quién |
|---|---|---|
| 1. Construcción y piloto | `npx skills add sebastianguevara23/neo-sns-skill -g --all` (requiere Node y acceso al repo privado). Para probar en Claude.ai, subir el ZIP a mano | Quien mantiene la skill y las personas del piloto |
| 2. Lanzamiento | El propietario de la organización conecta el repo en *Configuración de la organización → Plugins y skills → Sincronizar desde GitHub*, con sincronización automática | Toda la organización, según la disponibilidad que se defina |

- Versión semántica en `plugin.json` y `marketplace.json`; se sube en cada cambio y se
  anota en `CHANGELOG.md`.
- La rama principal es la que se distribuye: lo que no está listo vive en otra rama.

## 11. Calidad

- **Autotest** (`tests/`): genera todas las combinaciones de plantilla, formato y tema con
  contenido de ejemplo, y verifica que el validador las acepte. Incluye casos que deben
  fallar (texto largo, color suelto, letra chica, campo vacío).
- **Catálogo visual:** un PNG con todas las combinaciones, para revisarlas a ojo antes de
  cada versión.
- **Pruebas con pedidos reales:** uno simple, uno largo con «metodología», uno incompleto y
  uno fuera de marca, en Claude Code y en Claude.ai.

## 12. Extensión futura

- **Figma:** un exportador de escena a SVG con texto vivo (se arrastra a Figma) y otro a
  HTML con flexbox para importarlo con Auto Layout mediante html.to.design, o un plugin
  propio que lea la escena. Ninguno cambia plantillas ni piezas.
- **Plantillas nuevas:** un JSON en `catalogo/plantillas/`, su entrada en
  `references/plantillas.md` y su caso en el autotest.
- **Formatos nuevos:** una entrada en `formatos.json`; si su proporción ya existe, las
  plantillas sirven sin cambios.

## 13. Riesgos y supuestos

| Riesgo | Cómo se controla |
|---|---|
| La importación de PDF en Canva separa líneas, cambia fuentes o pierde transparencias | Fase 1 antes de todo lo demás; la arquitectura permite cambiar de renderizador sin tocar plantillas |
| Canva recompone el texto y cambian los saltos de línea | Holgura en el ancho de las cajas; se mide en la fase 1 |
| El entorno de Claude.ai no trae una librería o no permite instalarla | Se verifica en la fase 1; se prefiere la opción que corra sin instalar nada |
| TI bloquea instalaciones en las laptops | `uv` se instala en la carpeta del usuario, sin administrador; si aun así falla, se usa Claude.ai |
| Las medidas del Brandbook no coinciden con los archivos fuente | Se reemplazan cuando marketing los entregue; las plantillas usan retícula, así que el ajuste es local |
| Claude inventa un dato | Regla explícita en `SKILL.md`, campos de datos obligatorios por plantilla y marcas `[DATO]` que el validador reporta |
