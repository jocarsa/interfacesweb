<?php
header("Content-Type: application/json; charset=utf-8");

$question = trim($_POST["question"] ?? "");
if ($question === "") {
  echo json_encode(["ok" => false, "error" => "Empty question"]);
  exit;
}

// Build prompt (keep it simple)
$prompt = "Responde en español, en un solo párrafo y sin código.\n\nPregunta: ".$question;

$data = [
  "model"  => "ministral-3:3b",
  "prompt" => $prompt,
  "stream" => false
];

$ch = curl_init("http://localhost:11434/api/generate");
curl_setopt_array($ch, [
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_POST           => true,
  CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
  CURLOPT_POSTFIELDS     => json_encode($data, JSON_UNESCAPED_UNICODE),
  CURLOPT_TIMEOUT        => 120,
]);

$response = curl_exec($ch);

if ($response === false) {
  $err = curl_error($ch);
  curl_close($ch);
  echo json_encode(["ok" => false, "error" => "Curl error: ".$err]);
  exit;
}

$http = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($http < 200 || $http >= 300) {
  echo json_encode(["ok" => false, "error" => "HTTP ".$http, "raw" => $response]);
  exit;
}

$result = json_decode($response, true);
if (!is_array($result) || !isset($result["response"])) {
  echo json_encode(["ok" => false, "error" => "Bad JSON from Ollama", "raw" => $response]);
  exit;
}

echo json_encode([
  "ok" => true,
  "answer" => $result["response"]
], JSON_UNESCAPED_UNICODE);