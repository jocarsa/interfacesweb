<?php
$sistema = "Proporciona una explicación en texto, párrafo, sin código, de:";
$prompt = "Variables en PHP.";

$data = [
    "model"  => "qwen2.5:3b-instruct",
    "prompt" => $sistema.$prompt,
    "stream" => false
];

$ch = curl_init("http://localhost:11434/api/generate"); // Hago una petición a local
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
    CURLOPT_POSTFIELDS     => json_encode($data),
]);

$response = curl_exec($ch);                           // Ejecuto curl

if ($response === false) {
    die("Curl error: " . curl_error($ch));
}                                                     // Si hay respuesta

curl_close($ch);                                      // cierro curl
$result = json_decode($response, true);               // Paso la respuesta a json
echo $result["response"];                             // Y la pinto en pantalla

$sistema = "Proporciona un ejemplo de código, sin explicación, de:";
$prompt = "Variables en PHP.";

$data = [
    "model"  => "qwen2.5-coder:7b",
    "prompt" => $sistema.$prompt,
    "stream" => false
];

$ch = curl_init("http://localhost:11434/api/generate"); // Hago una petición a local
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
    CURLOPT_POSTFIELDS     => json_encode($data),
]);

$response = curl_exec($ch);                           // Ejecuto curl

if ($response === false) {
    die("Curl error: " . curl_error($ch));
}                                                     // Si hay respuesta

curl_close($ch);                                      // cierro curl
$result = json_decode($response, true);               // Paso la respuesta a json
echo $result["response"];                             // Y la pinto en pantalla
