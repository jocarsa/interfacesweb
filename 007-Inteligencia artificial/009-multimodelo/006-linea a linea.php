<?php

function generarContenido($tema, $lenguaje) {

    // --------------------------------------------------
    // EXPLICACIÓN TEÓRICA
    // --------------------------------------------------

    $sistema_teoria = "Proporciona una explicación en texto, párrafo, sin código, de:";

    $prompt_teoria = $tema . " en " . $lenguaje;

    $data_teoria = [
        "model"  => "qwen2.5:3b-instruct",
        "prompt" => $sistema_teoria . " " . $prompt_teoria,
        "stream" => false
    ];

    $ch = curl_init("http://localhost:11434/api/generate");

    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
        CURLOPT_POSTFIELDS     => json_encode($data_teoria),
    ]);

    $response = curl_exec($ch);

    if ($response === false) {
        die("Curl error: " . curl_error($ch));
    }

    curl_close($ch);

    $result = json_decode($response, true);

    $explicacion = $result["response"] ?? "";



    // --------------------------------------------------
    // EJEMPLO DE CÓDIGO
    // --------------------------------------------------

    $sistema_codigo = "Proporciona un ejemplo de código, sin explicación, de:";

    $prompt_codigo = $tema . " en " . $lenguaje;

    $data_codigo = [
        "model"  => "qwen2.5-coder:7b",
        "prompt" => $sistema_codigo . " " . $prompt_codigo,
        "stream" => false
    ];

    $ch = curl_init("http://localhost:11434/api/generate");

    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
        CURLOPT_POSTFIELDS     => json_encode($data_codigo),
    ]);

    $response = curl_exec($ch);

    if ($response === false) {
        die("Curl error: " . curl_error($ch));
    }

    curl_close($ch);

    $result = json_decode($response, true);

    $codigo = $result["response"] ?? "";



    // --------------------------------------------------
    // OUTPUT HTML
    // --------------------------------------------------

    echo "
    <section style='
        font-family:Ubuntu,Arial,sans-serif;
        max-width:900px;
        margin:40px auto;
        padding:30px;
        background:white;
        border-radius:12px;
        box-shadow:0px 2px 10px rgba(0,0,0,0.1);
    '>

        <h1 style='
            color:indigo;
            margin-top:0;
        '>
            $tema
        </h1>

        <h2 style='
            color:darkorange;
        '>
            Explicación
        </h2>

        <p style='
            text-align:justify;
            line-height:1.8;
            color:#333;
        '>
            " . nl2br(htmlspecialchars($explicacion)) . "
        </p>

        <h2 style='
            color:darkorange;
        '>
            Código
        </h2>

        <pre style='
            background:#1e1e1e;
            color:#eeeeee;
            padding:20px;
            border-radius:10px;
            overflow:auto;
        '><code>" . htmlspecialchars($codigo) . "</code></pre>

    </section>
    ";
}



// --------------------------------------------------
// EJEMPLOS DE USO
// --------------------------------------------------
$archivo = fopen("asignatura.txt", "r");
while (($linea = fgets($archivo)) !== false) {

        generarContenido($linea, "Python");

    }
fclose($archivo);

?>