<?php

function generarContenido($topic) {

    // --------------------------------------------------
    // EXPLICACIÓN TEÓRICA
    // --------------------------------------------------

    $sistema_teoria = "Proporciona una explicación en texto, párrafo, sin código, de:";
    
    $data_teoria = [
        "model"  => "qwen2.5:3b-instruct",
        "prompt" => $sistema_teoria . " " . $topic,
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

    $data_codigo = [
        "model"  => "qwen2.5-coder:7b",
        "prompt" => $sistema_codigo . " " . $topic,
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
    // DEVOLVER RESULTADO
    // --------------------------------------------------

    return [
        "explicacion" => $explicacion,
        "codigo"      => $codigo
    ];
}



// --------------------------------------------------
// EJEMPLO DE USO
// --------------------------------------------------

$resultado = generarContenido("Variables en PHP");

echo "<h1>Explicación</h1>";
echo "<p>" . nl2br(htmlspecialchars($resultado["explicacion"])) . "</p>";

echo "<h1>Código</h1>";
echo "<pre><code>" . htmlspecialchars($resultado["codigo"]) . "</code></pre>";

$resultado = generarContenido("Operadores en PHP");

echo "<h1>Explicación</h1>";
echo "<p>" . nl2br(htmlspecialchars($resultado["explicacion"])) . "</p>";

echo "<h1>Código</h1>";
echo "<pre><code>" . htmlspecialchars($resultado["codigo"]) . "</code></pre>";

?>