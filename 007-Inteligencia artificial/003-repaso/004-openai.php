<?php

// Leer API key desde archivo
$api_key = trim(file_get_contents("clave.txt"));

// Endpoint de OpenAI (Responses API)
$url = "https://api.openai.com/v1/responses";

// Datos mínimos
$data = [
    "model" => "gpt-5-mini",
    "input" => "Hola, ¿qué tal?"
];

// Inicializar cURL
$ch = curl_init($url);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json",
    "Authorization: Bearer " . $api_key
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

// Ejecutar
$response = curl_exec($ch);
curl_close($ch);

// Mostrar respuesta completa
echo $response;