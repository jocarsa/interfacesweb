<?php
// Generamos una llamada al servidor

$ch = curl_init("http://localhost:11434/api/generate");

// Elegimos modelo, le enviamos una pregunta, elegimos streaming
$sistema = "
	Te voy a proporcionar un texto. Para ese texto:
  - Formatealo correctamente
  - Manten todas mis palabras
  - Pon signos de puntuación, interrogación, etc, como sea necesario
  - No cambies mis expresiones ni mis palabras, solo formatea correctamente
  - El mensaje que vas a recibir es un correo electrónico. 
  - Formatealo debidamente con separaciones de párrafos por tema y saludo y despedida.
  Y el mensaje es:
";
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
    "model" => "phi4-mini:latest",
    "prompt" => $sistema.$_GET['mensaje'],
    "stream" => false
]));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Lanza la respuesta en pantalla

echo json_decode(curl_exec($ch), true)["response"];