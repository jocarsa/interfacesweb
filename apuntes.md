# interfacesweb

**Author:** Jose Vicente Carratala Sanchis

## Table of contents

- [Planificación de interfaces gráficas](#planificacion-de-interfaces-graficas)
  - [Elementos del diseño: percepción visual.](#elementos-del-diseno-percepcion-visual)
  - [Color, tipografía, iconos.](#color-tipografia-iconos)
  - [Interacción persona-ordenador.](#interaccion-persona-ordenador)
  - [Interpretación de guías de estilo. Elementos.](#interpretacion-de-guias-de-estilo-elementos)
  - [Generación de documentos y sitios web.](#generacion-de-documentos-y-sitios-web)
  - [Componentes de una interfaz web.](#componentes-de-una-interfaz-web)
  - [Tecnologías para el diseño de documentos web.](#tecnologias-para-el-diseno-de-documentos-web)
  - [Mapa de navegación. Prototipos.](#mapa-de-navegacion-prototipos)
  - [Maquetación web. Elementos de ordenación.](#maquetacion-web-elementos-de-ordenacion)
  - [Plantilla de diseño.](#plantilla-de-diseno)
  - [Simulacro de examen 1](#simulacro-de-examen-1)
  - [Simulacro de examen 2](#simulacro-de-examen-2)
  - [Repaso modal](#repaso-modal)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad)
  - [Examen final](#examen-final)
- [Uso de estilos](#uso-de-estilos)
  - [Estilos en línea basados en etiquetas y en clases.](#estilos-en-linea-basados-en-etiquetas-y-en-clases)
  - [Crear y vincular hojas de estilo.](#crear-y-vincular-hojas-de-estilo)
  - [Crear y vincular hojas de estilo en cascada externa.](#crear-y-vincular-hojas-de-estilo-en-cascada-externa)
  - [Herramientas y test de verificación.](#herramientas-y-test-de-verificacion)
  - [Tecnologías y frameworks.](#tecnologias-y-frameworks)
  - [Preprocesadores de estilos. Variables, mixins y funciones.](#preprocesadores-de-estilos-variables-mixins-y-funciones)
- [Implantación de contenido multimedia](#implantacion-de-contenido-multimedia)
  - [Tipos de Imágenes en la web.](#tipos-de-imagenes-en-la-web)
  - [Derechos de la propiedad intelectual. Licencias. Ley de la propiedad intelectual. Derechos de autor.](#derechos-de-la-propiedad-intelectual-licencias-ley-de-la-propiedad-intelectual-derechos-de-autor)
  - [Imágenes. Software para crear y procesar imágenes. Formatos. Conversiones](#imagenes-software-para-crear-y-procesar-imagenes-formatos-conversiones)
  - [Optimización de imágenes para la web.](#optimizacion-de-imagenes-para-la-web)
  - [Audio: formatos. Conversiones de formatos](#audio-formatos-conversiones-de-formatos)
  - [Vídeo: codificación de vídeo, conversiones de formatos](#video-codificacion-de-video-conversiones-de-formatos)
  - [Animaciones.](#animaciones)
  - [Integración de audio y vídeo en una animación.](#integracion-de-audio-y-video-en-una-animacion)
- [Integración de contenido interactivo](#integracion-de-contenido-interactivo)
  - [Elementos interactivos.](#elementos-interactivos)
  - [Comportamientos interactivos. Comportamiento de los elementos.](#comportamientos-interactivos-comportamiento-de-los-elementos)
  - [Ejecución de secuencias de comandos.](#ejecucion-de-secuencias-de-comandos)
  - [Verificación del funcionamiento en distintos navegadores y dispositivos.](#verificacion-del-funcionamiento-en-distintos-navegadores-y-dispositivos)
- [Diseño de webs accesibles](#diseno-de-webs-accesibles)
  - [El Consorcio World Wide Web (W3C).](#el-consorcio-world-wide-web-w3c)
  - [Principios y Pautas de Accesibilidad al Contenido en la Web (WCAG).](#principios-y-pautas-de-accesibilidad-al-contenido-en-la-web-wcag)
  - [Criterios de conformidad. Niveles de conformidad.](#criterios-de-conformidad-niveles-de-conformidad)
  - [Técnicas para satisfacer los requisitos definidos en las WCAG.](#tecnicas-para-satisfacer-los-requisitos-definidos-en-las-wcag)
  - [Prioridades. Puntos de verificación.](#prioridades-puntos-de-verificacion)
  - [Métodos para realizar revisiones preliminares y evaluaciones de adecuación o conformidad de documentos web.](#metodos-para-realizar-revisiones-preliminares-y-evaluaciones-de-adecuacion-o-conformidad-de-documentos-web)
  - [Herramientas de análisis de accesibilidad web.](#herramientas-de-analisis-de-accesibilidad-web)
  - [Chequeo de la accesibilidad web desde diferentes navegadores y dispositivos.](#chequeo-de-la-accesibilidad-web-desde-diferentes-navegadores-y-dispositivos)
  - [Posicionamiento en buscadores. Mejora de la visibilidad de un sitio web en diferentes buscadores.](#posicionamiento-en-buscadores-mejora-de-la-visibilidad-de-un-sitio-web-en-diferentes-buscadores)
- [Implementación de la usabilidad en la web. Diseño amigable](#implementacion-de-la-usabilidad-en-la-web-diseno-amigable)
  - [Análisis de la usabilidad. Técnicas.](#analisis-de-la-usabilidad-tecnicas)
  - [Identificación del objetivo de la web.](#identificacion-del-objetivo-de-la-web)
  - [Tipos de usuario.](#tipos-de-usuario)
  - [Barreras identificadas por los usuarios.](#barreras-identificadas-por-los-usuarios)
  - [Información fácilmente accesible.](#informacion-facilmente-accesible)
  - [Velocidad de conexión.](#velocidad-de-conexion)
  - [Importancia del uso de estándares externos.](#importancia-del-uso-de-estandares-externos)
  - [Navegación fácilmente recordada frente a navegación redescubierta.](#navegacion-facilmente-recordada-frente-a-navegacion-redescubierta)
  - [Facilidad de navegación en la web.](#facilidad-de-navegacion-en-la-web)
  - [Verificación de la usabilidad en diferentes navegadores y tecnologías.](#verificacion-de-la-usabilidad-en-diferentes-navegadores-y-tecnologias)
  - [Herramientas y test de verificación.](#herramientas-y-test-de-verificacion-1)
- [.git](#git)
  - [branches](#branches)
  - [hooks](#hooks)
  - [info](#info)
  - [logs](#logs)
  - [objects](#objects)
  - [refs](#refs)

---

<a id="planificacion-de-interfaces-graficas"></a>
# Planificación de interfaces gráficas

<a id="elementos-del-diseno-percepcion-visual"></a>
## Elementos del diseño: percepción visual.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/001-Elementos%20del%20dise%C3%B1o%3A%20percepci%C3%B3n%20visual.)

### estructural
<small>Creado: 2025-10-14 18:35</small>

`001-estructural.html`

```html
<html>
	<head>
	</head>
	<body>
		
	</body>
</html>
```

### bloques
<small>Creado: 2025-10-14 18:35</small>

`002-bloques.html`

```html
<html>
	<head>
	</head>
	<body>
		<header>
		</header>
		<div id="destacado">
		</div>
		<main>
		</main>
	</body>
</html>
```

### lista en el menu
<small>Creado: 2025-10-14 18:35</small>

`003-lista en el menu.html`

```html
<html>
	<head>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
		</div>
		<main>
		</main>
	</body>
</html>
```

### estilo
<small>Creado: 2025-10-14 18:35</small>

`004-estilo.html`

```html
<html>
	<head>
		<style>
			*{padding:0px;margin:0px;font-family:sans-serif;}
			ul{list-style-type:none;}
			ul li{display:inline-block;}
		</style>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
		</div>
		<main>
		</main>
	</body>
</html>
```

### estilo.htrml
<small>Creado: 2025-10-14 18:35</small>

`004-estilo.htrml.txt`

```
<html>
	<head>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
		</div>
		<main>
		</main>
	</body>
</html>
```

### menu
<small>Creado: 2025-10-14 18:35</small>

`005-menu.html`

```html
<html>
	<head>
		<style>
			*{padding:0px;margin:0px;font-family:sans-serif;}
			ul{list-style-type:none;}
			ul li{display:inline-block;}
		</style>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
		</div>
		<main>
		</main>
	</body>
</html>
```

### centrar
<small>Creado: 2025-10-14 18:35</small>

`006-centrar.html`

```html
<html>
	<head>
		<style>
			*{padding:0px;margin:0px;font-family:sans-serif;}
			ul{list-style-type:none;text-align:center;}
			ul li{display:inline-block;}
		</style>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
		</div>
		<main>
		</main>
	</body>
</html>
```

### Afinar estilo
<small>Creado: 2025-10-14 18:35</small>

`007-Afinar estilo.html`

```html
<html>
	<head>
		<style>
			*{padding:0px;margin:0px;font-family:sans-serif;}
			ul{list-style-type:none;text-align:center;}
			ul li{display:inline-block;color:rgb(50,50,50);font-size:10px;padding:10px;}
		</style>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
		</div>
		<main>
		</main>
	</body>
</html>
```

### destacado
<small>Creado: 2025-10-14 18:35</small>

`008-destacado.html`

```html
<html>
	<head>
		<style>
			*{padding:0px;margin:0px;font-family:sans-serif;}
			ul{list-style-type:none;text-align:center;}
			ul li{display:inline-block;color:rgb(50,50,50);font-size:10px;padding:10px;}
		</style>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
			En este destacado pondré información que me interese resaltar en la página para que el usuario la vea
		</div>
		<main>
		</main>
	</body>
</html>
```

### estilo del destacado
<small>Creado: 2025-10-14 18:35</small>

`009-estilo del destacado.html`

```html
<html>
	<head>
		<style>
			*{padding:0px;margin:0px;font-family:sans-serif;}
			ul{list-style-type:none;text-align:center;}
			ul li{display:inline-block;color:rgb(50,50,50);font-size:10px;padding:10px;}
			#destacado{background:rgb(240,240,240);font-size:11px;text-align:center;padding:14px;}
		</style>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
			En este destacado pondré información que me interese resaltar en la página para que el usuario la vea
		</div>
		<main>
		</main>
	</body>
</html>
```

### imagen de fondo
<small>Creado: 2025-10-14 18:35</small>

`010-imagen de fondo.html`

```html
<html>
	<head>
		<style>
			*{padding:0px;margin:0px;font-family:sans-serif;}
			ul{list-style-type:none;text-align:center;}
			ul li{display:inline-block;color:rgb(50,50,50);font-size:10px;padding:10px;}
			#destacado{background:rgb(240,240,240);font-size:11px;text-align:center;padding:14px;}
		</style>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
			En este destacado pondré información que me interese resaltar en la página para que el usuario la vea
		</div>
		<main>
		</main>
	</body>
</html>
```

### elementos del heroe
<small>Creado: 2025-10-14 18:35</small>

`011-elementos del heroe.html`

```html
<html>
	<head>
		<style>
			*{padding:0px;margin:0px;font-family:sans-serif;}
			ul{list-style-type:none;text-align:center;}
			ul li{display:inline-block;color:rgb(50,50,50);font-size:10px;padding:10px;}
			#destacado{background:rgb(240,240,240);font-size:11px;text-align:center;padding:14px;}
		</style>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
			En este destacado pondré información que me interese resaltar en la página para que el usuario la vea
		</div>
		<main>
			<h1>Producto</h1>
			<h2>Briiiiiiillante</h2>
			<img src="heroe.jpg">
			<p>Mensaje sugerente</p>
			<button>Comprar</button>
		</main>
	</body>
</html>
```

### estilo del heroe
<small>Creado: 2025-10-14 18:35</small>

`012-estilo del heroe.html`

```html
<html>
	<head>
		<style>
			*{padding:0px;margin:0px;font-family:sans-serif;}
			ul{list-style-type:none;text-align:center;}
			ul li{display:inline-block;color:rgb(50,50,50);font-size:10px;padding:10px;}
			#destacado{background:rgb(240,240,240);font-size:11px;text-align:center;padding:14px;}
			main{text-align:center;}
			main img{width:50%;}
		</style>
	</head>
	<body>
		<header>
			<ul>
				<li>M</li>
				<li>Tienda</li>
				<li>Mac</li>
				<li>iPad</li>
				<li>iPhone</li>
				<li>Watch</li>
				<li>AirPods</li>
				<li>TV y Casa</li>
				<li>Entretenimiento</li>
				<li>Accesorios</li>
				<li>Soporte</li>
				<li>L</li>
				<li>T</li>
			</ul>
		</header>
		<div id="destacado">
			En este destacado pondré información que me interese resaltar en la página para que el usuario la vea
		</div>
		<main>
			<h1>Producto</h1>
			<h2>Br<span style="color:red">i</span><span style="color:green">i</span><span style="color:orange">i</span><span style="color:blue">i</span><span style="color:yellow">i</span>llante</h2>
			<img src="heroe.jpg">
			<p>Mensaje sugerente</p>
			<button>Comprar</button>
		</main>
	</body>
</html>
```


<a id="color-tipografia-iconos"></a>
## Color, tipografía, iconos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/002-Color%2C%20tipograf%C3%ADa%2C%20iconos.)

### color
<small>Creado: 2025-10-14 18:35</small>

`001-color.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				color:red;
				background:orange;
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### hexadecimal
<small>Creado: 2025-10-14 18:35</small>

`002-hexadecimal.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				color:#ff0000;
				background:#ffcc00;
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### rgb
<small>Creado: 2025-10-14 18:35</small>

`003-rgb.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				color:rgb(255,0,0);
				background:rgb(255,200,0);
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### rgba
<small>Creado: 2025-10-14 18:35</small>

`004-rgba.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				color:rgba(255,0,0,0.2);
				background:rgb(255,200,0);
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### significado de los colores.md
<small>Creado: 2025-10-14 18:35</small>

`005-significado de los colores.md.txt`

```
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				color:rgba(255,0,0,0.2);
				background:rgb(255,200,0);
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### tipografias
<small>Creado: 2025-10-14 18:35</small>

`006-tipografias.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				font-family:sans-serif;
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### serifas
<small>Creado: 2025-10-14 18:35</small>

`007-serifas.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				font-family:serif;
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### cursiva
<small>Creado: 2025-10-14 18:35</small>

`008-cursiva.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				font-family:cursive;
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### monoespaciada
<small>Creado: 2025-10-14 18:35</small>

`009-monoespaciada.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				font-family:monospace;
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### fantasia
<small>Creado: 2025-10-14 18:35</small>

`010-fantasia.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			#contenedor{
				font-family:fantasy;
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### fuente ttf
<small>Creado: 2025-10-14 18:35</small>

`011-fuente ttf.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			/* Fuente Ubuntu */
			@font-face {
			    font-family: 'mifuente';
			    src: url('Ubuntu-R.ttf');
			}
			#contenedor{
				font-family:mifuente;
			}
		</style>
	</head>
	<body>
		<div id="contenedor">
			Esto es un contenido
		</div>
	</body>
</html>
```

### significado de las fuentes.md
<small>Creado: 2025-10-14 18:35</small>

`012-significado de las fuentes.md.txt`

```
Letra de palo = Limpieza, seriedad, claridad
Serifas = documentos, periodicos, elegancia, estilo
Cursiva (handwritten) = Acabado personal, humano, cercano, cálido
Monoespaciado = Maquina de escribir, recta, militar
```

### menu
<small>Creado: 2025-10-14 18:35</small>

`013-menu.html`

```html
<!doctype html>
<html>
	<head>
		
	</head>
	<body>
		<div id="menu">
			<ul>
				<li><a href="inicio.html">Inicio</a></li>
				<li><a href="galeria.html">Galeria</a></li>
				<li><a href="buscar.html">Buscar</a></li>
				<li><a href="tienda.html">Tienda</a></li>
			</ul>
		</div>
	</body>
</html>
```

### menu con emojis
<small>Creado: 2025-10-14 18:35</small>

`014-menu con emojis.html`

```html
<!doctype html>
<html>
	<head>
		
	</head>
	<body>
		<div id="menu">
			<ul>
				<li><a href="inicio.html">🏠</a></li>
				<li><a href="galeria.html">Galeria</a></li>
				<li><a href="buscar.html">Buscar</a></li>
				<li><a href="tienda.html">Tienda</a></li>
			</ul>
		</div>
	</body>
</html>
```

### filtros css
<small>Creado: 2025-10-14 18:35</small>

`015-filtros css.html`

```html
<!doctype html>
<html>
	<head>
		<style>
			a{
				text-decoration:none;
				filter:saturate(0) contrast(500%);
			}
		</style>
	</head>
	<body>
		<div id="menu">
			<ul>
				<li><a href="inicio.html">🏠</a></li>
				<li><a href="galeria.html">📸</a></li>
				<li><a href="buscar.html">🔎</a></li>
				<li><a href="tienda.html">🛒</a></li>
			</ul>
		</div>
	</body>
</html>
```


<a id="interaccion-persona-ordenador"></a>
## Interacción persona-ordenador.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/003-Interacci%C3%B3n%20persona-ordenador.)

### sintesis de voz
<small>Creado: 2025-10-14 18:35</small>

`001-sintesis de voz.html`

```html
<!doctype html>
<html>
  <body>
    <button onclick="speak()">Speak</button>

    <script>
      function speak(){
        const utterance = new SpeechSynthesisUtterance("Hola, esto es una prueba.");
        speechSynthesis.speak(utterance);
      }
    </script>
  </body>
</html>
```

### microfono
<small>Creado: 2025-10-14 18:35</small>

`002-microfono.html`

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <button onclick="startRecognition()">🎤 Start</button>
    <p id="salida"></p>

    <script>
      function startRecognition(){
        // Variable atrapa o bien la capacidad de reconocimiento del navegador
        const reconocimiento = window.SpeechRecognition || window.webkitSpeechRecognition;
        console.log(reconocimiento)
        
        // Crea una nueva instancia de de la variable que hemos atrapado arriba
        const reconocer = new reconocimiento();
        reconocer.lang = "es-ES";         // Propiedad idioma de la libreria
        reconocer.interimResults = false; // Espera al final del audio
        reconocer.maxAlternatives = 1;    // Solo quiero la más parecida

        reconocer.start();                // Método para arrancar el reconocimiento
        
        // Función que se va a ejecutar si el reconocimiento es exitoso
        reconocer.onresult = (event) => {
          // Coge el elemento que tiene el id "salida"
          let salida = document.getElementById("salida");
          // Atrapa el resultado de la transcripción
          console.log(event)
          let transcripcion = event.results[0][0].transcript;
          // Y en el elemento pon el texto
          salida.innerText(transcripcion)
        };
        
        // Función que se va a ejecutar si el reconocimiento da error
        reconocer.onerror = (event) => {
          console.error("Recognition error", event.error);
        };
      }
    </script>
  </body>
</html>
```

### manos
<small>Creado: 2025-10-14 18:35</small>

`003-manos.html`

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>MediaPipe Hands (mínimo)</title>
    <style>
      body { margin: 0; display: grid; place-items: center; height: 100vh; background: #111; }
      #wrap { position: relative; width: 640px; height: 480px; }
      video, canvas { position: absolute; inset: 0; width: 100%; height: 100%; }
      canvas { pointer-events: none; }
    </style>
  </head>
  <body>
    <div id="wrap">
      <video id="video" autoplay playsinline muted></video>
      <canvas id="canvas" width="640" height="480"></canvas>
    </div>

    <!-- MediaPipe Tasks Vision (ESM via CDN) -->
    <script type="module">
      import {
        FilesetResolver,
        HandLandmarker
      } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.9";

      const video = document.getElementById("video");
      const canvas = document.getElementById("canvas");
      const ctx = canvas.getContext("2d");

      // Carga el modelo y empieza la cámara
      const vision = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.9/wasm"
      );

      const handLandmarker = await HandLandmarker.createFromOptions(vision, {
        baseOptions: {
          modelAssetPath:
            "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
        },
        numHands: 2,                // detecta hasta 2 manos
        runningMode: "video"        // modo video (frame-by-frame)
      });

      // Pide la cámara
      const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
      video.srcObject = stream;

      // Dibuja landmarks en cada frame
      function draw(results) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // Dibuja el frame del vídeo
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Dibuja puntos y conexiones de cada mano
        (results.landmarks || []).forEach(landmarks => {
          // Conexiones simples (opcional, solo algunas para mantenerlo mínimo)
          const lines = [
            [0,1],[1,2],[2,3],[3,4],      // pulgar
            [5,6],[6,7],[7,8],            // índice
            [9,10],[10,11],[11,12],       // medio
            [13,14],[14,15],[15,16],      // anular
            [17,18],[18,19],[19,20],      // meñique
            [0,5],[5,9],[9,13],[13,17],[17,0] // palma aproximada
          ];
          ctx.lineWidth = 2;
          ctx.strokeStyle = "lime";
          lines.forEach(([a,b]) => {
            const pa = landmarks[a], pb = landmarks[b];
            ctx.beginPath();
            ctx.moveTo(pa.x * canvas.width, pa.y * canvas.height);
            ctx.lineTo(pb.x * canvas.width, pb.y * canvas.height);
            ctx.stroke();
          });

          // Puntos
          ctx.fillStyle = "deepskyblue";
          landmarks.forEach(p => {
            ctx.beginPath();
            ctx.arc(p.x * canvas.width, p.y * canvas.height, 3, 0, Math.PI * 2);
            ctx.fill();
          });
        });
      }

      // Bucle de inferencia
      function loop() {
        if (video.readyState >= 2) {
          const nowMs = performance.now();
          const results = handLandmarker.detectForVideo(video, nowMs);
          draw(results);
        }
        requestAnimationFrame(loop);
      }

      // Arranca cuando el vídeo está listo
      video.onloadeddata = () => requestAnimationFrame(loop);
    </script>
  </body>
</html>
```

### manos mas simplficadas
<small>Creado: 2025-10-14 18:35</small>

`004.manos mas simplficadas.html`

```html
<!doctype html>
<html>
  <body>
    <video id="video" autoplay playsinline style="display:none"></video>
    <canvas id="canvas" width="640" height="480"></canvas>

    <script type="module">
      import { FilesetResolver, HandLandmarker } 
        from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.9";

      const video = document.getElementById("video");
      const ctx = document.getElementById("canvas").getContext("2d");

      // Cargar modelo
      const vision = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.9/wasm"
      );
      const hand = await HandLandmarker.createFromOptions(vision, {
        baseOptions: {
          modelAssetPath:
            "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
        },
        runningMode: "video"
      });

      // Cámara
      const stream = await navigator.mediaDevices.getUserMedia({video:true});
      video.srcObject = stream;

      // Bucle simple
      function loop() {
        if (video.readyState >= 2) {
          const res = hand.detectForVideo(video, performance.now());
          ctx.drawImage(video,0,0,640,480);
          (res.landmarks||[]).forEach(landmarks=>{
            landmarks.forEach(p=>{
              ctx.fillRect(p.x*640, p.y*480, 5, 5);
            });
          });
        }
        requestAnimationFrame(loop);
      }
      video.onloadeddata = ()=>loop();
    </script>
  </body>
</html>
```

### caras
<small>Creado: 2025-10-14 18:35</small>

`005-caras.html`

```html
<!doctype html>
<html>
  <body>
    <video id="video" autoplay playsinline style="display:none"></video>
    <canvas id="canvas" width="640" height="480"></canvas>

    <script type="module">
      import { FilesetResolver, FaceLandmarker }
        from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.9";

      const video = document.getElementById("video");
      const ctx = document.getElementById("canvas").getContext("2d");

      // Cargar modelo de cara
      const vision = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.9/wasm"
      );
      const face = await FaceLandmarker.createFromOptions(vision, {
        baseOptions: {
          modelAssetPath:
            "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"
        },
        runningMode: "video",
        numFaces: 1
      });

      // Cámara
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      video.srcObject = stream;

      // Bucle mínimo
      function loop() {
        if (video.readyState >= 2) {
          const res = face.detectForVideo(video, performance.now());
          ctx.drawImage(video, 0, 0, 640, 480);
          (res.faceLandmarks || []).forEach(landmarks => {
            landmarks.forEach(p => {
              ctx.fillRect(p.x * 640, p.y * 480, 2, 2); // dibuja puntitos
            });
          });
        }
        requestAnimationFrame(loop);
      }
      video.onloadeddata = () => loop();
    </script>
  </body>
</html>
```

### lienzo
<small>Creado: 2025-10-14 18:35</small>

`006-lienzo.html`

```html
<!doctype html>
<html>
  <body>
    <canvas width=512 height=512></canvas>
  </body>
</html>
```

### contexto
<small>Creado: 2025-10-14 18:35</small>

`007-contexto.html`

```html
<!doctype html>
<html>
  <body>
    <canvas width=512 height=512 id="lienzo"></canvas>
    <script>
      // Primero atrapo al elemento
      const lienzo = document.getElementById("lienzo");
      // Ahora creo un contexto para dibujar
      const contexto = lienzo.getContext("2d");
      
      
    </script>
  </body>
</html>
```

### ahora empiezo a dibujar
<small>Creado: 2025-10-14 18:35</small>

`008-ahora empiezo a dibujar.html`

```html
<!doctype html>
<html>
  <body>
    <canvas width=512 height=512 id="lienzo"></canvas>
    <script>
      // Primero atrapo al elemento
      const lienzo = document.getElementById("lienzo");
      // Ahora creo un contexto para dibujar
      const contexto = lienzo.getContext("2d");
      // Dibujo un rectángulo
      contexto.fillRect(40,40,50,50);
    </script>
  </body>
</html>
```

### ahora un circulo
<small>Creado: 2025-10-14 18:35</small>

`009-ahora un circulo.html`

```html
<!doctype html>
<html>
  <body>
    <canvas width=512 height=512 id="lienzo"></canvas>
    <script>
      // Primero atrapo al elemento
      const lienzo = document.getElementById("lienzo");
      // Ahora creo un contexto para dibujar
      const contexto = lienzo.getContext("2d");
      // Dibujo un rectángulo
      contexto.fillRect(40,40,50,50);
      // Dibujo un circulo
      contexto.beginPath() // Ahora voy a empezar a dibujar
      contexto.arc(
        300,              // Valor de centro x
        300,              // Valor de centro y
        30,               // Radio 30
        0,                // Desde el angulo cero
        Math.PI*2         // Hasta el angulo 360
      )
      contexto.fill()     // Y ahora rellena con color
    </script>
  </body>
</html>
```

### estructura for
<small>Creado: 2025-10-14 18:35</small>

`010-estructura for.html`

```html
<!doctype html>
<html>
  <body>
    <canvas width=512 height=512 id="lienzo"></canvas>
    <script>
      // Primero atrapo al elemento
      const lienzo = document.getElementById("lienzo");
      // Ahora creo un contexto para dibujar
      const contexto = lienzo.getContext("2d");
      // Dibujo un rectángulo
      contexto.fillRect(40,40,50,50);
      const numerocirculos = 400;
      for(let cuentacirculo = 0;cuentacirculo<numerocirculos;cuentacirculo++){
        // Dibujo un circulo
        contexto.beginPath() // Ahora voy a empezar a dibujar
        contexto.arc(
          Math.random()*512,// Valor de centro x
          Math.random()*512,// Valor de centro y
          10,               // Radio 30
          0,                // Desde el angulo cero
          Math.PI*2         // Hasta el angulo 360
        )
        contexto.fill()     // Y ahora rellena con color
      }
    </script>
  </body>
</html>
```

### animacion
<small>Creado: 2025-10-14 18:35</small>

`011-animacion.html`

```html
<!doctype html>
<html>
  <body>
    <canvas width=512 height=512 id="lienzo"></canvas>
    <script>
      // Un temporizador es como un despertador
      var temporizador = setTimeout("bucle()",1000);
      
      // Esta es la función que se va a repetir
      function bucle(){
          // Saca un mensaje por consola
          console.log("Estas dentro del bucle")
          // Apaga el temporizador anterior
          clearTimeout(temporizador)
          // Crea un nuevo temporizador para dentro de un segundo
          temporizador = setTimeout("bucle()",1000);
      }
      
    </script>
  </body>
</html>
```

### contorno del relok
<small>Creado: 2025-10-14 18:35</small>

`012-contorno del relok.html`

```html
<!doctype html>
<html>
  <body>
    <canvas width=512 height=512 id="lienzo"></canvas>
    <script>
      // Un temporizador es como un despertador
      var temporizador = setTimeout("bucle()",1000);
      const lienzo = document.getElementById("lienzo")
      const contexto = lienzo.getContext("2d")
      
      // Esta es la función que se va a repetir
      function bucle(){
          // Creo el contorno del reloj
          contexto.beginPath();
          contexto.arc(
            256,
            256,
            200,
            0,
            Math.PI*2
          )
          contexto.stroke();
          // Ahora dibujo una linea
          contexto.beginPath()          // Empiezo a dibujar
          contexto.moveTo(256,256)      // Muevo el cursor hasta una posicion
          contexto.lineTo(456,256)      // Dibujo una linea
          contexto.stroke()             // Realmente dibujo la linea
          // Apaga el temporizador anterior
          clearTimeout(temporizador)
          // Crea un nuevo temporizador para dentro de un segundo
          temporizador = setTimeout("bucle()",1000);
      }
      
    </script>
  </body>
</html>
```

### muevo el segundero
<small>Creado: 2025-10-14 18:35</small>

`013-muevo el segundero.html`

```html
<!doctype html>
<html>
  <body>
    <canvas width=512 height=512 id="lienzo"></canvas>
    <script>
      // Un temporizador es como un despertador
      var temporizador = setTimeout("bucle()",1000);
      const lienzo = document.getElementById("lienzo")
      const contexto = lienzo.getContext("2d")
      let segundo = 0
      // Esta es la función que se va a repetir
      function bucle(){
          segundo += 0.1
          // Creo el contorno del reloj
          contexto.beginPath();
          contexto.arc(
            256,
            256,
            200,
            0,
            Math.PI*2
          )
          contexto.stroke();
          // Ahora dibujo una linea
          contexto.beginPath()          // Empiezo a dibujar
          contexto.moveTo(256,256)      // Muevo el cursor hasta una posicion
          contexto.lineTo(
            256+Math.cos(segundo)*200,
            256+Math.sin(segundo)*200
            )
          contexto.stroke()             // Realmente dibujo la linea
          // Apaga el temporizador anterior
          clearTimeout(temporizador)
          // Crea un nuevo temporizador para dentro de un segundo
          temporizador = setTimeout("bucle()",10);
      }
      
    </script>
  </body>
</html>
```


<a id="interpretacion-de-guias-de-estilo-elementos"></a>
## Interpretación de guías de estilo. Elementos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/004-Interpretaci%C3%B3n%20de%20gu%C3%ADas%20de%20estilo.%20Elementos.)

### inicio del manual
<small>Creado: 2025-10-14 18:35</small>

`001-inicio del manual.html`

```html
<html>
	<head>
		
	</head>
	<body>
		<section id="Portada"></section>
		<section id="Índice"></section>
		<section id="Manifiesto - Misión, visión, valores"></section>
<section id="Esquema de trazado del logo con rejilla"></section>
<section id="Simbolo como textura corporativa (poco frecuente)"></section>
<section id="Trazado del texto"></section>
<section id="Familias de fuentes a utilizar"></section>
<section id="Colores corporativos (primario y secundario)"></section>
<section id="Margenes (concepto es muy similar al padding)"></section>
<section id="Versión negativa"></section>
<section id="Variaciones de color permitidas"></section>
<section id="Aplicaciones (cartelería, papelería, etc)"></section>
<section id="Tamaño mínimo y máximo"></section>
	</body>
</html>
```


<a id="generacion-de-documentos-y-sitios-web"></a>
## Generación de documentos y sitios web.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/005-Generaci%C3%B3n%20de%20documentos%20y%20sitios%20web.)

### cliente
<small>Creado: 2025-10-14 18:35</small>

`002-cliente.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <main>
      <table>
        <tr>
          <td>Nombre</td>
          <td id="nombre"></td>
        </tr>
        <tr>
          <td>Apellidos</td>
          <td id="apellidos"></td>
        </tr>
        <tr>
          <td>Email</td>
          <td id="email"></td>
        </tr>
      </table>
    </main>
  </body>
</html>
```

### estilo
<small>Creado: 2025-10-14 18:35</small>

`003-estilo.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      body{background:grey;}
      main{background:white;width:300px;height:300px;padding:20px;margin:auto;}
    </style>
  </head>
  <body>
    <main>
      <table>
        <tr>
          <td>Nombre</td>
          <td id="nombre"></td>
        </tr>
        <tr>
          <td>Apellidos</td>
          <td id="apellidos"></td>
        </tr>
        <tr>
          <td>Email</td>
          <td id="email"></td>
        </tr>
      </table>
    </main>
  </body>
</html>
```

### comportamiento
<small>Creado: 2025-10-14 18:35</small>

`004-comportamiento.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      body{background:grey;}
      main{background:white;width:300px;height:300px;padding:20px;margin:auto;}
    </style>
  </head>
  <body>
    <main>
      <table>
        <tr>
          <td>Nombre</td>
          <td id="nombre"></td>
        </tr>
        <tr>
          <td>Apellidos</td>
          <td id="apellidos"></td>
        </tr>
        <tr>
          <td>Email</td>
          <td id="email"></td>
        </tr>
      </table>
    </main>
    <script>
      fetch("cliente.json")       // Ves y busca un archivo
      .then(function(response){   // Y cuando lo encuentres
        return response.json()    // Interpretalo como json
      })
      .then(function(datos){      // Y entonces ahora
        console.log(datos)        // Enseñame los datos en la consola
      })
    </script>
  </body>
</html>
```

### datos
<small>Creado: 2025-10-14 18:35</small>

`005-datos.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      body{background:grey;}
      main{background:white;width:300px;height:300px;padding:20px;margin:auto;}
    </style>
  </head>
  <body>
    <main>
      <table>
        <tr>
          <td>Nombre</td>
          <td id="nombre"></td>
        </tr>
        <tr>
          <td>Apellidos</td>
          <td id="apellidos"></td>
        </tr>
        <tr>
          <td>Email</td>
          <td id="email"></td>
        </tr>
      </table>
    </main>
    <script>
      fetch("cliente.json")       // Ves y busca un archivo
      .then(function(response){   // Y cuando lo encuentres
        return response.json()    // Interpretalo como json
      })
      .then(function(datos){      // Y entonces ahora
        console.log(datos)        // Enseñame los datos en la consola
        
        // Ves y busca el elemento que tiene el id nombre
        // Y cuando lo encuentres, su texto es el dato que viene del json "nombre"
        document.querySelector("#nombre").textContent = datos.nombre
        
        document.querySelector("#apellidos").textContent = datos.apellidos
        document.querySelector("#email").textContent = datos.email
      })
    </script>
  </body>
</html>
```

### web clasica
<small>Creado: 2025-10-14 18:35</small>

`006-web clasica.html`

```html
<!doctype html>
<html>
  <head>
    
  </head>
  <body>
    <h1>La web de Jose Vicente</h1>
  </body>
</html>
```

### web plantilla
<small>Creado: 2025-10-14 18:35</small>

`007-web plantilla.html`

```html
<!doctype html>
<html>
  <head>
    <style>
    body,html{height:100%;}
    body{
      display:flex;
      flex-direction:column;
      justify-content: space-between;
    }
    </style>
  </head>
  <body>
    <header>
      <h1>{titulo}</h1>
    </header>
    <main>
      {contenido}
    </main>
    <footer>
      {piedepagina}
    </footer>
  </body>
</html>
```

### cliente
<small>Creado: 2025-10-14 18:35</small>

`cliente.json`

```json
{
  "nombre":"Jose Vicente",
  "apellidos":"Carratala Sanchis",
  "email":"info@jocarsa.com"
}
```


<a id="componentes-de-una-interfaz-web"></a>
## Componentes de una interfaz web.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/006-Componentes%20de%20una%20interfaz%20web.)

### tipos de campos
<small>Creado: 2025-10-14 18:35</small>

`002-tipos de campos.html`

```html
<form action="?" method="POST">
  <input type="date">
  <input type="time">
  <input type="color">
  <input type="range">
  <input type="range" min=1 max=10 step=1>
  <input type="email">
  <input type="number">
  <input type="submit">
</form>
```

### validacion
<small>Creado: 2025-10-14 18:35</small>

`003-validacion.html`

```html
<input type="text" class="dni" maxlength=9>
<script>
  // Que cumpla con los parametros numéricos
  // Un DNI tiene 8 numeros y una letra - y la letra se calcula mediante un algoritmo
  
  // Selecciono el elemento cuya clase es DNI, y cuando salga de ese campo
  document.querySelector(".dni").onblur = function(){
    let contenido = this.value; // El contenido es el valor del elemento atrapado
    let caracter1 = contenido[0];
    let caracter2 = contenido[1];
    let caracter3 = contenido[2];
    let caracter4 = contenido[3];
    let caracter5 = contenido[4];
    let caracter6 = contenido[5];
    let caracter7 = contenido[6];
    let caracter8 = contenido[7];
    let caracter9 = contenido[8];
    
    let numeros = "0123456789";
    let dni = true;
    
    // Primero repaso el contenido del caracter 1 /////////////////////////////////////////////////////////
    dni = false
    for(let i = 0;i<10;i++){
      // Para cada uno de los numero comparo si el numero es igual al caracter
      if(caracter1 == numeros[i]){
        // Si es igual, saco mensaje
        console.log("El caracter 1 si que es un numero")
        dni = true;
      }
    }
    // Primero repaso el contenido del caracter 2 /////////////////////////////////////////////////////////
    dni = false
    for(let i = 0;i<10;i++){
      // Para cada uno de los numero comparo si el numero es igual al caracter
      if(caracter2 == numeros[i]){
        // Si es igual, saco mensaje
        console.log("El caracter 1 si que es un numero")
        dni = true;
      }
    }
    // Primero repaso el contenido del caracter 3 /////////////////////////////////////////////////////////
    dni = false
    for(let i = 0;i<10;i++){
      // Para cada uno de los numero comparo si el numero es igual al caracter
      if(caracter3 == numeros[i]){
        // Si es igual, saco mensaje
        console.log("El caracter 1 si que es un numero")
        dni = true;
      }
    }
    // Primero repaso el contenido del caracter 4 /////////////////////////////////////////////////////////
    dni = false
    for(let i = 0;i<10;i++){
      // Para cada uno de los numero comparo si el numero es igual al caracter
      if(caracter4 == numeros[i]){
        // Si es igual, saco mensaje
        console.log("El caracter 1 si que es un numero")
        dni = true;
      }
    }
    // Primero repaso el contenido del caracter 5 /////////////////////////////////////////////////////////
    dni = false
    for(let i = 0;i<10;i++){
      // Para cada uno de los numero comparo si el numero es igual al caracter
      if(caracter5 == numeros[i]){
        // Si es igual, saco mensaje
        console.log("El caracter 1 si que es un numero")
        dni = true;
      }
    }
    // Primero repaso el contenido del caracter 6 /////////////////////////////////////////////////////////
    dni = false
    for(let i = 0;i<10;i++){
      // Para cada uno de los numero comparo si el numero es igual al caracter
      if(caracter6 == numeros[i]){
        // Si es igual, saco mensaje
        console.log("El caracter 1 si que es un numero")
        dni = true;
      }
    }
    // Primero repaso el contenido del caracter 7 /////////////////////////////////////////////////////////
    dni = false
    for(let i = 0;i<10;i++){
      // Para cada uno de los numero comparo si el numero es igual al caracter
      if(caracter7 == numeros[i]){
        // Si es igual, saco mensaje
        console.log("El caracter 1 si que es un numero")
        dni = true;
      }
    }
    // Primero repaso el contenido del caracter 8 /////////////////////////////////////////////////////////
    dni = false
    for(let i = 0;i<10;i++){
      // Para cada uno de los numero comparo si el numero es igual al caracter
      if(caracter8 == numeros[i]){
        // Si es igual, saco mensaje
        console.log("El caracter 1 si que es un numero")
        dni = true;
      }
    }
    
    
    
    if(dni == true){
      alert("Lo que has introducido es un DNI valido")
    }else{
      alert("lo que has introducido no es un DNI")
    }
  }
  
</script>
```

### validacion por expresion regular
<small>Creado: 2025-10-14 18:35</small>

`004-validacion por expresion regular.html`

```html
<input type="text" class="dni" maxlength=9>
<script>
  // Que cumpla con los parametros numéricos
  // Un DNI tiene 8 numeros y una letra - y la letra se calcula mediante un algoritmo
  
  // Selecciono el elemento cuya clase es DNI, y cuando salga de ese campo
  document.querySelector(".dni").onblur = function(){
    let contenido = this.value; // El contenido es el valor del elemento atrapado
    const regexp = /^[0-9]{8}[A-Z]$/;
    if(regexp.test(contenido)){
      this.style.border = "1px solid green"
    }else{
      this.style.border = "1px solid red"
    }
  }
  
</script>
```

### micomponente
<small>Creado: 2025-10-14 18:35</small>

`006-micomponente.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body> 
    <input class="dni" type="text">
    <script src="https://jocarsa.github.io/validardni/validardni.js"></script>
  </body>
</html>
```

### validar dos decimales
<small>Creado: 2025-10-14 18:35</small>

`007-validar dos decimales.html`

```html
<input type="text" class="dni" maxlength=9>
<script>
  // Que cumpla con los parametros numéricos
  // Un DNI tiene 8 numeros y una letra - y la letra se calcula mediante un algoritmo
  
  // Selecciono el elemento cuya clase es DNI, y cuando salga de ese campo
  document.querySelector(".dni").onblur = function(){
    let contenido = this.value; // El contenido es el valor del elemento atrapado
    const regexp = /^[0-9]+(,[0-9]{1,2})?$/;
    if(regexp.test(contenido)){
      this.style.border = "1px solid green"
    }else{
      this.style.border = "1px solid red"
    }
  }
  
</script>
```

### inserto
<small>Creado: 2025-10-14 18:35</small>

`008-inserto.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body> 
    <input class="numerodecimalcoma" type="text">
    <script src="https://jocarsa.github.io/validarnumerocoma/validarnumerocoma.js"></script>
  </body>
</html>
```

### y tambien inserto estilo
<small>Creado: 2025-10-14 18:35</small>

`009-y tambien inserto estilo.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body> 
    <input class="numerodecimalcoma" type="text">
    
    
    <script src="https://jocarsa.github.io/validarnumerocoma/validarnumerocoma.js"></script>
    <link rel="stylesheet" href="https://jocarsa.github.io/validarnumerocoma/validarnumerocoma.css">
  </body>
</html>
```


<a id="tecnologias-para-el-diseno-de-documentos-web"></a>
## Tecnologías para el diseño de documentos web.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/007-Tecnolog%C3%ADas%20para%20el%20dise%C3%B1o%20de%20documentos%20web.)

### inicio
<small>Creado: 2025-10-14 18:35</small>

`001-inicio.php`

```
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <?php
      echo "Hola"
    ?>
  </body>
</html>
```

### for para html
<small>Creado: 2025-10-14 18:35</small>

`002-for para html.php`

```
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <table>
    <tr>
    <?php
      for($dia = 1;$dia<31;$dia++){
        echo "<th>".$dia."</th>";
      }
    ?>
    </tr>
    </table>
  </body>
</html>
```

### contenido para el cuerpo de la tabla
<small>Creado: 2025-10-14 18:35</small>

`003-contenido para el cuerpo de la tabla.php`

```
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <table>
    <tr>
    <?php
      for($dia = 1;$dia<31;$dia++){
        echo "<th>".$dia."</th>";
      }
    ?>
    </tr>
    <?php
      for($fila = 1;$fila<20;$fila++){
    ?>
      <tr>
        <?php
        for($dia = 1;$dia<31;$dia++){
          echo "<td>".rand(1,10000)."</td>";
        }
      ?>
    </tr>
    <?php } ?>
    </table>
  </body>
</html>
```

### ahora con objeto
<small>Creado: 2025-10-14 18:35</small>

`004-ahora con objeto.php`

```
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <?php
      $cliente = [
        "id" => 101,
        "nombre" => "María López García",
        "dni" => "12345678Z",
        "email" => "maria.lopez@example.com",
        "telefono" => "+34 600 123 456",
        "calle" => "Calle Mayor, 45",
        "ciudad" => "Valencia",
        "provincia" => "Valencia",
        "codigo_postal" => "46001",
        "pais" => "España",
        "empresa_nombre" => "López Consultores S.L.",
        "empresa_cif" => "B12345678",
        "empresa_direccion" => "Av. del Puerto, 123",
        "empresa_actividad" => "Consultoría empresarial",
        "fecha_alta" => "2024-09-15",
        "activo" => true
      ];
      
      echo $cliente['id'];
      echo $cliente['nombre'];
      
    ?> 
  </body>
</html>
```

### recorrer objeto
<small>Creado: 2025-10-14 18:35</small>

`005-recorrer objeto.php`

```
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <?php
      $cliente = [
        "id" => 101,
        "nombre" => "María López García",
        "dni" => "12345678Z",
        "email" => "maria.lopez@example.com",
        "telefono" => "+34 600 123 456",
        "calle" => "Calle Mayor, 45",
        "ciudad" => "Valencia",
        "provincia" => "Valencia",
        "codigo_postal" => "46001",
        "pais" => "España",
        "empresa_nombre" => "López Consultores S.L.",
        "empresa_cif" => "B12345678",
        "empresa_direccion" => "Av. del Puerto, 123",
        "empresa_actividad" => "Consultoría empresarial",
        "fecha_alta" => "2024-09-15",
        "activo" => true
      ];
      
      $claves = array_keys($cliente);
      //var_dump($claves);
      
    ?> 
    <table>
      <thead>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<th>".$clave."</th>
          ";
            }
          ?>
        </tr>
      </thead>
      <tbody>
      
      </tbody>
    </table>
  </body>
</html>
```

### ahora dibujo el cuerpo
<small>Creado: 2025-10-14 18:35</small>

`006-ahora dibujo el cuerpo.php`

```
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <?php
      $cliente = [
        "id" => 101,
        "nombre" => "María López García",
        "dni" => "12345678Z",
        "email" => "maria.lopez@example.com",
        "telefono" => "+34 600 123 456",
        "calle" => "Calle Mayor, 45",
        "ciudad" => "Valencia"
      ];
      
      $claves = array_keys($cliente);
      //var_dump($claves);
      
    ?> 
    <table>
      <thead>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<th>".$clave."</th>
          ";
            }
          ?>
        </tr>
      </thead>
      <tbody>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<td>".$valor."</td>
          ";
            }
          ?>
        </tr>
      </tbody>
    </table>
  </body>
</html>
```

### formulario
<small>Creado: 2025-10-14 18:35</small>

`007-formulario.php`

```
<!doctype html>
<html>
  <head>
    <title>CRUD</title>
    <!--
      Create = Formulario
      Read = Tabla
      Update = Boton + formulario
      Delete = Boton
    -->
  </head>
  <body>
    <?php
      $cliente = [
        "id" => 101,
        "nombre" => "María López García",
        "dni" => "12345678Z",
        "email" => "maria.lopez@example.com",
        "telefono" => "+34 600 123 456",
        "calle" => "Calle Mayor, 45",
        "ciudad" => "Valencia",
        "profesion" => "Médico"
      ];
      
      $claves = array_keys($cliente);
      //var_dump($claves);
      
    ?> 
    <table>
      <thead>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<th>".$clave."</th>
          ";
            }
          ?>
        </tr>
      </thead>
      <tbody>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<td>".$valor."</td>
          ";
            }
          ?>
        </tr>
      </tbody>
    </table>
    <form action="?" method="POST">
      <?php
        foreach ($cliente as $clave => $valor) {
            echo "<input type='text' placeholder='".$clave."'>
      ";
        }
      ?>
    </form>
  </body>
</html>
```

### vista
<small>Creado: 2025-10-14 18:40</small>

`008-vista.html`

```html
<!doctype html>
<html>
  <head>
    <title>CRUD</title>
    <!--
      Create = Formulario
      Read = Tabla
      Update = Boton + formulario
      Delete = Boton
    -->
  </head>
  <body>
    <form action="011-libreriafechas.php" method="POST">
      <input type="text" name="nombre" placeholder="Nombre del cliente">
      <input type="text" name="apellidos" placeholder="Apellidos del cliente">
      <input type="text" name="email" placeholder="Email del cliente">
      <input type="text" name="direccion" placeholder="Direccion del cliente">
      <input type="text" name="ciudad" placeholder="Ciudad del cliente">
      <input type="submit">
    </form>
  </body>
</html>
```

### procesa
<small>Creado: 2025-10-14 18:35</small>

`009-procesa.php`

```
<?php
  // Defino el nombre en el que voy a guardar el archivo
  $filename = 'data.json';
  // Codifica un array PHP a un objeto JSON
  $jsonData = json_encode($_POST, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
  // Este comando realmente guarda el archivo en el disco duro
  file_put_contents($filename, $jsonData);

?>
```

### procesadinamico
<small>Creado: 2025-10-14 18:35</small>

`010-procesadinamico.php`

```
<?php
  // Defino el nombre en el que voy a guardar el archivo
  $filename = 'basededatos/'.date('U').'.json';
  // Codifica un array PHP a un objeto JSON
  $jsonData = json_encode($_POST, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
  // Este comando realmente guarda el archivo en el disco duro
  file_put_contents($filename, $jsonData);

?>
```

### libreriafechas
<small>Creado: 2025-10-14 18:39</small>

`011-libreriafechas.php`

```
<?php
  // Defino el nombre en el que voy a guardar el archivo
  $filename = 'basededatos/'.date('Y').'-'.date('m').'-'.date('d').'-'.date('H').'-'.date('i').'-'.date('s').'.json';
  // Codifica un array PHP a un objeto JSON
  $jsonData = json_encode($_POST, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
  // Este comando realmente guarda el archivo en el disco duro
  file_put_contents($filename, $jsonData);

?>
```

### continuamos el anterior
<small>Creado: 2025-10-14 18:43</small>

`012-continuamos el anterior.php`

```
<!doctype html>
<html>
  <head>
    <title>CRUD</title>
    <!--
      Create = Formulario
      Read = Tabla
      Update = Boton + formulario
      Delete = Boton
    -->
  </head>
  <body>
    <?php
      $cliente = [
        "id" => 101,
        "nombre" => "María López García",
        "dni" => "12345678Z",
        "email" => "maria.lopez@example.com",
        "telefono" => "+34 600 123 456",
        "calle" => "Calle Mayor, 45",
        "ciudad" => "Valencia",
        "profesion" => "Médico"
      ];
      
      $claves = array_keys($cliente);
      //var_dump($claves);
      
    ?> 
    <table>
      <thead>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<th>".$clave."</th>
          ";
            }
          ?>
        </tr>
      </thead>
      <tbody>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<td>".$valor."</td>
          ";
            }
          ?>
        </tr>
      </tbody>
    </table>
    <form action="?" method="POST">
      <?php
        foreach ($cliente as $clave => $valor) {
            echo "<input type='text' placeholder='".$clave."'><br>
      ";
        }
      ?>
      <input type="submit">
    </form>
  </body>
</html>
```

### reutilizamos el procesa
<small>Creado: 2025-10-14 18:46</small>

`013-reutilizamos el procesa.php`

```
<!doctype html>
<html>
  <head>
    <title>CRUD</title>
    <!--
      Create = Formulario
      Read = Tabla
      Update = Boton + formulario
      Delete = Boton
    -->
  </head>
  <body>
    <?php
      $cliente = [
        "id" => 101,
        "nombre" => "María López García",
        "dni" => "12345678Z",
        "email" => "maria.lopez@example.com",
        "telefono" => "+34 600 123 456",
        "calle" => "Calle Mayor, 45",
        "ciudad" => "Valencia",
        "profesion" => "Médico"
      ];
      
      $claves = array_keys($cliente);
      //var_dump($claves);
      
    ?> 
    <table>
      <thead>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<th>".$clave."</th>
          ";
            }
          ?>
        </tr>
      </thead>
      <tbody>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<td>".$valor."</td>
          ";
            }
          ?>
        </tr>
      </tbody>
    </table>
    <form action="014-guardamos.php" method="POST">
      <?php
        foreach ($cliente as $clave => $valor) {
            echo "<input 
              type='text' 
              placeholder='".$clave."' 
              name='".$clave."' 
              '><br>
      ";
        }
      ?>
      <input type="submit">
    </form>
  </body>
</html>
```

### guardamos
<small>Creado: 2025-10-14 18:46</small>

`014-guardamos.php`

```
<?php
  // Defino el nombre en el que voy a guardar el archivo
  $filename = 'basededatos/'.date('U').'.json';
  // Codifica un array PHP a un objeto JSON
  $jsonData = json_encode($_POST, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
  // Este comando realmente guarda el archivo en el disco duro
  file_put_contents($filename, $jsonData);

?>
```

### json multiple
<small>Creado: 2025-10-14 18:52</small>

`015-json multiple.php`

```
<!doctype html>
<html>
  <head>
    <title>CRUD</title>
    <!--
      Create = Formulario
      Read = Tabla
      Update = Boton + formulario
      Delete = Boton
    -->
  </head>
  <body>
    <?php
      $cliente = [
        "id" => 101,
        "nombre" => "María López García",
        "dni" => "12345678Z",
        "email" => "maria.lopez@example.com",
        "telefono" => "+34 600 123 456",
        "calle" => "Calle Mayor, 45",
        "ciudad" => "Valencia",
        "profesion" => "Médico"
      ];
      
      $claves = array_keys($cliente);
      //var_dump($claves);
      
    ?> 
    <table>
      <thead>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<th>".$clave."</th>
          ";
            }
          ?>
        </tr>
      </thead>
      <tbody>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<td>".$valor."</td>
          ";
            }
          ?>
        </tr>
      </tbody>
    </table>
    <form action="016-guardamos.php" method="POST">
      <?php
        foreach ($cliente as $clave => $valor) {
            echo "<input 
              type='text' 
              placeholder='".$clave."' 
              name='".$clave."' 
              '><br>
      ";
        }
      ?>
      <input type="submit">
    </form>
  </body>
</html>
```

### guardamos
<small>Creado: 2025-10-14 18:57</small>

`016-guardamos.php`

```
<?php
  $f='basededatos/basededatos.json';
  $d=file_exists($f)?json_decode(file_get_contents($f),true):[];
  $d[]=$_POST;
  file_put_contents($f,json_encode($d,JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE));
?>
```

### data
<small>Creado: 2025-10-14 18:35</small>

`data.json`

```json
{
    "nombre": "Jose \"Vicente\"",
    "apellidos": "gsdf",
    "email": "sdfg",
    "direccion": "sdfg",
    "ciudad": "sdfg"
}
```


<a id="mapa-de-navegacion-prototipos"></a>
## Mapa de navegación. Prototipos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/008-Mapa%20de%20navegaci%C3%B3n.%20Prototipos.)


<a id="maquetacion-web-elementos-de-ordenacion"></a>
## Maquetación web. Elementos de ordenación.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/009-Maquetaci%C3%B3n%20web.%20Elementos%20de%20ordenaci%C3%B3n.)

### front
<small>Creado: 2025-10-15 17:08</small>

`001-front.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSApress</title>
    <meta charset="utf-8">
  </head>
  <body>
    <header>
    </header>
    <main>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

### back
<small>Creado: 2025-10-15 17:27</small>

`002-back.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSApress</title>
    <meta charset="utf-8">
    <style>
      html,body{width:100%;height:100%;overflow:hidden;padding:0px;margin:0px;}
      body{display:flex;flex-direction:column;font-family:sans-serif;}
      header{flex:1;background:SteelBlue;}
      main{flex:9;display:flex;flex-direction:row;}
      nav{background:SteelBlue;flex:1;display:flex;flex-direction:column;padding:10px;gap:10px;}
      section{flex:6;}
      nav a{background:white;color:SteelBlue;padding:10px;border-radius:5px;text-decoration:none;}
    </style>
  </head>
  <body>
    <header>
    </header>
    <main>
      <nav>
        <a href="">Entradas</a>
        <a href="">Páginas</a>
        <a href="">...</a>
      </nav>
      <section>
      </section>
    </main>
  </body>
</html> 
```

### back con contenido
<small>Creado: 2025-10-15 17:34</small>

`003-back con contenido.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSApress</title>
    <meta charset="utf-8">
    <style>
      html,body{width:100%;height:100%;overflow:hidden;padding:0px;margin:0px;}
      body{display:flex;flex-direction:column;font-family:sans-serif;}
      header{flex:1;background:SteelBlue;}
      main{flex:9;display:flex;flex-direction:row;}
      nav{background:SteelBlue;flex:1;display:flex;flex-direction:column;padding:10px;gap:10px;}
      section{flex:6;padding:10px;}
      nav a{background:white;color:SteelBlue;padding:10px;border-radius:5px;text-decoration:none;}
      button{background:steelblue;color:white;padding:10px 20px;border:none;border-radius:5px;margin:5px;}
      table{width:100%;border-collapse: collapse;}
      table thead tr{background:steelblue;color:white;}
    </style>
  </head>
  <body>
    <header>
    </header>
    <main>
      <nav>
        <a href="">Entradas</a>
        <a href="">Páginas</a>
        <a href="">...</a>
      </nav>
      <section>
        <button>Nuevo</button>
        <table>
          <thead>
            <tr><th>Fecha</th><th>Titulo</th><th>Autor</th><th>Acciones</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
            <tr>
              <td>2025-10-15</td>
              <td>Título del artículo</td>
              <td>Jose Vicente</td>
              <td>🖋❌</td>
            </tr>
          </tbody>
        </table>
      </section>
    </main>
  </body>
</html> 
```

### front con contenido
<small>Creado: 2025-10-15 18:15</small>

`004-front con contenido.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSApress</title>
    <meta charset="utf-8">
    <style>
      html,body{width:100%;padding:0px;margin:0px;font-family:sans-serif;background:steelblue;}
      header,footer,main{background:white;padding:20px;width:600px;margin:auto;}
      article{border-bottom:1px solid steelblue;padding:20px;}
      article *{padding:5px;margin:0px;}
    </style>
  </head>
  <body>
    <header>
      <h1>El blog de José Vicente</h1>
    </header>
    <main>
      <article> 
        <h3>Título del artículo</h3>
        <time>2025-10-15</time>
        <p>Texto del artículo</p>
      </article>
      <article> 
        <h3>Título del artículo</h3>
        <time>2025-10-15</time>
        <p>Texto del artículo</p>
      </article>
      <article> 
        <h3>Título del artículo</h3>
        <time>2025-10-15</time>
        <p>Texto del artículo</p>
      </article>
      <article> 
        <h3>Título del artículo</h3>
        <time>2025-10-15</time>
        <p>Texto del artículo</p>
      </article>
      <article> 
        <h3>Título del artículo</h3>
        <time>2025-10-15</time>
        <p>Texto del artículo</p>
      </article>
      <article> 
        <h3>Título del artículo</h3>
        <time>2025-10-15</time>
        <p>Texto del artículo</p>
      </article>
    </main>
    <footer>
    </footer>
  </body>
</html>
```


<a id="plantilla-de-diseno"></a>
## Plantilla de diseño.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/010-Plantilla%20de%20dise%C3%B1o.)

### introduccion
<small>Creado: 2025-10-21 16:58</small>

`001-introduccion.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
  </head>
  <body>
    
    
  </body>
</html>
```

### template
<small>Creado: 2025-10-21 16:59</small>

`002-template.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
  </head>
  <body>
    
    <template id="elementomenu">
      <button>
        <span>L</span>
        Letra
      </button>
    </template>
  </body>
</html>
```

### contenedor
<small>Creado: 2025-10-21 17:01</small>

`003-contenedor.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
  </head>
  <body>
    <nav>
    </nav>
    <template id="elementomenu">
      <button>
        <span>L</span>
        Letra
      </button>
    </template>
    <script>
      
    </script>
  </body>
</html>
```

### empiezo
<small>Creado: 2025-10-21 17:05</small>

`004-empiezo.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
  </head>
  <body>
    <nav>
    </nav>
    <template id="elementomenu">
      <button>
        <span>L</span>
        Letra
      </button>
    </template>
    <script>
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      let clon = plantilla.content.cloneNode(true);             // Clon en memoria
      contenedor.appendChild(clon);                             // Pongo la plantilla en c
    </script>
  </body>
</html>
```

### un poco de estilo
<small>Creado: 2025-10-21 17:08</small>

`005-un poco de estilo.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <style>
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:100px;color:white;text-align:left;
      }
      button span{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;
      }
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <template id="elementomenu">
      <button>
        <span>L</span>
        Letra
      </button>
    </template>
    <script>
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      let clon = plantilla.content.cloneNode(true);             // Clon en memoria
      contenedor.appendChild(clon);                             // Pongo la plantilla en c
    </script>
  </body>
</html>
```

### muchos clones
<small>Creado: 2025-10-21 17:17</small>

`006-muchos clones.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <style>
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:100px;color:white;text-align:left;
      }
      button span{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;
      }
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <template id="elementomenu">
      <button>
        <span>L</span>
        Letra
      </button>
    </template>
    
    <script>
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<10;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
    </script>
  </body>
</html>
```

### modifico plantilla
<small>Creado: 2025-10-21 17:18</small>

`007-modifico plantilla.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <style>
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:100px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;
      }
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <script>
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<10;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
    </script>
  </body>
</html>
```

### elementos del menu
<small>Creado: 2025-10-21 17:25</small>

`008-elementos del menu.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <style>
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:100px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;
      }
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <script>
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        clon.querySelector(".texto").textContent = elementosmenu[i]
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
    </script>
  </body>
</html>
```

### inicial
<small>Creado: 2025-10-21 17:28</small>

`009-inicial.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <style>
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:100px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <script>
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
    </script>
  </body>
</html>
```

### estilo interfaz
<small>Creado: 2025-10-21 17:35</small>

`010-estilo interfaz.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:lightblue;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <script>
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
    </script>
  </body>
</html>
```

### segundo template
<small>Creado: 2025-10-21 18:17</small>

`011-segundo template.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:lightblue;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <header>
        Cabecera de prueba
      </header>
      <section>
        Contenido de prueba
      </section>
    </template>
    
    <script>
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
    </script>
  </body>
</html>
```

### bloque javascript
<small>Creado: 2025-10-21 18:24</small>

`012-bloque javascript.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:lightblue;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <header>
        Cabecera de prueba
      </header>
      <section>
        Contenido de prueba
      </section>
    </template>
    
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      let clontarjeta = plantillatarjeta.content.cloneNode(true);
      
      contenedortarjetas.appendChild(clontarjeta)
      
      
    </script>
  </body>
</html>
```

### estilo grid
<small>Creado: 2025-10-21 18:37</small>

`013-estilo grid.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:lightblue;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;}
      .tarjeta header{background:lightgrey;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      let clontarjeta = plantillatarjeta.content.cloneNode(true);
      
      contenedortarjetas.appendChild(clontarjeta)
      
      
    </script>
  </body>
</html>
```

### muchas tarjetas
<small>Creado: 2025-10-21 18:38</small>

`014-muchas tarjetas.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:lightblue;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;}
      .tarjeta header{background:lightgrey;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<10;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### tarjetas json
<small>Creado: 2025-10-21 18:43</small>

`015-tarjetas json.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:lightblue;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;}
      .tarjeta header{background:lightgrey;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 4","texto":"texto 4","rowspan":"1","colspan":"1"}
      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<10;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### contenido json
<small>Creado: 2025-10-21 18:46</small>

`016-contenido json.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:lightblue;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;}
      .tarjeta header{background:lightgrey;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 4","texto":"texto 4","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 5","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 6","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 7","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 8","texto":"texto 4","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 9","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 10","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 11","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 12","texto":"texto 4","rowspan":"1","colspan":"1"}
      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<tarjetas.length;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
        clontarjeta.querySelector("section").textContent = tarjetas[i].texto
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### magia negra
<small>Creado: 2025-10-21 18:50</small>

`017-magia negra.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:lightblue;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;}
      .tarjeta header{background:lightgrey;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 4","texto":"texto 4","rowspan":"2","colspan":"1"},
        {"titulo":"Titulo 5","texto":"texto 1","rowspan":"2","colspan":"2"},
        {"titulo":"Titulo 6","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 7","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 8","texto":"texto 4","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 9","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 10","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 11","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 12","texto":"texto 4","rowspan":"1","colspan":"1"}
      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<tarjetas.length;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
        clontarjeta.querySelector("section").textContent = tarjetas[i].texto
        clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
        clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### estilo final
<small>Creado: 2025-10-21 18:58</small>

`018-estilo final.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 4","texto":"texto 4","rowspan":"2","colspan":"1"},
        {"titulo":"Titulo 5","texto":"texto 1","rowspan":"2","colspan":"2"},
        {"titulo":"Titulo 6","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 7","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 8","texto":"texto 4","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 9","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 10","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 11","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 12","texto":"texto 4","rowspan":"1","colspan":"1"}
      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<tarjetas.length;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
        clontarjeta.querySelector("section").textContent = tarjetas[i].texto
        clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
        clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### creo un boton
<small>Creado: 2025-10-22 16:58</small>

`019-creo un boton.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        alert("Vamos a crear uno nuevo")
      }
      contenedor.appendChild(boton_nuevo);
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 4","texto":"texto 4","rowspan":"2","colspan":"1"},
        {"titulo":"Titulo 5","texto":"texto 1","rowspan":"2","colspan":"2"},
        {"titulo":"Titulo 6","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 7","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 8","texto":"texto 4","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 9","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 10","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 11","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 12","texto":"texto 4","rowspan":"1","colspan":"1"}
      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<tarjetas.length;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
        clontarjeta.querySelector("section").textContent = tarjetas[i].texto
        clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
        clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### crear un modal
<small>Creado: 2025-10-22 17:04</small>

`020-crear un modal.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        alert("Vamos a crear uno nuevo")
      }
      contenedor.appendChild(boton_nuevo);
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 4","texto":"texto 4","rowspan":"2","colspan":"1"},
        {"titulo":"Titulo 5","texto":"texto 1","rowspan":"2","colspan":"2"},
        {"titulo":"Titulo 6","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 7","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 8","texto":"texto 4","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 9","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 10","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 11","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 12","texto":"texto 4","rowspan":"1","colspan":"1"}
      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<tarjetas.length;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
        clontarjeta.querySelector("section").textContent = tarjetas[i].texto
        clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
        clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### contenido del modal
<small>Creado: 2025-10-22 17:16</small>

`021-contenido del modal.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        alert("Vamos a crear uno nuevo")
      }
      contenedor.appendChild(boton_nuevo);
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 4","texto":"texto 4","rowspan":"2","colspan":"1"},
        {"titulo":"Titulo 5","texto":"texto 1","rowspan":"2","colspan":"2"},
        {"titulo":"Titulo 6","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 7","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 8","texto":"texto 4","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 9","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 10","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 11","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 12","texto":"texto 4","rowspan":"1","colspan":"1"}
      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<tarjetas.length;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
        clontarjeta.querySelector("section").textContent = tarjetas[i].texto
        clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
        clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### escondo el modal
<small>Creado: 2025-10-22 17:21</small>

`022-escondo el modal.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 4","texto":"texto 4","rowspan":"2","colspan":"1"},
        {"titulo":"Titulo 5","texto":"texto 1","rowspan":"2","colspan":"2"},
        {"titulo":"Titulo 6","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 7","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 8","texto":"texto 4","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 9","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 10","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 11","texto":"texto 3","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 12","texto":"texto 4","rowspan":"1","colspan":"1"}
      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<tarjetas.length;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
        clontarjeta.querySelector("section").textContent = tarjetas[i].texto
        clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
        clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### saco con boton
<small>Creado: 2025-10-22 17:30</small>

`023-saco con boton.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<tarjetas.length;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
        clontarjeta.querySelector("section").textContent = tarjetas[i].texto
        clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
        clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### crear un nuevo objeto
<small>Creado: 2025-10-22 17:31</small>

`024-crear un nuevo objeto.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":"Titulo 1",
          "texto":"texto 1",
          "rowspan":"1",
          "colspan":"1"
        }
        tarjetas.push(objeto)
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      
      let contenedortarjetas = document.querySelector("main");
      let plantillatarjeta = document.querySelector("#plantillatarjeta");
      for(let i = 0;i<tarjetas.length;i++){
        let clontarjeta = plantillatarjeta.content.cloneNode(true); 
        clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
        clontarjeta.querySelector("section").textContent = tarjetas[i].texto
        clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
        clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
        contenedortarjetas.appendChild(clontarjeta)
      }
      
    </script>
  </body>
</html>
```

### funcion
<small>Creado: 2025-10-22 17:39</small>

`025-funcion.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":"Titulo 1",
          "texto":"texto 1",
          "rowspan":"1",
          "colspan":"1"
        }
        tarjetas.push(objeto)
        repintar(); ///////////////////////////////// VUELVE A PINTAR LAS TARJETAS
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      function repintar(){
        let contenedortarjetas = document.querySelector("main");
        contenedortarjetas.innerHTML = ""
        let plantillatarjeta = document.querySelector("#plantillatarjeta");
        for(let i = 0;i<tarjetas.length;i++){
          let clontarjeta = plantillatarjeta.content.cloneNode(true); 
          clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
          clontarjeta.querySelector("section").textContent = tarjetas[i].texto
          clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
          clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
          contenedortarjetas.appendChild(clontarjeta)
        }
      }
      repintar(); /////////////////// PARA QUE SE EJECUTE AL PRINCIPIO
    </script>
  </body>
</html>
```

### objeto de verdad
<small>Creado: 2025-10-22 18:30</small>

`026-objeto de verdad.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":document.querySelector("#titulo_nueva_tarjeta").value,
          "texto":document.querySelector("#contenido_nueva_tarjeta").value,
          "rowspan":document.querySelector("#filas_nueva_tarjeta").value,
          "colspan":document.querySelector("#columnas_nueva_tarjeta").value
        }
        tarjetas.push(objeto)
        repintar(); ///////////////////////////////// VUELVE A PINTAR LAS TARJETAS
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      function repintar(){
        let contenedortarjetas = document.querySelector("main");
        contenedortarjetas.innerHTML = ""
        let plantillatarjeta = document.querySelector("#plantillatarjeta");
        for(let i = 0;i<tarjetas.length;i++){
          let clontarjeta = plantillatarjeta.content.cloneNode(true); 
          clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
          clontarjeta.querySelector("section").textContent = tarjetas[i].texto
          clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
          clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
          contenedortarjetas.appendChild(clontarjeta)
        }
      }
      repintar(); /////////////////// PARA QUE SE EJECUTE AL PRINCIPIO
    </script>
  </body>
</html>
```

### guardo en localstorage
<small>Creado: 2025-10-22 18:37</small>

`027-guardo en localstorage.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":document.querySelector("#titulo_nueva_tarjeta").value,
          "texto":document.querySelector("#contenido_nueva_tarjeta").value,
          "rowspan":document.querySelector("#filas_nueva_tarjeta").value,
          "colspan":document.querySelector("#columnas_nueva_tarjeta").value
        }
        tarjetas.push(objeto)
        localStorage.setItem("cartitas",JSON.stringify(tarjetas));
        repintar(); ///////////////////////////////// VUELVE A PINTAR LAS TARJETAS
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      function repintar(){
        let contenedortarjetas = document.querySelector("main");
        contenedortarjetas.innerHTML = ""
        let plantillatarjeta = document.querySelector("#plantillatarjeta");
        for(let i = 0;i<tarjetas.length;i++){
          let clontarjeta = plantillatarjeta.content.cloneNode(true); 
          clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
          clontarjeta.querySelector("section").textContent = tarjetas[i].texto
          clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
          clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
          contenedortarjetas.appendChild(clontarjeta)
        }
      }
      repintar(); /////////////////// PARA QUE SE EJECUTE AL PRINCIPIO
    </script>
  </body>
</html>
```

### get item
<small>Creado: 2025-10-22 18:40</small>

`028-get item.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":document.querySelector("#titulo_nueva_tarjeta").value,
          "texto":document.querySelector("#contenido_nueva_tarjeta").value,
          "rowspan":document.querySelector("#filas_nueva_tarjeta").value,
          "colspan":document.querySelector("#columnas_nueva_tarjeta").value
        }
        tarjetas.push(objeto)
        localStorage.setItem("cartitas",JSON.stringify(tarjetas));
        repintar(); ///////////////////////////////// VUELVE A PINTAR LAS TARJETAS
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      tarjetas = JSON.parse(localStorage.getItem("cartitas"))
      function repintar(){
        let contenedortarjetas = document.querySelector("main");
        contenedortarjetas.innerHTML = ""
        let plantillatarjeta = document.querySelector("#plantillatarjeta");
        for(let i = 0;i<tarjetas.length;i++){
          let clontarjeta = plantillatarjeta.content.cloneNode(true); 
          clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
          clontarjeta.querySelector("section").textContent = tarjetas[i].texto
          clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
          clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
          contenedortarjetas.appendChild(clontarjeta)
        }
      }
      repintar(); /////////////////// PARA QUE SE EJECUTE AL PRINCIPIO
    </script>
  </body>
</html>
```

### boton eliminar
<small>Creado: 2025-10-22 18:45</small>

`029-boton eliminar.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;border-radius:5px;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <button class="eliminar">❌</button>
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":document.querySelector("#titulo_nueva_tarjeta").value,
          "texto":document.querySelector("#contenido_nueva_tarjeta").value,
          "rowspan":document.querySelector("#filas_nueva_tarjeta").value,
          "colspan":document.querySelector("#columnas_nueva_tarjeta").value
        }
        tarjetas.push(objeto)
        localStorage.setItem("cartitas",JSON.stringify(tarjetas));
        repintar(); ///////////////////////////////// VUELVE A PINTAR LAS TARJETAS
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      tarjetas = JSON.parse(localStorage.getItem("cartitas"))
      function repintar(){
        let contenedortarjetas = document.querySelector("main");
        contenedortarjetas.innerHTML = ""
        let plantillatarjeta = document.querySelector("#plantillatarjeta");
        for(let i = 0;i<tarjetas.length;i++){
          let clontarjeta = plantillatarjeta.content.cloneNode(true); 
          clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
          clontarjeta.querySelector("section").textContent = tarjetas[i].texto
          clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
          clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
          contenedortarjetas.appendChild(clontarjeta)
        }
      }
      repintar(); /////////////////// PARA QUE SE EJECUTE AL PRINCIPIO
    </script>
  </body>
</html>
```

### estilo del boton
<small>Creado: 2025-10-22 18:50</small>

`030-estilo del boton.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    <style>
      .tarjeta{position:relative;border-radius:12px;}
      .tarjeta .eliminar{
        position:absolute;right:2px;top:2px;width:20px;height:20px;background:white;
        font-size:10px;line-height:11px;text-align:center;
      }
    </style>
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <button class="eliminar">❌</button>
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":document.querySelector("#titulo_nueva_tarjeta").value,
          "texto":document.querySelector("#contenido_nueva_tarjeta").value,
          "rowspan":document.querySelector("#filas_nueva_tarjeta").value,
          "colspan":document.querySelector("#columnas_nueva_tarjeta").value
        }
        tarjetas.push(objeto)
        localStorage.setItem("cartitas",JSON.stringify(tarjetas));
        repintar(); ///////////////////////////////// VUELVE A PINTAR LAS TARJETAS
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      tarjetas = JSON.parse(localStorage.getItem("cartitas"))
      function repintar(){
        let contenedortarjetas = document.querySelector("main");
        contenedortarjetas.innerHTML = ""
        let plantillatarjeta = document.querySelector("#plantillatarjeta");
        for(let i = 0;i<tarjetas.length;i++){
          let clontarjeta = plantillatarjeta.content.cloneNode(true); 
          clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
          clontarjeta.querySelector("section").textContent = tarjetas[i].texto
          clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
          clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
          contenedortarjetas.appendChild(clontarjeta)
        }
      }
      repintar(); /////////////////// PARA QUE SE EJECUTE AL PRINCIPIO
    </script>
  </body>
</html>
```

### comportamiento del boton
<small>Creado: 2025-10-22 18:53</small>

`031-comportamiento del boton.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    <style>
      .tarjeta{position:relative;border-radius:12px;}
      .tarjeta .eliminar{
        position:absolute;right:2px;top:2px;width:20px;height:20px;background:white;
        font-size:10px;line-height:11px;text-align:center;
      }
    </style>
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <button class="eliminar">❌</button>
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":document.querySelector("#titulo_nueva_tarjeta").value,
          "texto":document.querySelector("#contenido_nueva_tarjeta").value,
          "rowspan":document.querySelector("#filas_nueva_tarjeta").value,
          "colspan":document.querySelector("#columnas_nueva_tarjeta").value
        }
        tarjetas.push(objeto)
        localStorage.setItem("cartitas",JSON.stringify(tarjetas));
        repintar(); ///////////////////////////////// VUELVE A PINTAR LAS TARJETAS
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      tarjetas = JSON.parse(localStorage.getItem("cartitas"))
      function repintar(){
        let contenedortarjetas = document.querySelector("main");
        contenedortarjetas.innerHTML = ""
        let plantillatarjeta = document.querySelector("#plantillatarjeta");
        for(let i = 0;i<tarjetas.length;i++){
          let clontarjeta = plantillatarjeta.content.cloneNode(true); 
          clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
          clontarjeta.querySelector("section").textContent = tarjetas[i].texto
          clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
          clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
          clontarjeta.querySelector(".eliminar").onclick = function(){
            alert("Voy a eliminar la tarjeta, pero no sé muy bien cómo")
          }
          contenedortarjetas.appendChild(clontarjeta)
        }
      }
      repintar(); /////////////////// PARA QUE SE EJECUTE AL PRINCIPIO
    </script>
  </body>
</html>
```

### eliminar con identificador
<small>Creado: 2025-10-22 19:08</small>

`032-eliminar con identificador.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    <style>
      .tarjeta{position:relative;border-radius:12px;}
      .tarjeta .eliminar{
        position:absolute;right:2px;top:2px;width:20px;height:20px;background:white;
        font-size:10px;line-height:11px;text-align:center;
      }
    </style>
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <button class="eliminar">❌</button>
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":document.querySelector("#titulo_nueva_tarjeta").value,
          "texto":document.querySelector("#contenido_nueva_tarjeta").value,
          "rowspan":document.querySelector("#filas_nueva_tarjeta").value,
          "colspan":document.querySelector("#columnas_nueva_tarjeta").value
        }
        tarjetas.push(objeto)
        localStorage.setItem("cartitas",JSON.stringify(tarjetas));
        repintar(); ///////////////////////////////// VUELVE A PINTAR LAS TARJETAS
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      tarjetas = JSON.parse(localStorage.getItem("cartitas"))
      function repintar(){
        let contenedortarjetas = document.querySelector("main");
        contenedortarjetas.innerHTML = ""
        let plantillatarjeta = document.querySelector("#plantillatarjeta");
        for(let i = 0;i<tarjetas.length;i++){
          let clontarjeta = plantillatarjeta.content.cloneNode(true); 
          clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
          clontarjeta.querySelector("section").textContent = tarjetas[i].texto
          clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
          clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
          
          // Este selector crea un atributo personalizado para el boton
          clontarjeta.querySelector(".eliminar").setAttribute("rosalee_eliminar",i)
         
          // Este otro selector le añade un evento de click
          clontarjeta.querySelector(".eliminar").onclick = function(){
            
            // Primero elimino el elemento que tiene este atributo en el array
            tarjetas.splice(this.getAttribute("rosalee_eliminar"),1)
            
            // Actualizo el contenido del localstorage
            localStorage.setItem("cartitas",JSON.stringify(tarjetas));
            
            // Fuerzo un repintado
            repintar()
          }
          contenedortarjetas.appendChild(clontarjeta)
        }
      }
      repintar(); /////////////////// PARA QUE SE EJECUTE AL PRINCIPIO
    </script>
  </body>
</html>
```

### ahora sin comentarios
<small>Creado: 2025-10-22 19:08</small>

`033-ahora sin comentarios.html`

```html
<!doctype html>
<html>
  <head>
    <title>Plantillas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;font-family:sans-serif;font-size:10px;}
      nav{flex:1;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:8;background:MistyRose;}
      button{
        border:none;background:purple;border-radius:50px;
        padding:5px;width:150px;color:white;text-align:left;
      }
      button .inicial{
        width:20px;height:20px;background:white;border-radius:50px;color:purple;
        display:inline-block;text-align:center;line-height:20px;text-transform:uppercase;
      }
      main{display:grid;grid-template-columns:auto auto auto auto;gap:10px;padding:10px;}
      .tarjeta{background:white;box-shadow:0px 2px 4px rgba(0,0,0,0.3);overflow:hidden;transition:all 1s;}
      .tarjeta:hover{transform:scale(1.02,1.02);}
      .tarjeta header{background:purple;color:white;padding:10px;}
      .tarjeta section{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      
    </nav>
    <main>
    </main>
    <template id="elementomenu">
      <button>
        <span class="inicial">L</span>
        <span class="texto">Letra</span>
      </button>
    </template>
    <style>
      .tarjeta{position:relative;border-radius:12px;}
      .tarjeta .eliminar{
        position:absolute;right:2px;top:2px;width:20px;height:20px;background:white;
        font-size:10px;line-height:11px;text-align:center;
      }
    </style>
    <template id="plantillatarjeta">
      <article class="tarjeta">
        <button class="eliminar">❌</button>
        <header>
          Cabecera de prueba
        </header>
        <section>
          Contenido de prueba
        </section>
      </article>
    </template>
    
    <style>
      #contienemodal{
        position:absolute;width:100%;height:100%;top:0px;left:0px;background:rgba(0,0,0,0.6);
        display:flex;justify-content: center;align-items: center;
        display:none;
      }
      #modal{
        width:500px;height:300px;padding:20px;background:white;border-radius:5px;
        box-shadow:0px 5px 10px black;
        display:flex;flex-direction:column;justify-content: center;gap:5px; 
      }
      #modal input,#modal textarea,#modal button{
        border:1px solid indigo;width:100%;
      }
    </style>
    <div id="contienemodal">
      <div id="modal">
        <label for="titulo_nueva_tarjeta">Título de la nueva tarjeta</label>
        <input type="text" id="titulo_nueva_tarjeta">
        <label for="contenido_nueva_tarjeta">Contenido de la nueva tarjeta</label>
        <textarea id="contenido_nueva_tarjeta"></textarea>
        <label for="columnas_nueva_tarjeta">Expansión de columnas</label>
        <input type="number" id="columnas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="filas_nueva_tarjeta">Expansión de filas</label>
        <input type="number" id="filas_nueva_tarjeta" min=1 max=5 value=1 step=1>
        <label for="color_nueva_tarjeta">Color</label>
        <input type="color" id="color_nueva_tarjeta">
        <button id="guardatarjeta">Guardar</button>
      </div>
    </div>
    <script>
      /////////////////////////////// POBLAR MENU ////////////////////////////////////////////
      
      let elementosmenu = ["inicio","productos","clientes","pedidos","stock","empleados"];
      
      let contenedor = document.querySelector("nav");           // Contenedor
      let plantilla = document.querySelector("#elementomenu");  // Plantilla en memoria
      
      for(let i = 0;i<elementosmenu.length;i++){
        let clon = plantilla.content.cloneNode(true);             // Clon en memoria
        // Lo interesante es que puedo modificar los elementos del clon
        clon.querySelector(".texto").textContent = elementosmenu[i]
        clon.querySelector(".inicial").textContent = elementosmenu[i][0] // Primer caracter
        contenedor.appendChild(clon);                             // Pongo la plantilla en c
      }
      
      let boton_nuevo = document.createElement("button");
      boton_nuevo.textContent = "Crear nuevo elemento"
      boton_nuevo.onclick = function(){
        document.querySelector("#contienemodal").style.display = "flex"
      }
      contenedor.appendChild(boton_nuevo);
      
      let boton_guardatarjeta = document.querySelector("#guardatarjeta")
      boton_guardatarjeta.onclick = function(){
        let objeto = {
          "titulo":document.querySelector("#titulo_nueva_tarjeta").value,
          "texto":document.querySelector("#contenido_nueva_tarjeta").value,
          "rowspan":document.querySelector("#filas_nueva_tarjeta").value,
          "colspan":document.querySelector("#columnas_nueva_tarjeta").value
        }
        tarjetas.push(objeto)
        localStorage.setItem("cartitas",JSON.stringify(tarjetas));
        repintar(); ///////////////////////////////// VUELVE A PINTAR LAS TARJETAS
        document.querySelector("#contienemodal").style.display = "none"
      }
      
      /////////////////////////////// POBLAR TARJETAS ////////////////////////////////////////////
      
      let tarjetas = [
        {"titulo":"Titulo 1","texto":"texto 1","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 2","texto":"texto 2","rowspan":"1","colspan":"1"},
        {"titulo":"Titulo 3","texto":"texto 3","rowspan":"1","colspan":"1"}

      ]
      tarjetas = JSON.parse(localStorage.getItem("cartitas"))
      function repintar(){
        let contenedortarjetas = document.querySelector("main");
        contenedortarjetas.innerHTML = ""
        let plantillatarjeta = document.querySelector("#plantillatarjeta");
        for(let i = 0;i<tarjetas.length;i++){
          let clontarjeta = plantillatarjeta.content.cloneNode(true); 
          clontarjeta.querySelector("header").textContent = tarjetas[i].titulo
          clontarjeta.querySelector("section").textContent = tarjetas[i].texto
          clontarjeta.querySelector("article").style.gridRow = "span "+tarjetas[i].rowspan
          clontarjeta.querySelector("article").style.gridColumn = "span "+tarjetas[i].colspan
          clontarjeta.querySelector(".eliminar").setAttribute("rosalee_eliminar",i)
          clontarjeta.querySelector(".eliminar").onclick = function(){
            tarjetas.splice(this.getAttribute("rosalee_eliminar"),1)
            localStorage.setItem("cartitas",JSON.stringify(tarjetas));
            repintar()
          }
          contenedortarjetas.appendChild(clontarjeta)
        }
      }
      repintar(); /////////////////// PARA QUE SE EJECUTE AL PRINCIPIO
    </script>
  </body>
</html>
```


<a id="simulacro-de-examen-1"></a>
## Simulacro de examen 1

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/011-Simulacro%20de%20examen%201)


<a id="simulacro-de-examen-2"></a>
## Simulacro de examen 2

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/012-Simulacro%20de%20examen%202)


<a id="repaso-modal"></a>
## Repaso modal

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/013-Repaso%20modal)

### inicio
<small>Creado: 2025-11-04 17:04</small>

`001-inicio.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    
  </body>
</html>
```

### contenido principal
<small>Creado: 2025-11-04 17:04</small>

`002-contenido principal.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <p>Este es el contenido de la web</p>
    </main>
  </body>
</html>
```

### contenedormodal
<small>Creado: 2025-11-04 17:07</small>

`003-contenedormodal.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <p>Este es el contenido de la web</p>
    </main>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed; /* Va a su rollo */
        width:100%; /* Ocupa toda la anchura */
        height:100%; /* Ocupa toda la altura */
        background:black; /* Su fondo es negro */
        top:0px;   /* Empieza arriba */
        left:0px; /* Empieza a la izquierda */
        }
    </style>
    <div id="contenedormodal">
    </div>
  </body>
</html>
```

### semitransparente
<small>Creado: 2025-11-04 17:08</small>

`004-semitransparente.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <p>Este es el contenido de la web</p>
    </main>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed; /* Va a su rollo */
        width:100%; /* Ocupa toda la anchura */
        height:100%; /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;   /* Empieza arriba */
        left:0px; /* Empieza a la izquierda */
       }
    </style>
    <div id="contenedormodal">
    </div>
  </body>
</html>
```

### ahora hago el modal
<small>Creado: 2025-11-04 17:10</small>

`005-ahora hago el modal.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <p>Este es el contenido de la web</p>
    </main>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed; /* Va a su rollo */
        width:100%; /* Ocupa toda la anchura */
        height:100%; /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;   /* Empieza arriba */
        left:0px; /* Empieza a la izquierda */
       }
       #modal{
         width:400px; /* Anchura */
         height:400px; /* Altura */
         background:white; /* Fondo blanco */
         padding:20px; /* Margen interior */
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
      </div>
    </div>
  </body>
</html>
```

### centrar con flexbox
<small>Creado: 2025-11-04 17:13</small>

`006-centrar con flexbox.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <p>Este es el contenido de la web</p>
    </main>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:flex;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
      </div>
    </div>
  </body>
</html>
```

### lo escondo
<small>Creado: 2025-11-04 17:13</small>

`007-lo escondo.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <p>Este es el contenido de la web</p>
    </main>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
      </div>
    </div>
  </body>
</html>
```

### preparo un boton
<small>Creado: 2025-11-04 17:14</small>

`008-preparo un boton.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <p>Este es el contenido de la web</p>
      <button>Pulsame y te enseño el modal</button>
    </main>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
      </div>
    </div>
  </body>
</html>
```

### javascript
<small>Creado: 2025-11-04 17:17</small>

`009-javascript.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <p>Este es el contenido de la web</p>
      <button>Pulsame y te enseño el modal</button>
      <script>
        document.querySelector("button").onclick = function(){
          document.querySelector("#contenedormodal").style.display = "flex"
        }
      </script>
    </main>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
      </div>
    </div>
  </body>
</html>
```

### estilo del tobon
<small>Creado: 2025-11-04 17:18</small>

`010-estilo del tobon.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <p>Este es el contenido de la web</p>
      <!-- Componente boton /////////////////////////////////// -->
      <button>Pulsame y te enseño el modal</button>
      <style>
        button{
          background:blue;padding:20px;border:none;border-radius:5px;color:white;
        }
      </style>
      <script>
        document.querySelector("button").onclick = function(){
          document.querySelector("#contenedormodal").style.display = "flex"
        }
      </script>
      <!-- Componente boton /////////////////////////////////// -->
    </main>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
      </div>
    </div>
  </body>
</html>
```

### muro de imagenes
<small>Creado: 2025-11-04 17:25</small>

`011-muro de imagenes.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
      </div>
    </div>
  </body>
</html>
```

### grid
<small>Creado: 2025-11-04 17:27</small>

`012-grid.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
      </div>
    </div>
  </body>
</html>
```

### comportamiento modal parte 1
<small>Creado: 2025-11-04 17:34</small>

`013-comportamiento modal parte 1.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    <script>
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          document.querySelector("#contenedormodal").style.display = "flex";
        }
      })
    </script>
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
      </div>
    </div>
  </body>
</html>
```

### modal y me llevo la imagen
<small>Creado: 2025-11-04 17:39</small>

`014-modal y me llevo la imagen.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    <script>
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
    </script>
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{width:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <img src="">
      </div>
    </div>
  </body>
</html>
```

### ajusto a la altura
<small>Creado: 2025-11-04 18:17</small>

`015-ajusto a la altura.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    <script>
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
    </script>
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <img src="">
      </div>
    </div>
  </body>
</html>
```

### cuando haga click el modal se esconde
<small>Creado: 2025-11-04 18:20</small>

`016-cuando haga click el modal se esconde.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <img src="">
      </div>
    </div>
    <script>
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
      }
    </script>
  </body>
</html>
```

### botones siguiente y anterior
<small>Creado: 2025-11-04 18:23</small>

`017-botones siguiente y anterior.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <img src="">
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
      }
    </script>
  </body>
</html>
```

### flex al modal
<small>Creado: 2025-11-04 18:26</small>

`018-flex al modal.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <img src="">
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
      }
    </script>
  </body>
</html>
```

### comportamiento de los botones
<small>Creado: 2025-11-04 18:31</small>

`019-comportamiento de los botones.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <img src="">
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```

### imagen activa
<small>Creado: 2025-11-04 18:36</small>

`020-imagen activa.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <img src="">
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      var imagen_activa = undefined;    // Al principio no sé quién es la imagen activa
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          imagen_activa = this        // Ahora ya se quien es la imagen activa
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.nextElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```

### boton anterior
<small>Creado: 2025-11-04 18:37</small>

`021-boton anterior.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
      <img src="img/2024-04-28-19-35-35.jpg">
      <img src="img/2024-04-28-19-35-40.jpg"> 
      <img src="img/2024-04-28-19-36-06.jpg"> 
      <img src="img/2024-04-28-19-36-07.jpg"> 
      <img src="img/2024-04-28-19-38-03.jpg"> 
      <img src="img/2024-04-28-19-38-28.jpg">
      <img src="img/2024-04-28-19-38-45.jpg">
      <img src="img/2024-04-28-19-47-23.jpg">
      <img src="img/2024-04-28-19-49-02color.jpg">
    </main>
    
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <img src="">
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      var imagen_activa = undefined;    // Al principio no sé quién es la imagen activa
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          imagen_activa = this        // Ahora ya se quien es la imagen activa
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.nextElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
      document.querySelector("#anterior").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.previousElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```

### excusa del texto alternativa
<small>Creado: 2025-11-04 18:42</small>

`022-excusa del texto alternativa.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 1">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 2"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 3"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 4"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 5"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 6">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 7">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 8">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 9">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 10">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 11"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 12"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 13"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 14"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 15">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 16">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 17">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 18">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 19">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 20"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 21"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 22"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 23"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 24">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 25">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 26">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 27">
    </main>
    
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <img src="">
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      var imagen_activa = undefined;    // Al principio no sé quién es la imagen activa
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          imagen_activa = this        // Ahora ya se quien es la imagen activa
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.nextElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
      document.querySelector("#anterior").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.previousElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```

### trampichuela del blur
<small>Creado: 2025-11-04 18:46</small>

`023-trampichuela del blur.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 1">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 2"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 3"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 4"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 5"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 6">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 7">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 8">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 9">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 10">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 11"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 12"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 13"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 14"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 15">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 16">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 17">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 18">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 19">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 20"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 21"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 22"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 23"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 24">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 25">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 26">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 27">
    </main>
    
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:100%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
        backdrop-filter: blur(5px);
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
         backdrop-filter: blur(20px);
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <img src="">
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      var imagen_activa = undefined;    // Al principio no sé quién es la imagen activa
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          imagen_activa = this        // Ahora ya se quien es la imagen activa
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.nextElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
      document.querySelector("#anterior").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.previousElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```

### texto
<small>Creado: 2025-11-04 18:48</small>

`024-texto.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 1">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 2"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 3"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 4"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 5"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 6">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 7">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 8">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 9">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 10">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 11"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 12"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 13"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 14"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 15">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 16">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 17">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 18">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 19">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 20"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 21"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 22"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 23"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 24">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 25">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 26">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 27">
    </main>
    
    <style> 
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:90%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
        backdrop-filter: blur(5px);
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
         backdrop-filter: blur(20px);
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       #contienepieza{
        width:100%;
        height:100%;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <div id="contienepieza">
          <img src="">
          <p>Hola</p>
        </div>
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      var imagen_activa = undefined;    // Al principio no sé quién es la imagen activa
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          imagen_activa = this        // Ahora ya se quien es la imagen activa
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
          document.querySelector("#contienepieza p").textContent = this.getAttribute("alt")
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.nextElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
      document.querySelector("#anterior").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.previousElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```

### refino el estilo
<small>Creado: 2025-11-04 18:48</small>

`025-refino el estilo.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 1">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 2"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 3"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 4"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 5"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 6">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 7">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 8">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 9">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 10">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 11"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 12"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 13"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 14"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 15">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 16">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 17">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 18">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 19">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 20"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 21"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 22"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 23"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 24">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 25">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 26">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 27">
    </main>
    
    <style> 
      body{background:black;}
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;}
      #modal img{height:90%;}
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
        backdrop-filter: blur(5px);
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
         backdrop-filter: blur(20px);
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       #contienepieza{
        width:100%;
        height:100%;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <div id="contienepieza">
          <img src="">
          <p>Hola</p>
        </div>
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      var imagen_activa = undefined;    // Al principio no sé quién es la imagen activa
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          imagen_activa = this        // Ahora ya se quien es la imagen activa
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
          document.querySelector("#contienepieza p").textContent = this.getAttribute("alt")
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.nextElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
      document.querySelector("#anterior").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.previousElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```

### las imagenes se hacen grandes
<small>Creado: 2025-11-04 18:49</small>

`026-las imagenes se hacen grandes.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 1">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 2"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 3"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 4"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 5"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 6">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 7">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 8">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 9">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 10">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 11"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 12"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 13"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 14"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 15">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 16">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 17">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 18">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 19">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 20"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 21"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 22"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 23"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 24">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 25">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 26">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 27">
    </main>
    
    <style> 
      body{background:black;}
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;transition:all 1s;}
      main img:hover{transform:scale(1.1,1.1);}
      #modal img{height:90%;}
      
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
        backdrop-filter: blur(5px);
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
         backdrop-filter: blur(20px);
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       #contienepieza{
        width:100%;
        height:100%;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <div id="contienepieza">
          <img src="">
          <p>Hola</p>
        </div>
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      var imagen_activa = undefined;    // Al principio no sé quién es la imagen activa
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          imagen_activa = this        // Ahora ya se quien es la imagen activa
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
          document.querySelector("#contienepieza p").textContent = this.getAttribute("alt")
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.nextElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
      document.querySelector("#anterior").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.previousElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```

### propago a los botones
<small>Creado: 2025-11-04 18:58</small>

`027-propago a los botones.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 1">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 2"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 3"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 4"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 5"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 6">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 7">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 8">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 9">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 10">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 11"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 12"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 13"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 14"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 15">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 16">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 17">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 18">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 19">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 20"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 21"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 22"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 23"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 24">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 25">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 26">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 27">
    </main>
    
    <style> 
      body{background:black;}
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;transition:all 1s;}
      main img:hover{transform:scale(1.1,1.1);}
      #modal img{height:90%;}
      
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
        backdrop-filter: blur(5px);
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
         backdrop-filter: blur(20px);
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       #contienepieza{
        width:100%;
        height:100%;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <div id="contienepieza">
          <img src="">
          <p>Hola</p>
        </div>
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      var imagen_activa = undefined;    // Al principio no sé quién es la imagen activa
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          imagen_activa = this        // Ahora ya se quien es la imagen activa
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
          document.querySelector("#contienepieza p").textContent = this.getAttribute("alt")
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.nextElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        document.querySelector("#contienepieza p").textContent = siguiente.getAttribute("alt")
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
      document.querySelector("#anterior").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.previousElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        document.querySelector("#contienepieza p").textContent = siguiente.getAttribute("alt")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```

### editamos un poco el estilo
<small>Creado: 2025-11-04 19:02</small>

`028-editamos un poco el estilo.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Modal</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 1">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 2"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 3"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 4"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 5"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 6">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 7">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 8">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 9">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 10">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 11"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 12"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 13"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 14"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 15">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 16">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 17">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 18">
      <img src="img/2024-04-28-19-35-35.jpg" alt="Descripción de la imagen 19">
      <img src="img/2024-04-28-19-35-40.jpg" alt="Descripción de la imagen 20"> 
      <img src="img/2024-04-28-19-36-06.jpg" alt="Descripción de la imagen 21"> 
      <img src="img/2024-04-28-19-36-07.jpg" alt="Descripción de la imagen 22"> 
      <img src="img/2024-04-28-19-38-03.jpg" alt="Descripción de la imagen 23"> 
      <img src="img/2024-04-28-19-38-28.jpg" alt="Descripción de la imagen 24">
      <img src="img/2024-04-28-19-38-45.jpg" alt="Descripción de la imagen 25">
      <img src="img/2024-04-28-19-47-23.jpg" alt="Descripción de la imagen 26">
      <img src="img/2024-04-28-19-49-02color.jpg" alt="Descripción de la imagen 27">
    </main>
    
    <style> 
      body{background:black;}
      main{
        display:grid;   /* Voy a crear una rejilla */
        grid-template-columns:auto auto auto auto auto auto auto auto;   /* Elijo cuantas columnas quiero */
        gap:20px;   /* Separación entre celdas */
      }
      main img{width:100%;transition:all 1s;border-radius:5px;border:1px solid white;}
      main img:hover{transform:scale(1.1,1.1);}
      #modal img{height:90%;}
      
    </style>
    <style>
      #contenedormodal{
        /* Con esto hago un telón negro */
        position:fixed;         /* Va a su rollo */
        width:100%;             /* Ocupa toda la anchura */
        height:100%;            /* Ocupa toda la altura */
        background:rgba(0,0,0,0.5); /* Su fondo es negro */
        top:0px;                /* Empieza arriba */
        left:0px;               /* Empieza a la izquierda */
        display:none;           /* Centro con flex */
        align-items:center;     /* Centro en vertical */
        justify-content:center; /* Centro en horizontal */
        backdrop-filter: blur(5px);
       }
       #modal{
         width:400px;           /* Anchura */
         height:400px;          /* Altura */
         background:white;      /* Fondo blanco */
         padding:20px;          /* Margen interior */
         border-radius:5px;
         box-shadow:0px 10px 20px black;
         text-align:center;
         display:flex;
         justify-content:space-between;
         align-items:center;
         backdrop-filter: blur(20px);
       }
       #modal button{
         border:none; /* No quiero borde */
         background:white; /* El fondo es blanco */
         box-shadow:0px 2px 4px black; /* Sombrita */
         border-radius:100px; /* Borde redondeado */
         width:30px; /* Anchura de 30 pixeles */
         height:30px; /* Altura de 30 pixeles */
       }
       #contienepieza{
        width:100%;
        height:100%;
       }
    </style>
    <div id="contenedormodal">
      <div id="modal">
        <button id="anterior">⬅</button>
        <div id="contienepieza">
          <img src="">
          <p>Hola</p>
        </div>
        <button id="siguiente">➡</button>
      </div>
    </div>
    <script>
      var imagen_activa = undefined;    // Al principio no sé quién es la imagen activa
      let imagenes = document.querySelectorAll("img")
      console.log(imagenes)
      
      imagenes.forEach(function(imagen){
        imagen.onclick = function(){
          imagen_activa = this        // Ahora ya se quien es la imagen activa
          document.querySelector("#contenedormodal").style.display = "flex";
          let imagen_origen = this.getAttribute("src")
          let imagen_destino = document.querySelector("#modal img")
          imagen_destino.setAttribute("src",imagen_origen)
          document.querySelector("#contienepieza p").textContent = this.getAttribute("alt")
        }
      })
      // Cuando haga click en el fondo del modal
      document.querySelector("#contenedormodal").onclick = function(){
        this.style.display = "none";  // Se esconde el modal
        
      }
      // Vamos a gestionar los botones
      document.querySelector("#siguiente").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.nextElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        document.querySelector("#contienepieza p").textContent = siguiente.getAttribute("alt")
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
      document.querySelector("#anterior").onclick = function(event){
        console.log("Vamos a la siguiente imagen")
        // Cogemos la siguiente imagen
        const siguiente = imagen_activa.previousElementSibling;
        // De esa imagen cogemos el atributo src
        let imagen_origen = siguiente.getAttribute("src")
        // Cogemos la imagen de destino
        let imagen_destino = document.querySelector("#modal img")
        document.querySelector("#contienepieza p").textContent = siguiente.getAttribute("alt")
        // Y le planchamos la imagen (el src)
        imagen_destino.setAttribute("src",imagen_origen)
        // Actualizamos lo que consideramos la imagen activa
        imagen_activa = siguiente
        
        event.stopPropagation();    // Evita que se dispare por accidente el ocultar
      }
    </script>
  </body>
</html>
```


<a id="ejercicio-de-final-de-unidad"></a>
## Ejercicio de final de unidad

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/101-Ejercicio%20de%20final%20de%20unidad)


<a id="examen-final"></a>
## Examen final

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/001-Planificaci%C3%B3n%20de%20interfaces%20gr%C3%A1ficas/104-Examen%20final)

### crear tablas
<small>Creado: 2025-11-11 17:56</small>

`001-crear tablas.sql`

```sql
CREATE DATABASE portafolioceac;

USE portafolioceac;


CREATE TABLE Piezas(
  Identificador INT auto_increment PRIMARY KEY,
  titulo VARCHAR(255),
  descripcion VARCHAR(255),
  imagen VARCHAR(255),
  url VARCHAR(255),
  id_categoria INT
);

CREATE TABLE Categorias(
  Identificador INT auto_increment PRIMARY KEY,
  titulo VARCHAR(255),
  descripcion VARCHAR(255)
);
```

### insertar
<small>Creado: 2025-11-11 17:56</small>

`002-insertar.sql`

```sql
INSERT INTO Categorias VALUES(
  NULL,
  'General',
  'Esta es la categoria general'
);

INSERT INTO Piezas VALUES(
  NULL,
  'Primera pieza',
  'Esta es la descripcion de la primera pieza',
  'josevicente.jpg',
  'https://jocarsa.com',
  1
);
```

### fk
<small>Creado: 2025-11-11 17:56</small>

`003-fk.sql`

```sql
ALTER TABLE Piezas
ADD CONSTRAINT fk_piezas_categorias
FOREIGN KEY (id_categoria) REFERENCES Categorias(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

### selecciones
<small>Creado: 2025-11-11 17:56</small>

`004-selecciones.sql`

```sql
SELECT * FROM Categorias;

SELECT * FROM Piezas;
```

### left join
<small>Creado: 2025-11-11 17:56</small>

`005-left join.sql`

```sql
SELECT 
* 
FROM Piezas
LEFT JOIN Categorias
ON Piezas.id_categoria = Categorias.Identificador;
```

### ahora creo la vista
<small>Creado: 2025-11-11 17:56</small>

`006-ahora creo la vista.sql`

```sql
CREATE VIEW piezas_y_categorias AS 
SELECT 
Categorias.titulo AS categoriatitulo,
Categorias.descripcion AS categoriadescripcion,
Piezas.titulo AS piezatitulo,
Piezas.descripcion AS piezadescripcion,
imagen,
url
FROM Piezas
LEFT JOIN Categorias
ON Piezas.id_categoria = Categorias.Identificador;

SELECT * FROM piezas_y_categorias;
```

### usuario
<small>Creado: 2025-11-11 17:56</small>

`007-usuario.sql`

```sql
-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER 
'portafolioceac'@'localhost' 
IDENTIFIED  BY 'portafolioceac';

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'portafolioceac'@'localhost';
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len

-- quitale todos los limites que tenga
ALTER USER 'portafolioceac'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON portafolioceac.* 
TO 'portafolioceac'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
```



<a id="uso-de-estilos"></a>
# Uso de estilos

<a id="estilos-en-linea-basados-en-etiquetas-y-en-clases"></a>
## Estilos en línea basados en etiquetas y en clases.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/002-Uso%20de%20estilos/001-Estilos%20en%20l%C3%ADnea%20basados%20en%20etiquetas%20y%20en%20clases.)

### en linea
<small>Creado: 2025-10-14 18:35</small>

`001-en linea.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <p style="color:red;">Este es un texto de color rojo</p>
  </body>
</html>

No recomendado en lineas generales, pero puede venir bien en ocasiones particulares
```

### estilo interno
<small>Creado: 2025-10-14 18:35</small>

`002-estilo interno.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      p{
        color:red;
      }
    </style>
  </head>
  <body>
    <p style="color:red;">Este es un texto de color rojo</p>
  </body>
</html>

Estilo en linea:
No recomendado en lineas generales, pero puede venir bien en ocasiones particulares

Estilo interno:
Desventaja: requiere controlar el concepto de selector
Ventaja: Centralizar estilos dentro del mismo documento
```

### estilo externo
<small>Creado: 2025-10-14 18:35</small>

`003-estilo externo.html`

```html
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="estilo.css">
    <style>
      p{
        color:red;
      }
    </style>
  </head>
  <body>
    <p style="color:red;">Este es un texto de color rojo</p>
  </body>
</html>

Estilo en linea:
No recomendado en lineas generales, pero puede venir bien en ocasiones particulares

Estilo interno:
Desventaja: requiere controlar el concepto de selector
Ventaja: Centralizar estilos dentro del mismo documento
```

### selector etiqueta id y clase
<small>Creado: 2025-10-14 18:35</small>

`004-selector etiqueta id y clase.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      p{
        color:red;
      }
    </style>
  </head>
  <body>
    <p>Color rojo</p>
    <p>Color verde</p>
    <p>Color azul</p>
  </body>
</html>
```

### clases
<small>Creado: 2025-10-14 18:35</small>

`005-clases.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      p{
        color:red;
      }
      .verde{
        color:green;
      }
      #azul{
        color:blue;
      }
      input[type='text']{
        background:blue;
      }
    </style>
  </head>
  <body>
    <p>Color rojo</p>
    <p class="verde">Color verde</p>
    <p id="azul">Color azul</p>
    <input type="text">
    <input type="password">
  </body>
</html>
```

### pseudoselectores
<small>Creado: 2025-10-14 18:35</small>

`006-pseudoselectores.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      button{
        color:white;
        background:blue;
        border:none;
        border-radius:5px;
        padding:10px;
        transition:all 1s;
        transform:translateY(-2px);
        box-shadow:0px 2px 2px rgba(0,0,0,0.5);
      }
      button:hover{
        transform:translateY(0px) rotate(10deg) scale(1.1,1.1);
        transform:translateY(0px);
        background:red;
        box-shadow:0px 0px 1px rgba(0,0,0,0.2);
      }     
    </style>
  </head>
  <body>
    <button>Pulsame</button>
  </body>
</html>
```

### estilo
<small>Creado: 2025-10-14 18:35</small>

`estilo.css`

```css
p{
  color:red;
}
```


<a id="crear-y-vincular-hojas-de-estilo"></a>
## Crear y vincular hojas de estilo.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/002-Uso%20de%20estilos/002-Crear%20y%20vincular%20hojas%20de%20estilo.)

### index
<small>Creado: 2025-10-14 18:35</small>

`001-index.html`

```html
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="estilo.css">
  </head>
  <body>
    <input type="text">
  </body>
</html>
```

### biblioteca
<small>Creado: 2025-10-14 18:35</small>

`002-biblioteca.html`

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="estilo2.css">
  </head>
  <body>
    <!--
      id PK
      titulo
      isbn
      autor
      editorial FK
      categoria FK
      num_paginas
    -->
    <!-- CREATE -->
    <form action="003-procesar.php" method="POST">
      <label for="titulo">Titulo</label>
      <input type="text" name="titulo" id="titulo">
      <label for="isbn">ISBN</label>
      <input type="text" name="isbn" id="isbn">
      <label for="autor">Autor</label>
      <input type="text" name="autor" id="autor">
      <label for="editorial">Editorial</label>
      <input type="text" name="editorial" id="editorial">
      <label for="categoria">Categoria</label>
      <input type="text" name="categoria" id="categoria">
      <label for="num_paginas">Número de páginas</label>
      <input type="text" name="num_paginas" id="num_paginas">
      <input type="submit">
    </form>
  </body>
</html>
```

### biblioteca
<small>Creado: 2025-10-14 18:35</small>

`003-biblioteca.php`

```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="estilo2.css">
  </head>
  <body>
    <!--
      id PK
      titulo
      isbn
      autor
      editorial FK
      categoria FK
      num_paginas
    -->
    <!-- CREATE -->
    <form action="003-procesar.php" method="POST">
      <label for="titulo">Titulo</label>
      <input type="text" name="titulo" id="titulo">
      <label for="isbn">ISBN</label>
      <input type="text" name="isbn" id="isbn">
      <label for="autor">Autor</label>
      <input type="text" name="autor" id="autor">
      <label for="editorial">Editorial</label>
      <input type="text" name="editorial" id="editorial">
      <label for="categoria">Categoria</label>
      <input type="text" name="categoria" id="categoria">
      <label for="num_paginas">Número de páginas</label>
      <input type="text" name="num_paginas" id="num_paginas">
      <input type="submit">
    </form>
    <section>
      <table>
        <thead>
          <tr>
            <th>Titulo</th>
            <th>ISBN</th>
            <th>Autor</th>
            <th>Editorial</th>
            <th>Categoria</th>
            <th>Número de páginas</th>
          </tr>
        </thead>
        <tbody>
          <?php
            $db = new SQLite3("biblioteca.db");             // Conectate a la base de datos
            $result = $db->query("SELECT * FROM libros");   // Dame un listado de todos los libros

            while ($row = $result->fetchArray(SQLITE3_ASSOC)) { // Y para cada uno de los resultados
                echo "<tr>
                  <td>".$row['titulo']."</td>
                  <td>".$row['isbn']."</td>
                  <td>".$row['autor']."</td>
                  <td>".$row['editorial']."</td>
                  <td>".$row['categoria']."</td>
                  <td>".$row['num_paginas']."</td>
                </tr>";                                     // Pinta una nueva fila de tabla
            }
          ?>
        </tbody>
      </table>
    </section>
  </body>
</html>
```

### procesar
<small>Creado: 2025-10-14 18:35</small>

`003-procesar.php`

```
<?php
  /*
      id PK
      titulo
      isbn
      autor
      editorial FK
      categoria FK
      num_paginas
   */
  $titulo = $_POST['titulo'];
  $isbn = $_POST['isbn'];
  $autor = $_POST['autor'];
  $editorial = $_POST['editorial'];
  $categoria = $_POST['categoria'];
  $num_paginas = $_POST['num_paginas'];
?>
<?php
  $db = new SQLite3("biblioteca.db");                     // Abrimos una base de datos
  $db->exec("CREATE TABLE IF NOT EXISTS libros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT, isbn TEXT, autor TEXT,
    editorial TEXT, categoria TEXT, num_paginas INTEGER
  )");                                                    // Si no existe la tabla libros, la creamos
  $db->exec("INSERT INTO libros(titulo,isbn,autor,editorial,categoria,num_paginas)
  VALUES ('$_POST[titulo]','$_POST[isbn]','$_POST[autor]','$_POST[editorial]','$_POST[categoria]',$_POST[num_paginas])");                                   // Insertamos un libro
  echo "✅ Libro insertado";                             // Hacemos un echo
?>
<meta http-equiv="refresh" content="5; url=003-biblioteca.php">
```

### boton borrar
<small>Creado: 2025-10-14 18:35</small>

`004-boton borrar.php`

```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="estilo2.css">
  </head>
  <body>
    <!--
      id PK
      titulo
      isbn
      autor
      editorial FK
      categoria FK
      num_paginas
    -->
    <!-- CREATE -->
    <form action="003-procesar.php" method="POST">
      <label for="titulo">Titulo</label>
      <input type="text" name="titulo" id="titulo">
      <label for="isbn">ISBN</label>
      <input type="text" name="isbn" id="isbn">
      <label for="autor">Autor</label>
      <input type="text" name="autor" id="autor">
      <label for="editorial">Editorial</label>
      <input type="text" name="editorial" id="editorial">
      <label for="categoria">Categoria</label>
      <input type="text" name="categoria" id="categoria">
      <label for="num_paginas">Número de páginas</label>
      <input type="text" name="num_paginas" id="num_paginas">
      <input type="submit">
    </form>
    <section>
      <table>
        <thead>
          <tr>
            <th>Titulo</th>
            <th>ISBN</th>
            <th>Autor</th>
            <th>Editorial</th>
            <th>Categoria</th>
            <th>Número de páginas</th>
            <th>Borrar</th>
          </tr>
        </thead>
        <tbody>
          <?php
            $db = new SQLite3("biblioteca.db");             // Conectate a la base de datos
            $result = $db->query("SELECT * FROM libros");   // Dame un listado de todos los libros

            while ($row = $result->fetchArray(SQLITE3_ASSOC)) { // Y para cada uno de los resultados
                echo "<tr>
                  <td>".$row['titulo']."</td>
                  <td>".$row['isbn']."</td>
                  <td>".$row['autor']."</td>
                  <td>".$row['editorial']."</td>
                  <td>".$row['categoria']."</td>
                  <td>".$row['num_paginas']."</td>
                  <td><a href='borrar.php?id=".$row['id']."'>✖</a></td>
                </tr>";                                     // Pinta una nueva fila de tabla
            }
          ?>
        </tbody>
      </table>
    </section>
  </body>
</html>
```

### todojuntobiblioteca
<small>Creado: 2025-10-14 18:35</small>

`005-todojuntobiblioteca.php`

```
<?php
  if(isset($_GET['operacion']) && $_GET['operacion'] == "insertar"){     // Solo ejecuto este código si la operacion es insertar
    $titulo = $_POST['titulo'];
    $isbn = $_POST['isbn'];
    $autor = $_POST['autor'];
    $editorial = $_POST['editorial'];
    $categoria = $_POST['categoria'];
    $num_paginas = $_POST['num_paginas'];
    $db = new SQLite3("biblioteca.db");                     // Abrimos una base de datos
    $db->exec("CREATE TABLE IF NOT EXISTS libros(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT, isbn TEXT, autor TEXT,
      editorial TEXT, categoria TEXT, num_paginas INTEGER
    )");                                                    // Si no existe la tabla libros, la creamos
    $db->exec("INSERT INTO libros(titulo,isbn,autor,editorial,categoria,num_paginas)
    VALUES ('$_POST[titulo]','$_POST[isbn]','$_POST[autor]','$_POST[editorial]','$_POST[categoria]',$_POST[num_paginas])");                                   // Insertamos un libro
   
  }
?>
<?php
  if(isset($_GET['operacion']) && $_GET['operacion'] == "borrar"){       // Solo ejecuto este codigo si la operacion es borrar
    $db = new SQLite3("biblioteca.db");                     // Abrimos una base de datos
    $db->exec("DELETE FROM libros WHERE id = ".$_GET['id']);     
  }   
?>

<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      body{
        background:LightSkyBlue;
        font-family:sans-serif;
        display:flex;     /* NUEVO */
      }
      form,table{         /* NUEVO */
        background:white;
        margin:auto;
        padding:20px;
                          /* He quitado del width */
        display:flex;
        flex-direction:column;
        gap:2px;
      }
      input{
        padding:5px;
        border:1px solid LightSkyBlue;
      }
      input[type="submit"]{
        background:LightSkyBlue;
        color:white;
        border:none;
      }
    </style>
  </head>
  <body>
    <!--
      id PK
      titulo
      isbn
      autor
      editorial FK
      categoria FK
      num_paginas
    -->
    <!-- CREATE -->
    <form action="?operacion=insertar" method="POST"> <!-- El action es yo mismo con la operación de insertar -->
      <label for="titulo">Titulo</label>
      <input type="text" name="titulo" id="titulo">
      <label for="isbn">ISBN</label>
      <input type="text" name="isbn" id="isbn">
      <label for="autor">Autor</label>
      <input type="text" name="autor" id="autor">
      <label for="editorial">Editorial</label>
      <input type="text" name="editorial" id="editorial">
      <label for="categoria">Categoria</label>
      <input type="text" name="categoria" id="categoria">
      <label for="num_paginas">Número de páginas</label>
      <input type="text" name="num_paginas" id="num_paginas">
      <input type="submit">
    </form>
    <section>
      <table>
        <thead>
          <tr>
            <th>Titulo</th>
            <th>ISBN</th>
            <th>Autor</th>
            <th>Editorial</th>
            <th>Categoria</th>
            <th>Número de páginas</th>
            <th>Borrar</th>
          </tr>
        </thead>
        <tbody>
          <?php
            $db = new SQLite3("biblioteca.db");             // Conectate a la base de datos
            $result = $db->query("SELECT * FROM libros");   // Dame un listado de todos los libros

            while ($row = $result->fetchArray(SQLITE3_ASSOC)) { // Y para cada uno de los resultados
                echo "<tr>
                  <td>".$row['titulo']."</td>
                  <td>".$row['isbn']."</td>
                  <td>".$row['autor']."</td>
                  <td>".$row['editorial']."</td>
                  <td>".$row['categoria']."</td>
                  <td>".$row['num_paginas']."</td>
                  <td><a href='?id=".$row['id']."&operacion=borrar'>✖</a></td>
                </tr>";                                     // Pinta una nueva fila de tabla
                // El hipervinculo es yo mismo ? con la operacion de borrar
            }
          ?>
        </tbody>
      </table>
    </section>
  </body>
</html>
```

### borrar
<small>Creado: 2025-10-14 18:35</small>

`borrar.php`

```
<?php
  $db = new SQLite3("biblioteca.db");                     // Abrimos una base de datos
  $db->exec("DELETE FROM libros WHERE id = ".$_GET['id']);        
?>
<meta http-equiv="refresh" content="5; url=003-biblioteca.php">
```

### estilo
<small>Creado: 2025-10-14 18:35</small>

`estilo.css`

```css
input{
  border:1px solid red;
}
```

### estilo2
<small>Creado: 2025-10-14 18:35</small>

`estilo2.css`

```css
body{
  background:LightSkyBlue;
  font-family:sans-serif;
  display:flex;     /* NUEVO */
}
form,table{         /* NUEVO */
  background:white;
  margin:auto;
  padding:20px;
                    /* He quitado del width */
  display:flex;
  flex-direction:column;
  gap:2px;
}
input{
  padding:5px;
  border:1px solid LightSkyBlue;
}
input[type="submit"]{
  background:LightSkyBlue;
  color:white;
  border:none;
}
```


<a id="crear-y-vincular-hojas-de-estilo-en-cascada-externa"></a>
## Crear y vincular hojas de estilo en cascada externa.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/002-Uso%20de%20estilos/003-Crear%20y%20vincular%20hojas%20de%20estilo%20en%20cascada%20externa.)


<a id="herramientas-y-test-de-verificacion"></a>
## Herramientas y test de verificación.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/002-Uso%20de%20estilos/004-Herramientas%20y%20test%20de%20verificaci%C3%B3n.)


<a id="tecnologias-y-frameworks"></a>
## Tecnologías y frameworks.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/002-Uso%20de%20estilos/005-Tecnolog%C3%ADas%20y%20frameworks.)


<a id="preprocesadores-de-estilos-variables-mixins-y-funciones"></a>
## Preprocesadores de estilos. Variables, mixins y funciones.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/002-Uso%20de%20estilos/006-Preprocesadores%20de%20estilos.%20Variables%2C%20mixins%20y%20funciones.)



<a id="implantacion-de-contenido-multimedia"></a>
# Implantación de contenido multimedia

<a id="tipos-de-imagenes-en-la-web"></a>
## Tipos de Imágenes en la web.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/003-Implantaci%C3%B3n%20de%20contenido%20multimedia/001-Tipos%20de%20Im%C3%A1genes%20en%20la%20web.)

### ejemplo imagenes
<small>Creado: 2026-02-17 17:01</small>

`002-ejemplo imagenes.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <img src="josevicente.jpg" alt="Jose Vicente Carratalá">
  </body>
</html>
```

### insertar svg parte 1
<small>Creado: 2026-02-17 17:09</small>

`003-insertar svg parte 1.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <img src="dibujo.svg" alt="Jose Vicente Carratalá">
  </body>
</html>
```

### insertar directamente
<small>Creado: 2026-02-17 17:10</small>

`004-insertar directamente.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <svg
       width="210mm"
       height="297mm"
       viewBox="0 0 210 297"
       version="1.1"
       id="svg1"
       inkscape:version="1.4.2 (1:1.4.2+202505120737+ebf0e940d0)"
       sodipodi:docname="dibujo.svg"
       xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
       xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
       xmlns="http://www.w3.org/2000/svg"
       xmlns:svg="http://www.w3.org/2000/svg">
      <sodipodi:namedview
         id="namedview1"
         pagecolor="#ffffff"
         bordercolor="#000000"
         borderopacity="0.25"
         inkscape:showpageshadow="2"
         inkscape:pageopacity="0.0"
         inkscape:pagecheckerboard="0"
         inkscape:deskcolor="#d1d1d1"
         inkscape:document-units="mm"
         inkscape:zoom="1.4142136"
         inkscape:cx="178.89801"
         inkscape:cy="225.21351"
         inkscape:window-width="1854"
         inkscape:window-height="1011"
         inkscape:window-x="66"
         inkscape:window-y="32"
         inkscape:window-maximized="1"
         inkscape:current-layer="layer1" />
      <defs
         id="defs1" />
      <g
         inkscape:label="Capa 1"
         inkscape:groupmode="layer"
         id="layer1">
        <path
           style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:round;stroke-linejoin:round"
           id="path1"
           sodipodi:type="arc"
           sodipodi:cx="30.883562"
           sodipodi:cy="34.397259"
           sodipodi:rx="19.602739"
           sodipodi:ry="19.602739"
           sodipodi:start="2.7699416"
           sodipodi:end="2.6877779"
           sodipodi:open="true"
           sodipodi:arc-type="arc"
           d="M 12.619121,41.516077 A 19.602739,19.602739 0 0 1 23.391103,16.282887 19.602739,19.602739 0 0 1 48.840221,26.534321 19.602739,19.602739 0 0 1 39.113662,52.188629 19.602739,19.602739 0 0 1 13.264987,42.991048" />
      </g>
    </svg>
  </body>
</html>
```

### dibujo
<small>Creado: 2026-02-17 17:07</small>

`dibujo.svg`

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   width="210mm"
   height="297mm"
   viewBox="0 0 210 297"
   version="1.1"
   id="svg1"
   inkscape:version="1.4.2 (1:1.4.2+202505120737+ebf0e940d0)"
   sodipodi:docname="dibujo.svg"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <sodipodi:namedview
     id="namedview1"
     pagecolor="#ffffff"
     bordercolor="#000000"
     borderopacity="0.25"
     inkscape:showpageshadow="2"
     inkscape:pageopacity="0.0"
     inkscape:pagecheckerboard="0"
     inkscape:deskcolor="#d1d1d1"
     inkscape:document-units="mm"
     inkscape:zoom="1.4142136"
     inkscape:cx="178.89801"
     inkscape:cy="225.21351"
     inkscape:window-width="1854"
     inkscape:window-height="1011"
     inkscape:window-x="66"
     inkscape:window-y="32"
     inkscape:window-maximized="1"
     inkscape:current-layer="layer1" />
  <defs
     id="defs1" />
  <g
     inkscape:label="Capa 1"
     inkscape:groupmode="layer"
     id="layer1">
    <path
       style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:round;stroke-linejoin:round"
       id="path1"
       sodipodi:type="arc"
       sodipodi:cx="30.883562"
       sodipodi:cy="34.397259"
       sodipodi:rx="19.602739"
       sodipodi:ry="19.602739"
       sodipodi:start="2.7699416"
       sodipodi:end="2.6877779"
       sodipodi:open="true"
       sodipodi:arc-type="arc"
       d="M 12.619121,41.516077 A 19.602739,19.602739 0 0 1 23.391103,16.282887 19.602739,19.602739 0 0 1 48.840221,26.534321 19.602739,19.602739 0 0 1 39.113662,52.188629 19.602739,19.602739 0 0 1 13.264987,42.991048" />
  </g>
</svg>
```


<a id="derechos-de-la-propiedad-intelectual-licencias-ley-de-la-propiedad-intelectual-derechos-de-autor"></a>
## Derechos de la propiedad intelectual. Licencias. Ley de la propiedad intelectual. Derechos de autor.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/003-Implantaci%C3%B3n%20de%20contenido%20multimedia/002-Derechos%20de%20la%20propiedad%20intelectual.%20Licencias.%20Ley%20de%20la%20propiedad%20intelectual.%20Derechos%20de%20autor.)


<a id="imagenes-software-para-crear-y-procesar-imagenes-formatos-conversiones"></a>
## Imágenes. Software para crear y procesar imágenes. Formatos. Conversiones

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/003-Implantaci%C3%B3n%20de%20contenido%20multimedia/003-Im%C3%A1genes.%20Software%20para%20crear%20y%20procesar%20im%C3%A1genes.%20Formatos.%20Conversiones)


<a id="optimizacion-de-imagenes-para-la-web"></a>
## Optimización de imágenes para la web.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/003-Implantaci%C3%B3n%20de%20contenido%20multimedia/004-Optimizaci%C3%B3n%20de%20im%C3%A1genes%20para%20la%20web.)

### cargamos la imagen
<small>Creado: 2026-02-17 17:14</small>

`002-cargamos la imagen.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <img src="josevicente.jpg">
  </body>
</html>
```

### escalo la imagen
<small>Creado: 2026-02-17 17:16</small>

`003-escalo la imagen.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      img{width:30%;}
    </style>
  </head>
  <body>
    <img src="josevicente.jpg">
  </body>
</html>
```

### solucion buena
<small>Creado: 2026-02-17 17:18</small>

`004-solucion buena.html`

```html
Vamos a abrir GIMP y usamos la opción de reescalar

400x600 por ejemplo
```

### cargo imagen escalada
<small>Creado: 2026-02-17 17:20</small>

`005-cargo imagen escalada.html`

```html
<!doctype html>
<html>
  <head>
    <style>
    
    </style>
  </head>
  <body>
    <img src="josevicentepequeno.jpg">
  </body>
</html>
```


<a id="audio-formatos-conversiones-de-formatos"></a>
## Audio: formatos. Conversiones de formatos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/003-Implantaci%C3%B3n%20de%20contenido%20multimedia/005-Audio%3A%20formatos.%20Conversiones%20de%20formatos)

### insertar audio en web
<small>Creado: 2026-02-17 18:22</small>

`003-insertar audio en web.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <audio src="Let you go.mp3"></audio>
  </body>
</html>
```

### ahora quiero controles
<small>Creado: 2026-02-17 18:22</small>

`004-ahora quiero controles.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <audio src="Let you go.mp3" controls></audio>
  </body>
</html>
```

### audio en Javascript
<small>Creado: 2026-02-17 18:25</small>

`005-audio en Javascript.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <script>
      let audio = new Audio();
      audio.src = "Let you go.mp3";
      audio.play()
    </script>
  </body>
</html>
```

### mejor costumbre
<small>Creado: 2026-02-17 18:28</small>

`006-mejor costumbre.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <button id="play">Play</button>
    <button id="pausa">Pausa</button>
    <script>
      let audio = new Audio();
      audio.src = "Let you go.mp3";
      document.querySelector("#play").onclick = function(){
        console.log("ok play")
      	audio.play()
      }
      document.querySelector("#pausa").onclick = function(){
      	audio.pause()
      }
    </script>
  </body>
</html>
```

### reproductor
<small>Creado: 2026-02-17 18:35</small>

`007-reproductor.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      #reproductor{
      	width:300px;
      }
      #reproductor img{width:100%;}
    </style>
  </head>
  <body>
    <div id="reproductor">
      <div id="portada">
        <img src="portada.png">
      </div>
      <button id="play">Play</button>
      <button id="pausa">Pausa</button>
    </div>
    <script>
      let audio = new Audio();
      audio.src = "Let you go.mp3";
      document.querySelector("#play").onclick = function(){
        console.log("ok play")
      	audio.play()
      }
      document.querySelector("#pausa").onclick = function(){
      	audio.pause()
      }
    </script>
  </body>
</html>
```

### rango
<small>Creado: 2026-02-17 18:46</small>

`008-rango.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      #reproductor{
      	width:300px;
      }
      #reproductor img{width:100%;}
      #rango{width:100%;}
    </style>
  </head>
  <body>
    <div id="reproductor">
      <div id="portada">
        <img src="portada.png">
      </div>
      <input type="range" id="rango">
      <button id="play">Play</button>
      <button id="pausa">Pausa</button>
    </div>
    <script>
      let audio = new Audio();
      let rango = document.querySelector("#rango")
      let temporizador;
      rango.value = 0
      audio.src = "Let you go.mp3";
      console.log(audio)
      document.querySelector("#play").onclick = function(){
        console.log("ok play")
        console.log(audio)
      	audio.play()
        temporizador = setTimeout("bucle()",1000)
      }
      document.querySelector("#pausa").onclick = function(){
      	audio.pause()
      }
      function bucle(){

        rango.value = (audio.currentTime/audio.duration)*100
      	clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",1000)
      }
    </script>
  </body>
</html>
```

### rango tambien controla
<small>Creado: 2026-02-17 18:48</small>

`009-rango tambien controla.html`

```html
<!doctype html>
<html>
  <head>
    <style>
      #reproductor{
      	width:300px;
      }
      #reproductor img{width:100%;}
      #rango{width:100%;}
    </style>
  </head>
  <body>
    <div id="reproductor">
      <div id="portada">
        <img src="portada.png">
      </div>
      <input type="range" id="rango">
      <button id="play">Play</button>
      <button id="pausa">Pausa</button>
    </div>
    <script>
      let audio = new Audio();
      let rango = document.querySelector("#rango")
      let temporizador;
      rango.value = 0
      audio.src = "Let you go.mp3";
      console.log(audio)
      document.querySelector("#play").onclick = function(){
        console.log("ok play")
        console.log(audio)
      	audio.play()
        temporizador = setTimeout("bucle()",1000)
      }
      document.querySelector("#pausa").onclick = function(){
      	audio.pause()
      }
      rango.onchange = function(){
      	audio.currentTime = this.value*(audio.duration/100)
      }
      function bucle(){
		
        rango.value = (audio.currentTime/audio.duration)*100
      	clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",1000)
      }
    </script>
  </body>
</html>
```

### ia
<small>Creado: 2026-02-17 18:53</small>

`010-ia.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Reproductor tipo Spotify</title>
    <style>
      :root{
        --bg:#121212;
        --panel:#181818;
        --panel2:#202020;
        --text:#eaeaea;
        --muted:#b3b3b3;
        --green:#1db954;
        --line:#2a2a2a;
        --shadow: 0 10px 30px rgba(0,0,0,.35);
        --radius:16px;
        --font: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, "Noto Sans", Arial, sans-serif;
      }
      body{
        margin:0;
        min-height:100vh;
        display:grid;
        place-items:center;
        background: radial-gradient(1200px 600px at 20% 10%, rgba(29,185,84,.18), transparent 60%),
                    radial-gradient(900px 500px at 80% 70%, rgba(255,255,255,.06), transparent 60%),
                    var(--bg);
        font-family:var(--font);
        color:var(--text);
      }

      .player{
        width:min(920px, 92vw);
        background: linear-gradient(180deg, rgba(255,255,255,.04), transparent 40%), var(--panel);
        border:1px solid rgba(255,255,255,.06);
        border-radius:var(--radius);
        box-shadow:var(--shadow);
        overflow:hidden;
      }

      .top{
        display:grid;
        grid-template-columns: 1.2fr 2fr 1.2fr;
        gap:16px;
        padding:16px;
        align-items:center;
      }

      .track{
        display:flex;
        gap:12px;
        align-items:center;
        min-width:0;
      }
      .cover{
        width:64px;
        height:64px;
        border-radius:12px;
        overflow:hidden;
        background:var(--panel2);
        flex:0 0 auto;
        border:1px solid rgba(255,255,255,.08);
      }
      .cover img{
        width:100%;
        height:100%;
        object-fit:cover;
        display:block;
      }
      .meta{
        min-width:0;
      }
      .title{
        font-weight:650;
        font-size:14px;
        line-height:1.2;
        white-space:nowrap;
        overflow:hidden;
        text-overflow:ellipsis;
      }
      .artist{
        margin-top:4px;
        font-size:12px;
        color:var(--muted);
        white-space:nowrap;
        overflow:hidden;
        text-overflow:ellipsis;
      }
      .like{
        margin-left:6px;
        width:34px;
        height:34px;
        border-radius:999px;
        display:grid;
        place-items:center;
        background:transparent;
        border:1px solid rgba(255,255,255,.08);
        color:var(--muted);
        cursor:pointer;
      }
      .like[data-on="1"]{
        border-color:rgba(29,185,84,.35);
        color:var(--green);
      }

      .center{
        display:flex;
        flex-direction:column;
        gap:10px;
        align-items:center;
      }

      .controls{
        display:flex;
        align-items:center;
        justify-content:center;
        gap:10px;
      }
      .btn{
        width:36px;
        height:36px;
        border-radius:999px;
        background:transparent;
        border:1px solid rgba(255,255,255,.10);
        color:var(--text);
        cursor:pointer;
        display:grid;
        place-items:center;
      }
      .btn:hover{
        border-color:rgba(255,255,255,.22);
      }
      .btn.small{
        width:34px;height:34px;
        color:var(--muted);
      }
      .btn.small[data-on="1"]{
        color:var(--green);
        border-color:rgba(29,185,84,.35);
      }
      .btn.play{
        width:44px;height:44px;
        border:none;
        background:var(--green);
        color:#0b0b0b;
        box-shadow: 0 12px 22px rgba(29,185,84,.25);
      }
      .btn.play:hover{
        filter:brightness(1.05);
      }

      .timeline{
        width:min(520px, 100%);
        display:grid;
        grid-template-columns: 44px 1fr 44px;
        gap:10px;
        align-items:center;
        color:var(--muted);
        font-size:12px;
      }

      input[type="range"]{
        -webkit-appearance:none;
        appearance:none;
        width:100%;
        height:4px;
        border-radius:999px;
        background: linear-gradient(90deg, var(--green) var(--pct,0%), rgba(255,255,255,.18) var(--pct,0%));
        outline:none;
      }
      input[type="range"]::-webkit-slider-thumb{
        -webkit-appearance:none;
        appearance:none;
        width:12px;height:12px;
        border-radius:999px;
        background: var(--text);
        border:2px solid rgba(0,0,0,.25);
        opacity:0;
        transition:opacity .12s ease;
      }
      input[type="range"]:hover::-webkit-slider-thumb{ opacity:1; }
      input[type="range"]::-moz-range-thumb{
        width:12px;height:12px;
        border-radius:999px;
        background: var(--text);
        border:none;
        opacity:0;
      }
      input[type="range"]:hover::-moz-range-thumb{ opacity:1; }

      .right{
        display:flex;
        align-items:center;
        justify-content:flex-end;
        gap:10px;
      }
      .pill{
        background:rgba(255,255,255,.06);
        border:1px solid rgba(255,255,255,.08);
        border-radius:999px;
        padding:8px 10px;
        display:flex;
        align-items:center;
        gap:8px;
      }
      .vol{
        width:110px;
      }
      .muted{
        color:var(--muted);
        font-size:12px;
      }

      .bottom{
        border-top:1px solid rgba(255,255,255,.06);
        padding:10px 16px;
        display:flex;
        justify-content:space-between;
        align-items:center;
        background: rgba(0,0,0,.10);
      }
      .status{
        display:flex;
        gap:10px;
        align-items:center;
        color:var(--muted);
        font-size:12px;
      }
      .badge{
        color:#0b0b0b;
        background:var(--green);
        border-radius:999px;
        padding:4px 8px;
        font-weight:650;
        font-size:11px;
      }

      /* Iconos simples (sin librerías) */
      .i{ width:18px; height:18px; display:block; }
      .i svg{ width:18px;height:18px; display:block; }
      .btn.play .i svg{ width:20px;height:20px; }

      @media (max-width: 760px){
        .top{ grid-template-columns: 1fr; }
        .right{ justify-content:space-between; }
        .timeline{ width:100%; }
      }
    </style>
  </head>
  <body>
    <div class="player" id="player">
      <div class="top">
        <!-- Izquierda: track -->
        <div class="track">
          <div class="cover"><img id="cover" alt="Portada"></div>
          <div class="meta">
            <div class="title" id="title"></div>
            <div class="artist" id="artist"></div>
          </div>
          <button class="like" id="like" title="Me gusta" data-on="0" aria-label="Me gusta">
            <span class="i" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none">
                <path d="M12 21s-7-4.4-9.4-8.7C.7 8.5 2.7 5.5 6 5.2c1.6-.2 3.1.5 4 1.6.9-1.1 2.4-1.8 4-1.6 3.3.3 5.3 3.3 3.4 7.1C19 16.6 12 21 12 21z"
                      stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
              </svg>
            </span>
          </button>
        </div>

        <!-- Centro: controles + timeline -->
        <div class="center">
          <div class="controls">
            <button class="btn small" id="shuffle" title="Aleatorio" data-on="0" aria-label="Aleatorio">
              <span class="i"><svg viewBox="0 0 24 24" fill="none">
                <path d="M16 3h5v5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M4 7h4l10 10h3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M16 21h5v-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M4 17h4l3-3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M13 11l3-3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
              </svg></span>
            </button>

            <button class="btn" id="prev" title="Anterior" aria-label="Anterior">
              <span class="i"><svg viewBox="0 0 24 24" fill="none">
                <path d="M7 6v12" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M18 6l-9 6 9 6V6z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
              </svg></span>
            </button>

            <button class="btn play" id="play" title="Reproducir/Pausar" aria-label="Reproducir/Pausar">
              <span class="i" id="playIcon"></span>
            </button>

            <button class="btn" id="next" title="Siguiente" aria-label="Siguiente">
              <span class="i"><svg viewBox="0 0 24 24" fill="none">
                <path d="M17 6v12" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M6 6l9 6-9 6V6z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
              </svg></span>
            </button>

            <button class="btn small" id="repeat" title="Repetir: off" data-mode="off" aria-label="Repetir">
              <span class="i" id="repeatIcon"></span>
            </button>
          </div>

          <div class="timeline">
            <div id="tCur" style="text-align:right;">0:00</div>
            <input type="range" id="seek" min="0" max="1000" value="0" />
            <div id="tDur">0:00</div>
          </div>
        </div>

        <!-- Derecha: volumen -->
        <div class="right">
          <div class="pill">
            <button class="btn small" id="mute" title="Silenciar" aria-label="Silenciar">
              <span class="i" id="volIcon"></span>
            </button>
            <input class="vol" type="range" id="volume" min="0" max="100" value="80" />
          </div>
        </div>
      </div>

      <div class="bottom">
        <div class="status">
          <span class="badge" id="stateBadge">PAUSA</span>
          <span class="muted" id="hint">Espacio: play/pausa · ←/→: -/+5s · ↑/↓: volumen</span>
        </div>
        <div class="muted" id="fileInfo"></div>
      </div>
    </div>

    <script>
      // === CONFIGURA AQUÍ ===
      const TRACKS = [
        {
          title: "Let you go",
          artist: "Artista",
          src: "Let you go.mp3",
          cover: "portada.png"
        }
        // Puedes añadir más pistas:
        // { title:"Tema 2", artist:"...", src:"tema2.mp3", cover:"cover2.jpg" },
      ];

      // === LÓGICA ===
      const audio = new Audio();
      audio.preload = "metadata";

      let index = 0;
      let seeking = false;

      const $ = (s) => document.querySelector(s);

      const cover = $("#cover");
      const title = $("#title");
      const artist = $("#artist");
      const like = $("#like");
      const shuffleBtn = $("#shuffle");
      const prevBtn = $("#prev");
      const playBtn = $("#play");
      const nextBtn = $("#next");
      const repeatBtn = $("#repeat");

      const seek = $("#seek");
      const tCur = $("#tCur");
      const tDur = $("#tDur");

      const volume = $("#volume");
      const muteBtn = $("#mute");

      const playIcon = $("#playIcon");
      const repeatIcon = $("#repeatIcon");
      const volIcon = $("#volIcon");

      const stateBadge = $("#stateBadge");
      const fileInfo = $("#fileInfo");

      function fmtTime(sec){
        if (!isFinite(sec) || sec < 0) return "0:00";
        const m = Math.floor(sec / 60);
        const s = Math.floor(sec % 60);
        return m + ":" + String(s).padStart(2, "0");
      }

      function setRangeVisual(el, pct01){
        const pct = Math.max(0, Math.min(100, pct01 * 100));
        el.style.setProperty("--pct", pct + "%");
      }

      function iconPlay(){
        return `
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M9 7l10 5-10 5V7z" fill="currentColor"/>
          </svg>`;
      }
      function iconPause(){
        return `
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M7 6h4v12H7V6zm6 0h4v12h-4V6z" fill="currentColor"/>
          </svg>`;
      }
      function iconRepeatOff(){
        return `
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M7 7h10l2 2v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
            <path d="M17 17H7l-2-2v-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
            <path d="M20 9l-2-2-2 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M4 15l2 2 2-2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>`;
      }
      function iconRepeatOne(){
        return `
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M7 7h10l2 2v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
            <path d="M17 17H7l-2-2v-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
            <path d="M20 9l-2-2-2 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M4 15l2 2 2-2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M12 10v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
            <path d="M12 10h1.8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
          </svg>`;
      }
      function iconVol(on){
        if(!on){
          return `
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M11 5L6 9H3v6h3l5 4V5z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
            <path d="M16 9l5 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
            <path d="M21 9l-5 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
          </svg>`;
        }
        return `
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M11 5L6 9H3v6h3l5 4V5z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
            <path d="M15.5 9.5a4 4 0 010 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
            <path d="M17.8 7.2a7 7 0 010 9.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
          </svg>`;
      }

      function loadTrack(i){
        index = (i + TRACKS.length) % TRACKS.length;
        const tr = TRACKS[index];
        audio.src = tr.src;
        title.textContent = tr.title || "Sin título";
        artist.textContent = tr.artist || "";
        cover.src = tr.cover || "";
        fileInfo.textContent = tr.src;

        // reset UI
        seek.value = 0;
        setRangeVisual(seek, 0);
        tCur.textContent = "0:00";
        tDur.textContent = "0:00";
        updatePlayUI();
      }

      function updatePlayUI(){
        const playing = !audio.paused;
        playIcon.innerHTML = playing ? iconPause() : iconPlay();
        stateBadge.textContent = playing ? "REPRODUCIENDO" : "PAUSA";
      }

      function setRepeatMode(mode){
        repeatBtn.dataset.mode = mode;
        if(mode === "off"){
          repeatBtn.title = "Repetir: off";
          repeatIcon.innerHTML = iconRepeatOff();
          repeatBtn.dataset.on = "0";
          audio.loop = false;
        }else if(mode === "one"){
          repeatBtn.title = "Repetir: one";
          repeatIcon.innerHTML = iconRepeatOne();
          repeatBtn.dataset.on = "1";
          audio.loop = true; // repite la misma
        }else{
          // "all" (lo gestionamos en 'ended')
          repeatBtn.title = "Repetir: all";
          repeatIcon.innerHTML = iconRepeatOff();
          repeatBtn.dataset.on = "1";
          audio.loop = false;
        }
      }

      function nextTrack(){
        if (shuffleBtn.dataset.on === "1" && TRACKS.length > 1){
          let n = index;
          while(n === index) n = Math.floor(Math.random() * TRACKS.length);
          loadTrack(n);
        }else{
          loadTrack(index + 1);
        }
        audio.play();
      }

      function prevTrack(){
        // si llevas más de 3s, vuelve al inicio; si no, anterior
        if (audio.currentTime > 3){
          audio.currentTime = 0;
        }else{
          loadTrack(index - 1);
          audio.play();
        }
      }

      // Eventos
      playBtn.addEventListener("click", async () => {
        if (audio.paused) await audio.play();
        else audio.pause();
      });

      prevBtn.addEventListener("click", prevTrack);
      nextBtn.addEventListener("click", nextTrack);

      shuffleBtn.addEventListener("click", () => {
        shuffleBtn.dataset.on = (shuffleBtn.dataset.on === "1") ? "0" : "1";
      });

      repeatBtn.addEventListener("click", () => {
        const mode = repeatBtn.dataset.mode;
        if (mode === "off") setRepeatMode("one");
        else if (mode === "one") setRepeatMode("all");
        else setRepeatMode("off");
      });

      like.addEventListener("click", () => {
        like.dataset.on = (like.dataset.on === "1") ? "0" : "1";
      });

      seek.addEventListener("input", () => {
        seeking = true;
        const dur = audio.duration;
        if (isFinite(dur) && dur > 0){
          const pct = Number(seek.value) / Number(seek.max);
          setRangeVisual(seek, pct);
          tCur.textContent = fmtTime(pct * dur);
        }
      });

      seek.addEventListener("change", () => {
        const dur = audio.duration;
        if (isFinite(dur) && dur > 0){
          const pct = Number(seek.value) / Number(seek.max);
          audio.currentTime = pct * dur;
        }
        seeking = false;
      });

      volume.addEventListener("input", () => {
        const v = Number(volume.value) / 100;
        audio.volume = v;
        setRangeVisual(volume, v);
        if (audio.muted && v > 0) audio.muted = false;
        volIcon.innerHTML = iconVol(!audio.muted);
      });

      muteBtn.addEventListener("click", () => {
        audio.muted = !audio.muted;
        volIcon.innerHTML = iconVol(!audio.muted);
      });

      audio.addEventListener("loadedmetadata", () => {
        tDur.textContent = fmtTime(audio.duration);
      });

      audio.addEventListener("timeupdate", () => {
        if (seeking) return;
        const dur = audio.duration;
        if (!isFinite(dur) || dur <= 0) return;
        const pct = audio.currentTime / dur;
        seek.value = Math.round(pct * Number(seek.max));
        setRangeVisual(seek, pct);
        tCur.textContent = fmtTime(audio.currentTime);
      });

      audio.addEventListener("play", updatePlayUI);
      audio.addEventListener("pause", updatePlayUI);

      audio.addEventListener("ended", () => {
        const mode = repeatBtn.dataset.mode;
        if (mode === "all" && TRACKS.length > 1){
          nextTrack();
          return;
        }
        // off: se queda en pausa al final
        updatePlayUI();
      });

      // Teclado: espacio play/pausa, flechas tiempo, volumen
      window.addEventListener("keydown", (e) => {
        const tag = (e.target && e.target.tagName) ? e.target.tagName.toLowerCase() : "";
        if (tag === "input" || tag === "textarea") return;

        if (e.code === "Space"){
          e.preventDefault();
          playBtn.click();
        }else if (e.code === "ArrowRight"){
          audio.currentTime = Math.min(audio.currentTime + 5, audio.duration || audio.currentTime + 5);
        }else if (e.code === "ArrowLeft"){
          audio.currentTime = Math.max(audio.currentTime - 5, 0);
        }else if (e.code === "ArrowUp"){
          e.preventDefault();
          volume.value = Math.min(100, Number(volume.value) + 5);
          volume.dispatchEvent(new Event("input"));
        }else if (e.code === "ArrowDown"){
          e.preventDefault();
          volume.value = Math.max(0, Number(volume.value) - 5);
          volume.dispatchEvent(new Event("input"));
        }
      });

      // Inicializa
      playIcon.innerHTML = iconPlay();
      setRepeatMode("off");
      audio.volume = Number(volume.value) / 100;
      setRangeVisual(volume, audio.volume);
      volIcon.innerHTML = iconVol(true);
      loadTrack(0);
    </script>
  </body>
</html>
```


<a id="video-codificacion-de-video-conversiones-de-formatos"></a>
## Vídeo: codificación de vídeo, conversiones de formatos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/003-Implantaci%C3%B3n%20de%20contenido%20multimedia/006-V%C3%ADdeo%3A%20codificaci%C3%B3n%20de%20v%C3%ADdeo%2C%20conversiones%20de%20formatos)

### video
<small>Creado: 2026-02-17 18:57</small>

`001-video.html`

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <video src="cerrar.mp4" controls></video>
  </body>
</html>
```


<a id="animaciones"></a>
## Animaciones.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/003-Implantaci%C3%B3n%20de%20contenido%20multimedia/007-Animaciones.)


<a id="integracion-de-audio-y-video-en-una-animacion"></a>
## Integración de audio y vídeo en una animación.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/003-Implantaci%C3%B3n%20de%20contenido%20multimedia/008-Integraci%C3%B3n%20de%20audio%20y%20v%C3%ADdeo%20en%20una%20animaci%C3%B3n.)



<a id="integracion-de-contenido-interactivo"></a>
# Integración de contenido interactivo

<a id="elementos-interactivos"></a>
## Elementos interactivos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/004-Integraci%C3%B3n%20de%20contenido%20interactivo/001-Elementos%20interactivos.)


<a id="comportamientos-interactivos-comportamiento-de-los-elementos"></a>
## Comportamientos interactivos. Comportamiento de los elementos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/004-Integraci%C3%B3n%20de%20contenido%20interactivo/002-Comportamientos%20interactivos.%20Comportamiento%20de%20los%20elementos.)


<a id="ejecucion-de-secuencias-de-comandos"></a>
## Ejecución de secuencias de comandos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/004-Integraci%C3%B3n%20de%20contenido%20interactivo/003-Ejecuci%C3%B3n%20de%20secuencias%20de%20comandos.)


<a id="verificacion-del-funcionamiento-en-distintos-navegadores-y-dispositivos"></a>
## Verificación del funcionamiento en distintos navegadores y dispositivos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/004-Integraci%C3%B3n%20de%20contenido%20interactivo/004-Verificaci%C3%B3n%20del%20funcionamiento%20en%20distintos%20navegadores%20y%20dispositivos.)



<a id="diseno-de-webs-accesibles"></a>
# Diseño de webs accesibles

<a id="el-consorcio-world-wide-web-w3c"></a>
## El Consorcio World Wide Web (W3C).

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/005-Dise%C3%B1o%20de%20webs%20accesibles/001-El%20Consorcio%20World%20Wide%20Web%20%28W3C%29.)


<a id="principios-y-pautas-de-accesibilidad-al-contenido-en-la-web-wcag"></a>
## Principios y Pautas de Accesibilidad al Contenido en la Web (WCAG).

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/005-Dise%C3%B1o%20de%20webs%20accesibles/002-Principios%20y%20Pautas%20de%20Accesibilidad%20al%20Contenido%20en%20la%20Web%20%28WCAG%29.)


<a id="criterios-de-conformidad-niveles-de-conformidad"></a>
## Criterios de conformidad. Niveles de conformidad.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/005-Dise%C3%B1o%20de%20webs%20accesibles/003-Criterios%20de%20conformidad.%20Niveles%20de%20conformidad.)


<a id="tecnicas-para-satisfacer-los-requisitos-definidos-en-las-wcag"></a>
## Técnicas para satisfacer los requisitos definidos en las WCAG.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/005-Dise%C3%B1o%20de%20webs%20accesibles/004-T%C3%A9cnicas%20para%20satisfacer%20los%20requisitos%20definidos%20en%20las%20WCAG.)


<a id="prioridades-puntos-de-verificacion"></a>
## Prioridades. Puntos de verificación.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/005-Dise%C3%B1o%20de%20webs%20accesibles/005-Prioridades.%20Puntos%20de%20verificaci%C3%B3n.)


<a id="metodos-para-realizar-revisiones-preliminares-y-evaluaciones-de-adecuacion-o-conformidad-de-documentos-web"></a>
## Métodos para realizar revisiones preliminares y evaluaciones de adecuación o conformidad de documentos web.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/005-Dise%C3%B1o%20de%20webs%20accesibles/006-M%C3%A9todos%20para%20realizar%20revisiones%20preliminares%20y%20evaluaciones%20de%20adecuaci%C3%B3n%20o%20conformidad%20de%20documentos%20web.)


<a id="herramientas-de-analisis-de-accesibilidad-web"></a>
## Herramientas de análisis de accesibilidad web.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/005-Dise%C3%B1o%20de%20webs%20accesibles/007-Herramientas%20de%20an%C3%A1lisis%20de%20accesibilidad%20web.)


<a id="chequeo-de-la-accesibilidad-web-desde-diferentes-navegadores-y-dispositivos"></a>
## Chequeo de la accesibilidad web desde diferentes navegadores y dispositivos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/005-Dise%C3%B1o%20de%20webs%20accesibles/008-Chequeo%20de%20la%20accesibilidad%20web%20desde%20diferentes%20navegadores%20y%20dispositivos.)


<a id="posicionamiento-en-buscadores-mejora-de-la-visibilidad-de-un-sitio-web-en-diferentes-buscadores"></a>
## Posicionamiento en buscadores. Mejora de la visibilidad de un sitio web en diferentes buscadores.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/005-Dise%C3%B1o%20de%20webs%20accesibles/009-Posicionamiento%20en%20buscadores.%20Mejora%20de%20la%20visibilidad%20de%20un%20sitio%20web%20en%20diferentes%20buscadores.)



<a id="implementacion-de-la-usabilidad-en-la-web-diseno-amigable"></a>
# Implementación de la usabilidad en la web. Diseño amigable

<a id="analisis-de-la-usabilidad-tecnicas"></a>
## Análisis de la usabilidad. Técnicas.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/001-An%C3%A1lisis%20de%20la%20usabilidad.%20T%C3%A9cnicas.)


<a id="identificacion-del-objetivo-de-la-web"></a>
## Identificación del objetivo de la web.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/002-Identificaci%C3%B3n%20del%20objetivo%20de%20la%20web.)


<a id="tipos-de-usuario"></a>
## Tipos de usuario.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/003-Tipos%20de%20usuario.)


<a id="barreras-identificadas-por-los-usuarios"></a>
## Barreras identificadas por los usuarios.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/004-Barreras%20identificadas%20por%20los%20usuarios.)


<a id="informacion-facilmente-accesible"></a>
## Información fácilmente accesible.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/005-Informaci%C3%B3n%20f%C3%A1cilmente%20accesible.)


<a id="velocidad-de-conexion"></a>
## Velocidad de conexión.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/006-Velocidad%20de%20conexi%C3%B3n.)


<a id="importancia-del-uso-de-estandares-externos"></a>
## Importancia del uso de estándares externos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/007-Importancia%20del%20uso%20de%20est%C3%A1ndares%20externos.)


<a id="navegacion-facilmente-recordada-frente-a-navegacion-redescubierta"></a>
## Navegación fácilmente recordada frente a navegación redescubierta.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/008-Navegaci%C3%B3n%20f%C3%A1cilmente%20recordada%20frente%20a%20navegaci%C3%B3n%20redescubierta.)


<a id="facilidad-de-navegacion-en-la-web"></a>
## Facilidad de navegación en la web.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/009-Facilidad%20de%20navegaci%C3%B3n%20en%20la%20web.)


<a id="verificacion-de-la-usabilidad-en-diferentes-navegadores-y-tecnologias"></a>
## Verificación de la usabilidad en diferentes navegadores y tecnologías.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/010-Verificaci%C3%B3n%20de%20la%20usabilidad%20en%20diferentes%20navegadores%20y%20tecnolog%C3%ADas.)


<a id="herramientas-y-test-de-verificacion-1"></a>
## Herramientas y test de verificación.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/006-Implementaci%C3%B3n%20de%20la%20usabilidad%20en%20la%20web.%20Dise%C3%B1o%20amigable/011-Herramientas%20y%20test%20de%20verificaci%C3%B3n.)



<a id="git"></a>
# .git

<a id="branches"></a>
## branches

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/.git/branches)


<a id="hooks"></a>
## hooks

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/.git/hooks)


<a id="info"></a>
## info

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/.git/info)


<a id="logs"></a>
## logs

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/.git/logs)


<a id="objects"></a>
## objects

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/.git/objects)


<a id="refs"></a>
## refs

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/interfacesweb/tree/main/.git/refs)
