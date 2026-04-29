Perfecto 💪 — te propongo ahora un **ejercicio final de unidad completo**, ideal para 1 h 30 min de trabajo guiado o autónomo.
Integra **todas las subunidades** del módulo *“001 – Planificación de interfaces gráficas”*, pero con un nivel justo para que el alumno llegue al final con un resultado **visible, funcional y evaluable**.

---

## 💻 Ejercicio final de unidad: **“Mini catálogo interactivo”**

### 🎯 Objetivo

Diseñar y construir una **página web funcional** que simule el **catálogo de productos o servicios** de una empresa, aplicando principios de diseño visual, estructura semántica, tipografía, color, interacción, componentes reutilizables y carga dinámica de datos.

---

### 🧩 Enunciado general

Crea una pequeña aplicación de una sola página llamada **`catalogo.html`** que muestre un listado de productos cargados desde un archivo `productos.json`, permita **filtrarlos**, **añadir nuevos elementos** desde un formulario, y muestre un diseño visual coherente y estructurado.

---

## 🔧 Requisitos paso a paso

### 1️⃣ Estructura general (HTML)

**Subunidades 001, 009 y 010**

La página debe contener:

```html
<header>        <!-- título principal y menú de navegación --> </header>
<main>          <!-- zona principal con listado y formulario --> </main>
<footer>        <!-- créditos o enlace --> </footer>
```

Dentro de `<main>`:

* una **sección de listado** (`<section id="listado">`)
* y una **sección de formulario** (`<section id="formulario">`)

El menú del `<header>` tendrá al menos 3 elementos (por ejemplo: Inicio | Productos | Contacto).

---

### 2️⃣ Diseño visual coherente (CSS interno o archivo aparte)

**Subunidad 002**

* Usa `font-family: 'Ubuntu', sans-serif;` o una fuente personalizada.
* Define dos colores base (uno principal y otro de acento).
* Centra el contenido principal y crea tarjetas (`div.producto`) con:

  ```css
  background: white;
  border-radius: 8px;
  box-shadow: 0 0 5px rgba(0,0,0,0.2);
  padding: 10px;
  margin: 10px;
  width: 150px;
  display: inline-block;
  text-align: center;
  ```
* Aplica un color diferente de fondo al header y al footer.
* Usa iconos o emojis en los botones.

---

### 3️⃣ Carga dinámica desde JSON

**Subunidades 005 y 007**

Crea un archivo llamado **`productos.json`** en la misma carpeta, con este contenido:

```json
[
  {"nombre": "Auriculares", "precio": 39.99},
  {"nombre": "Teclado", "precio": 25.50},
  {"nombre": "Ratón", "precio": 19.00}
]
```

En tu script JavaScript, al cargar la página:

```js
fetch("productos.json")
  .then(r => r.json())
  .then(datos => {
    const contenedor = document.getElementById("listado");
    datos.forEach(prod => {
      const card = document.createElement("div");
      card.className = "producto";
      card.innerHTML = `<h3>${prod.nombre}</h3><p>${prod.precio} €</p>`;
      contenedor.appendChild(card);
    });
  });
```

---

### 4️⃣ Interacción y validación

**Subunidades 003 y 006**

Debajo del listado habrá un pequeño **formulario** para añadir un nuevo producto:

```html
<form id="formAgregar">
  <input type="text" id="nombre" placeholder="Nombre del producto">
  <input type="number" id="precio" placeholder="Precio" step="0.01">
  <button type="submit">➕ Añadir</button>
</form>
```

El script validará los campos y añadirá una nueva tarjeta:

```js
document.getElementById("formAgregar").onsubmit = e => {
  e.preventDefault();
  const nombre = document.getElementById("nombre").value.trim();
  const precio = document.getElementById("precio").value.trim();
  if (nombre === "" || precio === "") {
    alert("Rellena ambos campos correctamente");
    return;
  }
  const card = document.createElement("div");
  card.className = "producto";
  card.innerHTML = `<h3>${nombre}</h3><p>${precio} €</p>`;
  document.getElementById("listado").appendChild(card);
  e.target.reset();
};
```

---

### 📁 Estructura final del proyecto

```
/catalogo/
 ├── catalogo.html
 └── productos.json
```

---

### ⏱️ Tiempo estimado

**1 hora 30 minutos**
*(30 min estructura + 30 min estilos + 30 min JS y test final)*

---

¿Quieres que te genere ahora el **código base completo y comentado** (HTML + CSS + JS + JSON) para que el alumnado parta de una plantilla y solo tenga que completarla o personalizarla?

