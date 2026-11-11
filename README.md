# MLEARN

Material de estudio de **Machine Learning (MLEARN)**, Ingeniería de Telecomunicaciones (UPC · Telecom BCN).

Cada tema tiene su propia carpeta con una **plataforma de estudio interactiva**: un único `index.html` que funciona sin internet y reúne la teoría explicada paso a paso con la notación de las diapositivas, laboratorios interactivos, tests con corrección razonada, los ejercicios de la hoja resueltos, flashcards y una hoja resumen para imprimir.

## Temas

| Tema | Contenido | Estado | Carpeta |
|---|---|---|---|
| 2 | Clasificadores gaussianos: discriminante lineal y cuadrático | Pendiente | — |
| **3** | **Feature selection: dimensionalidad, PCA, MDA, enfoques no lineales** | **Disponible** | [`Tema 3 - Feature Selection`](Tema%203%20-%20Feature%20Selection/) |
| 4 | k vecinos, lógica difusa, SVM, redes neuronales, árboles de decisión | Pendiente | — |
| 5 | Random forest | Pendiente | — |
| 6 | K-means y clustering | Pendiente | — |

La lista de temas pendientes sale del *course overview* de la diapositiva 2 del tema 3. Se irá completando a medida que avance la asignatura.

## Cómo usarlo

1. **Descarga el repositorio**: botón verde **Code → Download ZIP** en GitHub, o `git clone`.
2. **Abre** `index.html` dentro de la carpeta del tema con un doble clic. Funciona en Chrome, Edge, Firefox y Safari, sin conexión.
3. **Para imprimir**, usa `hoja-resumen.pdf` (o el botón «Imprimir hoja resumen» de la propia página).

El progreso (conceptos marcados, tests, ejercicios y flashcards) se guarda en el navegador de cada persona. Cada uno lleva el suyo y no se sube al repositorio.

## Qué incluye cada tema

Tomando el tema 3 como modelo:

- **Teoría por bloques**, en el orden del PDF, con «Diapositiva X · PDF p. Y» en cada tarjeta, un resumen visible y la explicación a fondo desplegable. Las derivaciones se revelan paso a paso.
- **Cajas destacadas**: apuntes manuscritos del profesor, errores habituales, erratas del material y conexiones con otros temas.
- **Laboratorios interactivos**: en el tema 3, Pr(e) = Q(r/2), PCA en 2D, efecto de d′, restar o no la media, y MDA frente a PCA.
- **Tests** de 4–6 preguntas por bloque, con explicación de cada opción y modo «Repasar falladas».
- **Ejercicios** de la hoja con tres pistas graduales y solución paso a paso, comprobada numéricamente.
- **Flashcards** de fórmulas y definiciones, y una **hoja resumen** con todas las fórmulas.
- **Erratas**: lista de erratas y dudas detectadas en el material, en la página de inicio.

## Estructura del repositorio

```
MLEARN/
├── README.md
├── Tema 3 - Feature Selection/
│   ├── index.html          plataforma completa (un solo archivo)
│   ├── hoja-resumen.pdf    fórmulas del tema en 2 páginas A4
│   ├── hoja-resumen.html   la misma hoja en formato web
│   └── LEEME.txt           instrucciones para compartir la carpeta
└── fuente/
    └── tema-3/             piezas y scripts que generan el index.html
```

Cada tema nuevo se añade como una carpeta `Tema N - Nombre/` y, si se quiere poder editar, su fuente en `fuente/tema-N/`.

## Regenerar un tema desde la fuente

El contenido de cada tema está repartido en `fuente/tema-N/parts/` (un archivo por bloque, más los datos de tests, flashcards y erratas). Para corregir algo, edita la pieza y vuelve a generar el `index.html`. Las dependencias (KaTeX y las tipografías) se descargan con npm y no se suben al repositorio:

```bash
cd fuente
mkdir -p vendor && (cd vendor && npm pack katex@0.16.9 && tar xzf katex-0.16.9.tgz)
mkdir -p vendor-fonts && cd vendor-fonts
for p in @fontsource/ibm-plex-sans@5.0.20 @fontsource/ibm-plex-mono@5.0.13 @fontsource/source-serif-4@5.0.19; do npm pack "$p"; done
for f in *.tgz; do mkdir -p "${f%.tgz}" && tar xzf "$f" -C "${f%.tgz}"; done
cd ../tema-3
python3 build_local.py "../../Tema 3 - Feature Selection"
```

## Registro de cambios

| Fecha | Cambio |
|---|---|
| 2026-11-11 | Tema 3 (Feature Selection): primera versión completa. |

## Origen del contenido

Elaborado a partir de las diapositivas y las hojas de ejercicios de la asignatura (tema 3: `ML_Chapter3_FS_GO.pdf` y `ExercisesChapter3MLEARN.pdf`). **No es material oficial**: para cualquier duda manda lo que diga el profesor. Las erratas detectadas en el material original se señalan en cada tema.
