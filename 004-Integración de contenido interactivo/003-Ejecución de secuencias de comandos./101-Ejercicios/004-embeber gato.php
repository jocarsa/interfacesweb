<?php
// Embeddings con Ollama: nomic-embed-text:v1.5 para el texto "perro"

$texto = "gato";

$data = [
    "model"  => "nomic-embed-text:v1.5",
    "prompt" => $texto
];

$ch = curl_init("http://localhost:11434/api/embeddings");
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
    CURLOPT_POSTFIELDS     => json_encode($data, JSON_UNESCAPED_UNICODE),
]);

$response = curl_exec($ch);
if ($response === false) {
    die("Curl error: " . curl_error($ch));
}
curl_close($ch);

$result = json_decode($response, true);
if (!is_array($result)) {
    die("JSON decode error");
}

// En Ollama, la clave suele ser "embedding" (vector numérico)
$embedding = $result["embedding"] ?? null;
if (!$embedding || !is_array($embedding)) {
    // Por si tu versión devuelve otra estructura
    die("No se encontró 'embedding' en la respuesta: " . htmlspecialchars($response));
}

// Imprime el vector (útil para depurar)
header("Content-Type: application/json; charset=utf-8");
echo json_encode([
    "texto"     => $texto,
    "dim"       => count($embedding),
    "embedding" => $embedding
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);