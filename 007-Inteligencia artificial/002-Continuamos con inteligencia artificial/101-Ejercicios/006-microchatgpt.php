<?php
// index.php - MicroChatGPT con Ollama (session chat)
session_start();

function h($s){ return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }

if(!isset($_SESSION["chat"])) $_SESSION["chat"] = [];

if(isset($_GET["reset"])){
	$_SESSION["chat"] = [];
	header("Location: ".$_SERVER["PHP_SELF"]);
	exit;
}

$pregunta = trim((string)($_GET["pregunta"] ?? ""));
$respuesta = null;
$error = null;

if($pregunta !== ""){
	// Guardar mensaje del usuario
	$_SESSION["chat"][] = ["role" => "user", "content" => $pregunta];

	// Opcional: contexto mínimo usando historial (simple)
	// Ollama /api/generate acepta "prompt". Le pasamos el chat como texto:
	$contexto = "";
	foreach($_SESSION["chat"] as $m){
		if($m["role"] === "user") $contexto .= "Usuario: ".$m["content"]."\n";
		else                     $contexto .= "Asistente: ".$m["content"]."\n";
	}
	$contexto .= "Asistente: ";

	$data = [
		"model"  => "ministral-3:3b",
		"prompt" => $contexto,
		"stream" => false
	];

	$ch = curl_init("http://localhost:11434/api/generate");
	curl_setopt_array($ch, [
		CURLOPT_RETURNTRANSFER => true,
		CURLOPT_POST           => true,
		CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
		CURLOPT_POSTFIELDS     => json_encode($data),
		CURLOPT_TIMEOUT        => 120
	]);

	$response = curl_exec($ch);

	if($response === false){
		$error = "Curl error: ".curl_error($ch);
	}else{
		$result = json_decode($response, true);
		if(!is_array($result) || !isset($result["response"])){
			$error = "Respuesta inválida de Ollama.";
		}else{
			$respuesta = (string)$result["response"];
			$_SESSION["chat"][] = ["role" => "assistant", "content" => $respuesta];
		}
	}

	curl_close($ch);

	// Evitar reenvío al refrescar (PRG)
	header("Location: ".$_SERVER["PHP_SELF"]);
	exit;
}
?>
<!doctype html>
<html lang="es">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width,initial-scale=1">
	<title>MicroChatGPT (Ollama)</title>
	<style>
		body{ margin:0; font-family: ui-serif, Georgia, "Times New Roman", serif; background:#f6f7f8; color:#111; }
		header{ background:#05483f; color:#fff; padding:14px 18px; display:flex; gap:12px; align-items:center; }
		header b{ font-size:16px; }
		header a{ color:#fff; text-decoration:none; padding:6px 10px; border:1px solid rgba(255,255,255,.4); border-radius:10px; }
		.wrap{ max-width:900px; margin:0 auto; padding:18px; }
		.chat{ display:flex; flex-direction:column; gap:10px; padding-bottom:84px; }
		.msg{ max-width:80%; padding:12px 14px; border-radius:14px; line-height:1.35; white-space:pre-wrap; box-shadow:0 2px 8px rgba(0,0,0,.06); }
		.user{ align-self:flex-end; background:#05483f; color:#fff; border-bottom-right-radius:6px; }
		.bot{ align-self:flex-start; background:#fff; color:#111; border:1px solid #e6e6e6; border-bottom-left-radius:6px; }
		.footer{
			position:fixed; left:0; right:0; bottom:0;
			background:#ffffff; border-top:1px solid #e6e6e6;
			padding:12px;
		}
		form{ max-width:900px; margin:0 auto; display:flex; gap:10px; }
		input[type=text]{
			flex:1; padding:12px 14px; border:1px solid #d7d7d7;
			border-radius:12px; font-size:15px;
		}
		button{
			padding:12px 14px; border:0; border-radius:12px;
			background:#05483f; color:#fff; font-size:15px; cursor:pointer;
		}
		.hint{ max-width:900px; margin:10px auto 0; color:#666; font-size:13px; padding:0 2px; }
	</style>
</head>
<body>
	<header>
		<b>MicroChatGPT</b>
		<span style="opacity:.85">Ollama · ministral-3:3b</span>
		<span style="flex:1"></span>
		<a href="?reset=1">Nuevo chat</a>
	</header>

	<div class="wrap">
		<div class="chat">
			<?php if(empty($_SESSION["chat"])): ?>
				<div class="msg bot">Escribe una pregunta abajo.</div>
			<?php else: ?>
				<?php foreach($_SESSION["chat"] as $m): ?>
					<div class="msg <?= $m["role"] === "user" ? "user" : "bot" ?>"><?= h($m["content"]) ?></div>
				<?php endforeach; ?>
			<?php endif; ?>
		</div>
	</div>

	<div class="footer">
		<form action="<?= h($_SERVER["PHP_SELF"]) ?>" method="GET" autocomplete="off">
			<input type="text" name="pregunta" placeholder="Pregunta lo que quieras" autofocus>
			<button type="submit">Enviar</button>
		</form>
		<div class="hint">Enter para enviar · “Nuevo chat” borra el historial</div>
	</div>

	<script>
		// Auto-scroll al final
		window.scrollTo(0, document.body.scrollHeight);
	</script>
</body>
</html>