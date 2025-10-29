📝 Enunciado

Crea una página llamada panel.html que represente el panel de control de una aplicación (por ejemplo, un “Panel de tareas”, “Listado de productos” o “Gestor de usuarios”).

La página debe incluir los siguientes elementos:

1️⃣ Estructura y maquetación

(Subunidades 001, 009 y 010)

Un <header> con el título del panel y un menú horizontal (mínimo 3 opciones).

Un <main> dividido en dos zonas:

una columna lateral (<nav>) con botones o enlaces;

una zona principal (<section>) con un listado dinámico.

Un <footer> con un texto de autor o enlace de contacto.

💡 Usa Flexbox o Grid para distribuir el contenido.

2️⃣ Estilo visual coherente

(Subunidad 002)

Define dos colores corporativos (primario y secundario).

Usa una tipografía personalizada (@font-face o Google Fonts).

El menú y los botones deben tener estilos uniformes y legibles.

Añade iconos o emojis para mejorar la comunicación visual.

3️⃣ Interacción

(Subunidades 003 y 006)

Al pulsar un botón “Añadir elemento”, debe aparecer un modal o bloque emergente con un formulario simple:

<input> de texto (por ejemplo, “Nombre del producto/tarea”).

Botón “Guardar”.

Al guardar, el nuevo elemento debe añadirse visualmente al listado. (no perdáis el tiempo con este punto)

Implementa una validación básica: si el campo está vacío, muestra un aviso (alert() o borde rojo).

4️⃣ Carga de datos dinámica

(Subunidades 005 y 007)

Crea un archivo datos.json con 3 objetos de ejemplo (por ejemplo, tareas, productos o usuarios).

Lo podéis hacer en Javascript o en PHP

si usais Javascript, Usad fetch() para cargar esos datos al abrir la página.
Si usais PHP, haced que PHP lea el json y en un bucle pintais HTML

Muestra los elementos dentro de la zona principal (por ejemplo, en tarjetas o una tabla).

5️⃣ Coherencia visual y funcional

(Subunidades 004 y 008)

Incluye al principio del archivo un pequeño comentario HTML con tu “mini guía de estilo”:

<!--
Guía visual:
- Colores: #0044cc y #ffcc00
- Fuente: 'Ubuntu'
- Bordes redondeados, sombras suaves
- Jerarquía: h1 (título), h2 (secciones)
-->


Crea una mini navegación funcional entre secciones (por ejemplo, botones que filtran o muestran partes del contenido).

📂 Estructura de entrega
/panel/
 ├── panel.html
 ├── estilo.css  (opcional, si no lo incluyes dentro del HTML)
 └── datos.json

