console.log("Vamos con la accesibilidad")

window.onload = function(){

  let zoom = 1;
  let invertido = false;
  let contraste = false;
  let fuenteGrande = false;

  console.log("Esto solo carga cuando la ventana haya cargado")

  let barra = document.createElement("div")
  barra.classList.add("jocarsa-accesibilidad")

  let cuerpo = document.querySelector("body")
  cuerpo.appendChild(barra)

  // ------------------------
  // ZOOM IN
  // ------------------------
  let zoomin = document.createElement("div")
  zoomin.textContent = "🔍"
  barra.appendChild(zoomin)

  zoomin.onclick = function(){
    if(zoom < 2){
      zoom += 0.1
      cuerpo.style.zoom = zoom
      console.log("Zoom:", zoom)
    }
  }

  // ------------------------
  // ZOOM OUT
  // ------------------------
  let zoomout = document.createElement("div")
  zoomout.textContent = "🔎"
  barra.appendChild(zoomout)

  zoomout.onclick = function(){
    if(zoom > 0.5){
      zoom -= 0.1
      cuerpo.style.zoom = zoom
      console.log("Zoom:", zoom)
    }
  }

  // ------------------------
  // INVERTIR COLORES
  // ------------------------
  let invertir = document.createElement("div")
  invertir.textContent = "🧙‍♂️"
  barra.appendChild(invertir)

  invertir.onclick = function(){
    invertido = !invertido
    aplicarFiltros()
  }

  // ------------------------
  // CONTRASTE ALTO
  // ------------------------
  let contrasteBtn = document.createElement("div")
  contrasteBtn.textContent = "⚫"
  barra.appendChild(contrasteBtn)

  contrasteBtn.onclick = function(){
    contraste = !contraste
    aplicarFiltros()
  }

  // ------------------------
  // FUENTE GRANDE
  // ------------------------
  let fuenteBtn = document.createElement("div")
  fuenteBtn.textContent = "A"
  barra.appendChild(fuenteBtn)

  fuenteBtn.onclick = function(){
    if(fuenteGrande == false){
      fuenteGrande = true
      cuerpo.style.fontSize = "1.3em"
      cuerpo.style.lineHeight = "1.6em"
    }else{
      fuenteGrande = false
      cuerpo.style.fontSize = ""
      cuerpo.style.lineHeight = ""
    }
  }

  // ------------------------
  // RESET
  // ------------------------
  let reset = document.createElement("div")
  reset.textContent = "↺"
  barra.appendChild(reset)

  reset.onclick = function(){
    zoom = 1
    invertido = false
    contraste = false
    fuenteGrande = false

    cuerpo.style.zoom = 1
    cuerpo.style.filter = ""
    cuerpo.style.fontSize = ""
    cuerpo.style.lineHeight = ""
  }

  // ------------------------
  // FUNCIÓN FILTROS
  // ------------------------
  function aplicarFiltros(){

    let filtros = ""

    if(invertido){
      filtros += " invert(1)"
    }

    if(contraste){
      filtros += " contrast(1.5)"
    }

    cuerpo.style.filter = filtros
  }

}