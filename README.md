# MLEARN

Material de estudio de **Machine Learning (MLEARN)**, Ingeniería de Telecomunicaciones (UPC · Telecom BCN).

Cada tema tiene su propia carpeta con una **plataforma de estudio interactiva**: un único `index.html` que funciona sin internet y reúne la teoría explicada paso a paso con la notación de las diapositivas, laboratorios interactivos, tests con corrección razonada, los ejercicios de la hoja resueltos, flashcards y una hoja resumen para imprimir.

## Temas

| Tema | Contenido | Estado | Carpeta |
|---|---|---|---|
| **2** | **Decision theory: Bayes, MAP, riesgo mínimo, Neyman-Pearson, LDA/QDA, estimación ML, ROC y métricas** | **Disponible** | [`Tema 2 - Decision Theory`](Tema%202%20-%20Decision%20Theory/) |
| **3** | **Feature selection: dimensionalidad, PCA, MDA, enfoques no lineales** | **Disponible** | [`Tema 3 - Feature Selection`](Tema%203%20-%20Feature%20Selection/) |
| 4 | k vecinos, lógica difusa, SVM, redes neuronales, árboles de decisión | Pendiente | — |
| 5 | Random forest | Pendiente | — |
| 6 | K-means y clustering | Pendiente | — |

La lista de temas pendientes sale del *course overview* de las diapositivas (diap. 2 del tema 3 y 29 del tema 2). Se irá completando a medida que avance la asignatura.

## Abrir online

Con GitHub Pages activado, la portada está en **https://marcel02.github.io/MLEARN/** y cada tema se abre desde ahí sin descargar nada (el tema 2, en https://marcel02.github.io/MLEARN/Tema%202%20-%20Decision%20Theory/, y el tema 3, en https://marcel02.github.io/MLEARN/Tema%203%20-%20Feature%20Selection/).

Para activarlo (una sola vez): **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main`, carpeta `/ (root)` → Save**. En uno o dos minutos el enlace funciona. GitHub Pages es gratis en repositorios públicos; en uno privado necesita un plan de pago, y la web queda pública aunque el repositorio no lo sea.

## Cómo usarlo sin conexión

1. **Descarga el repositorio**: botón verde **Code → Download ZIP** en GitHub, o `git clone`.
2. **Abre** `index.html` dentro de la carpeta del tema con un doble clic. Funciona en Chrome, Edge, Firefox y Safari, sin conexión.
3. **Para imprimir**, usa `hoja-resumen.pdf` (o el botón «Imprimir hoja resumen» de la propia página).

El progreso (conceptos marcados, tests, ejercicios y flashcards) se guarda en el navegador de cada persona. Cada uno lleva el suyo y no se sube al repositorio.

## Qué incluye cada tema

Los temas 2 y 3 siguen el mismo modelo:

- **Teoría por bloques**, en el orden del PDF, con «Diapositiva X · PDF p. Y» en cada tarjeta, un resumen visible y la explicación a fondo desplegable. Las derivaciones se revelan paso a paso.
- **Cajas destacadas**: apuntes manuscritos del profesor, errores habituales, erratas del material y conexiones con otros temas.
- **Laboratorios interactivos**: en el tema 2, MAP y riesgo mínimo en 1D, fronteras LDA/QDA en 2D, sesgo del estimador ML, ROC con Neyman-Pearson y matriz de confusión, y el test diagnóstico con prevalencias reales; en el tema 3, Pr(e) = Q(r/2), PCA en 2D, efecto de d′, restar o no la media, y MDA frente a PCA.
- **Tests** de 4–6 preguntas por bloque, con explicación de cada opción y modo «Repasar falladas».
- **Ejercicios** de la hoja con tres pistas graduales y solución paso a paso, comprobada numéricamente. En el tema 2 solo están los que mandó el profesor: 1, 2, 4, 5, 7.1, 7.2, 7.3, 9, 10 y 11.
- **Flashcards** de fórmulas y definiciones, y una **hoja resumen** con todas las fórmulas.
- **Erratas**: lista de erratas y dudas detectadas en el material, en la página de inicio.

## Estructura del repositorio

```
MLEARN/
├── README.md
├── index.html              portada con la lista de temas (GitHub Pages)
├── Tema 2 - Decision Theory/
│   └── …                   mismos cuatro archivos que el tema 3
├── Tema 3 - Feature Selection/
│   ├── index.html          plataforma completa (un solo archivo)
│   ├── hoja-resumen.pdf    fórmulas del tema en 2 páginas A4
│   ├── hoja-resumen.html   la misma hoja en formato web
│   └── LEEME.txt           instrucciones para compartir la carpeta
└── fuente/
    ├── tema-2/             piezas y scripts que generan el index.html del tema 2
    └── tema-3/             ídem para el tema 3
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
cd ../tema-2
python3 build_local.py "../../Tema 2 - Decision Theory"
```

## Registro de cambios

| Fecha | Cambio |
|---|---|
| 2026-11-11 | Tema 3 (Feature Selection): primera versión completa. |
| 2026-11-11 | Portada `index.html` para abrir los temas con GitHub Pages. |
| 2026-11-12 | Tema 2 (Decision Theory): primera versión completa, con los ejercicios asignados 1, 2, 4, 5, 7.1–7.3, 9, 10 y 11. |

## Origen del contenido

Elaborado a partir de las diapositivas y las hojas de ejercicios de la asignatura (tema 2: `ML_Chapter2` y `ExercisesChapter2MLEARN.pdf`; tema 3: `ML_Chapter3_FS_GO.pdf` y `ExercisesChapter3MLEARN.pdf`). **No es material oficial**: para cualquier duda manda lo que diga el profesor. Las erratas detectadas en el material original se señalan en cada tema.
