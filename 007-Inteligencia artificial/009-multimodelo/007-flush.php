<?php

function llamarOllama($model, $prompt) {
    $data = [
        "model" => $model,
        "prompt" => $prompt,
        "stream" => false
    ];

    $ch = curl_init("http://localhost:11434/api/generate");

    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => ["Content-Type: application/json"],
        CURLOPT_POSTFIELDS => json_encode($data),
    ]);

    $response = curl_exec($ch);

    if ($response === false) {
        return "Error CURL: " . curl_error($ch);
    }

    curl_close($ch);

    $result = json_decode($response, true);

    return $result["response"] ?? "";
}

if (isset($_GET["api"]) && $_GET["api"] === "generar") {
    header("Content-Type: application/json; charset=UTF-8");

    $tema = trim($_POST["tema"] ?? "");
    $lenguaje = trim($_POST["lenguaje"] ?? "Python");

    if ($tema === "") {
        echo json_encode(["ok" => false, "error" => "Tema vacío"]);
        exit;
    }

    $explicacion = llamarOllama(
        "qwen2.5:3b-instruct",
        "Proporciona una explicación en texto, párrafo, sin código, de: $tema en $lenguaje"
    );

    $codigo = llamarOllama(
        "qwen2.5-coder:7b",
        "Proporciona un ejemplo de código, sin explicación, de: $tema en $lenguaje"
    );

    echo json_encode([
        "ok" => true,
        "tema" => $tema,
        "explicacion" => $explicacion,
        "codigo" => $codigo
    ]);

    exit;
}

$temas = file("asignatura.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

?>
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Generador</title>

<style>
body {
    margin: 0;
    padding: 30px;
    background: #f4f4f7;
    font-family: Ubuntu, Arial, sans-serif;
}

section {
    max-width: 900px;
    margin: 30px auto;
    padding: 30px;
    background: white;
    border-radius: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

h1 {
    color: indigo;
    margin-top: 0;
}

h2 {
    color: darkorange;
}

p {
    text-align: justify;
    line-height: 1.8;
    color: #333;
}

pre {
    background: #1e1e1e;
    color: #eeeeee;
    padding: 20px;
    border-radius: 10px;
    overflow: auto;
}

.estado {
    max-width: 900px;
    margin: 20px auto;
    color: indigo;
    font-weight: bold;
}
</style>
</head>

<body>

<div class="estado" id="estado">Preparando generación...</div>
<div id="resultados"></div>

<script>
const temas = <?php echo json_encode($temas, JSON_UNESCAPED_UNICODE); ?>;
const lenguaje = "Python";
const resultados = document.getElementById("resultados");
const estado = document.getElementById("estado");

function escapar(texto) {
    return texto
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}

async function generarUno(tema, indice) {
    estado.innerHTML = `Generando ${indice + 1} de ${temas.length}: <strong>${escapar(tema)}</strong>`;

    const formData = new FormData();
    formData.append("tema", tema);
    formData.append("lenguaje", lenguaje);

    const respuesta = await fetch("?api=generar", {
        method: "POST",
        body: formData
    });

    const data = await respuesta.json();

    if (!data.ok) {
        resultados.innerHTML += `<section><h1>Error</h1><p>${escapar(data.error)}</p></section>`;
        return;
    }

    resultados.innerHTML += `
        <section>
            <h1>${escapar(data.tema)}</h1>

            <h2>Explicación</h2>
            <p>${escapar(data.explicacion).replaceAll("\\n", "<br>")}</p>

            <h2>Código</h2>
            <pre><code>${escapar(data.codigo)}</code></pre>
        </section>
    `;

    window.scrollTo(0, document.body.scrollHeight);
}

async function iniciar() {
    for (let i = 0; i < temas.length; i++) {
        await generarUno(temas[i], i);
    }

    estado.innerHTML = "Generación terminada.";
}

iniciar();
</script>

</body>
</html>