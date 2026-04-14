<?php
// Generamos una llamada al servidor

$ch = curl_init("http://localhost:11434/api/generate");

// Elegimos modelo, le enviamos una pregunta, elegimos streaming

curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
    "model" => "phi4-mini:latest",
    "prompt" => "Que es la informática?",
    "stream" => false
]));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Lanza la respueesta en pantalla

echo json_decode(curl_exec($ch), true)["response"];