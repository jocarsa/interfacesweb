<?php
/**
 * Cosine similarity con embeddings de Ollama (nomic-embed-text:v1.5)
 * Compara automáticamente TODOS los pares posibles (sin repetidos)
 */

header("Content-Type: application/json; charset=utf-8");

$OLLAMA_URL = "http://localhost:11434/api/embeddings";
$MODEL      = "nomic-embed-text:v1.5";

$textos = ["alma","ameba","plutón","enfado","junio","célula"];

/** Obtiene embedding desde Ollama */
function ollama_embedding(string $url, string $model, string $texto): array {
    $data = [
        "model"  => $model,
        "prompt" => $texto
    ];

    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
        CURLOPT_POSTFIELDS     => json_encode($data, JSON_UNESCAPED_UNICODE),
        CURLOPT_TIMEOUT        => 60
    ]);

    $response = curl_exec($ch);
    if ($response === false) {
        $err = curl_error($ch);
        curl_close($ch);
        throw new RuntimeException("Curl error: $err");
    }

    $http = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($http < 200 || $http >= 300) {
        throw new RuntimeException("HTTP $http: $response");
    }

    $result = json_decode($response, true);
    if (!is_array($result)) {
        throw new RuntimeException("JSON decode error: $response");
    }

    $embedding = $result["embedding"] ?? null;
    if (!is_array($embedding) || count($embedding) === 0) {
        throw new RuntimeException("No se encontró 'embedding' en la respuesta: $response");
    }

    return array_map('floatval', $embedding);
}

/** Producto punto */
function dot(array $a, array $b): float {
    if (count($a) !== count($b)) {
        throw new InvalidArgumentException("Dimensiones distintas: ".count($a)." vs ".count($b));
    }
    $sum = 0.0;
    $n = count($a);
    for ($i = 0; $i < $n; $i++) {
        $sum += $a[$i] * $b[$i];
    }
    return $sum;
}

/** Norma L2 */
function norm(array $v): float {
    return sqrt(dot($v, $v));
}

/** Similitud coseno */
function cosine_similarity(array $a, array $b): float {
    $na = norm($a);
    $nb = norm($b);
    if ($na == 0.0 || $nb == 0.0) return 0.0;
    return dot($a, $b) / ($na * $nb);
}

/** Genera todos los pares únicos (i<j) */
function all_pairs(array $items): array {
    $pairs = [];
    $n = count($items);
    for ($i = 0; $i < $n; $i++) {
        for ($j = $i + 1; $j < $n; $j++) {
            $pairs[] = [$items[$i], $items[$j]];
        }
    }
    return $pairs;
}

try {
    // 1) Embeddings
    $emb = [];
    foreach ($textos as $t) {
        $emb[$t] = ollama_embedding($GLOBALS['OLLAMA_URL'], $GLOBALS['MODEL'], $t);
    }

    // 2) Todos los pares automáticamente
    $pairs = all_pairs($textos);

    $sims = [];
    foreach ($pairs as [$a, $b]) {
        $sims["$a-$b"] = cosine_similarity($emb[$a], $emb[$b]);
    }

    // (Opcional) Ordenar por similitud descendente
    arsort($sims);

    // 3) Respuesta
    echo json_encode([
        "model" => $MODEL,
        "dim"   => count($emb[$textos[0]]),
        "textos" => $textos,
        "pairs_count" => count($pairs),
        "cosine_similarity" => $sims
        // ,"embeddings" => $emb
    ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

} catch (Throwable $e) {
    http_response_code(500);
    echo json_encode([
        "error" => $e->getMessage()
    ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
}