<?php

$api_key = trim(file_get_contents("clave.txt"));

$data = [
    "model" => "gpt-5-mini",
    "input" => "Qué es CEAC FP?"
];

$ch = curl_init("https://api.openai.com/v1/responses");

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json",
    "Authorization: Bearer " . $api_key
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

$response = curl_exec($ch);
curl_close($ch);

$json = json_decode($response, true);

echo $json["output"][1]["content"][0]["text"] ?? "No response";