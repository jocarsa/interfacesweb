<?php
declare(strict_types=1);

session_start();

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: Content-Type');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

function json_response(array $data, int $status = 200): void {
    http_response_code($status);
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}

function db(): SQLite3 {
    static $db = null;

    if ($db instanceof SQLite3) {
        return $db;
    }

    $db = new SQLite3(__DIR__ . '/exposiciones.db');
    $db->exec('PRAGMA foreign_keys = ON;');
    return $db;
}

function input_json(): array {
    $raw = file_get_contents('php://input');
    if (!$raw) {
        return [];
    }
    $data = json_decode($raw, true);
    return is_array($data) ? $data : [];
}

function require_login(): int {
    if (!isset($_SESSION['usuario_id'])) {
        json_response([
            'ok' => false,
            'error' => 'Debes iniciar sesión'
        ], 401);
    }
    return (int)$_SESSION['usuario_id'];
}

function usuario_actual(): ?array {
    if (!isset($_SESSION['usuario_id'])) {
        return null;
    }

    return [
        'id' => (int)$_SESSION['usuario_id'],
        'nombre' => (string)($_SESSION['usuario_nombre'] ?? ''),
        'email' => (string)($_SESSION['usuario_email'] ?? '')
    ];
}

$action = $_GET['action'] ?? '';

$db = db();

try {

    if ($action === 'estado') {
        json_response([
            'ok' => true,
            'logueado' => isset($_SESSION['usuario_id']),
            'usuario' => usuario_actual()
        ]);
    }

    if ($action === 'register') {
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            json_response(['ok' => false, 'error' => 'Método no permitido'], 405);
        }

        $data = input_json();

        $nombre = trim((string)($data['nombre'] ?? ''));
        $email = trim((string)($data['email'] ?? ''));
        $password = (string)($data['password'] ?? '');
        $password2 = (string)($data['password2'] ?? '');

        if ($nombre === '' || $email === '' || $password === '' || $password2 === '') {
            json_response(['ok' => false, 'error' => 'Debes completar todos los campos'], 400);
        }

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            json_response(['ok' => false, 'error' => 'Correo no válido'], 400);
        }

        if ($password !== $password2) {
            json_response(['ok' => false, 'error' => 'Las contraseñas no coinciden'], 400);
        }

        if (mb_strlen($password) < 4) {
            json_response(['ok' => false, 'error' => 'La contraseña es demasiado corta'], 400);
        }

        $stmt = $db->prepare('INSERT INTO usuarios (nombre_completo, email, password) VALUES (:nombre, :email, :password)');
        $stmt->bindValue(':nombre', $nombre, SQLITE3_TEXT);
        $stmt->bindValue(':email', $email, SQLITE3_TEXT);
        $stmt->bindValue(':password', password_hash($password, PASSWORD_DEFAULT), SQLITE3_TEXT);

        $res = @$stmt->execute();

        if (!$res) {
            json_response(['ok' => false, 'error' => 'No se pudo registrar. Puede que el correo ya exista'], 409);
        }

        $id = $db->lastInsertRowID();

        $_SESSION['usuario_id'] = $id;
        $_SESSION['usuario_nombre'] = $nombre;
        $_SESSION['usuario_email'] = $email;

        json_response([
            'ok' => true,
            'message' => 'Usuario registrado correctamente',
            'usuario' => usuario_actual()
        ]);
    }

    if ($action === 'login') {
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            json_response(['ok' => false, 'error' => 'Método no permitido'], 405);
        }

        $data = input_json();

        $email = trim((string)($data['email'] ?? ''));
        $password = (string)($data['password'] ?? '');

        if ($email === '' || $password === '') {
            json_response(['ok' => false, 'error' => 'Debes indicar correo y contraseña'], 400);
        }

        $stmt = $db->prepare('SELECT id, nombre_completo, email, password FROM usuarios WHERE email = :email LIMIT 1');
        $stmt->bindValue(':email', $email, SQLITE3_TEXT);
        $result = $stmt->execute();
        $usuario = $result ? $result->fetchArray(SQLITE3_ASSOC) : false;

        if (!$usuario || !password_verify($password, $usuario['password'])) {
            json_response(['ok' => false, 'error' => 'Credenciales incorrectas'], 401);
        }

        $_SESSION['usuario_id'] = (int)$usuario['id'];
        $_SESSION['usuario_nombre'] = (string)$usuario['nombre_completo'];
        $_SESSION['usuario_email'] = (string)$usuario['email'];

        json_response([
            'ok' => true,
            'message' => 'Sesión iniciada correctamente',
            'usuario' => usuario_actual()
        ]);
    }

    if ($action === 'logout') {
        session_unset();
        session_destroy();

        json_response([
            'ok' => true,
            'message' => 'Sesión cerrada'
        ]);
    }

    if ($action === 'reservar') {
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            json_response(['ok' => false, 'error' => 'Método no permitido'], 405);
        }

        $usuarioId = require_login();
        $data = input_json();

        $semana = trim((string)($data['semana'] ?? ''));
        $dia = (int)($data['dia'] ?? 0);
        $hora = trim((string)($data['hora'] ?? ''));

        if ($semana === '' || $dia < 1 || $dia > 7 || $hora === '') {
            json_response(['ok' => false, 'error' => 'Datos incompletos para la reserva'], 400);
        }

        $stmt = $db->prepare('INSERT INTO reservas (usuario_id, semana, dia, hora) VALUES (:usuario_id, :semana, :dia, :hora)');
        $stmt->bindValue(':usuario_id', $usuarioId, SQLITE3_INTEGER);
        $stmt->bindValue(':semana', $semana, SQLITE3_TEXT);
        $stmt->bindValue(':dia', $dia, SQLITE3_INTEGER);
        $stmt->bindValue(':hora', $hora, SQLITE3_TEXT);

        $res = @$stmt->execute();

        if (!$res) {
            $msg = $db->lastErrorMsg();

            if (stripos($msg, 'UNIQUE') !== false) {
                json_response(['ok' => false, 'error' => 'Ya habías reservado ese slot'], 409);
            }

            if (stripos($msg, 'máximo') !== false || stripos($msg, 'maximo') !== false) {
                json_response(['ok' => false, 'error' => $msg], 409);
            }

            json_response(['ok' => false, 'error' => 'No se pudo guardar la reserva', 'detalle' => $msg], 500);
        }

        json_response([
            'ok' => true,
            'message' => 'Reserva guardada correctamente'
        ]);
    }

    if ($action === 'cancelar_reserva') {
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            json_response(['ok' => false, 'error' => 'Método no permitido'], 405);
        }

        $usuarioId = require_login();
        $data = input_json();

        $semana = trim((string)($data['semana'] ?? ''));
        $dia = (int)($data['dia'] ?? 0);
        $hora = trim((string)($data['hora'] ?? ''));

        if ($semana === '' || $dia < 1 || $dia > 7 || $hora === '') {
            json_response(['ok' => false, 'error' => 'Datos incompletos para cancelar la reserva'], 400);
        }

        $stmt = $db->prepare('
            DELETE FROM reservas
            WHERE usuario_id = :usuario_id
              AND semana = :semana
              AND dia = :dia
              AND hora = :hora
        ');
        $stmt->bindValue(':usuario_id', $usuarioId, SQLITE3_INTEGER);
        $stmt->bindValue(':semana', $semana, SQLITE3_TEXT);
        $stmt->bindValue(':dia', $dia, SQLITE3_INTEGER);
        $stmt->bindValue(':hora', $hora, SQLITE3_TEXT);

        $res = $stmt->execute();

        if (!$res) {
            json_response(['ok' => false, 'error' => 'No se pudo cancelar la reserva'], 500);
        }

        if ($db->changes() < 1) {
            json_response(['ok' => false, 'error' => 'No existía esa reserva'], 404);
        }

        json_response([
            'ok' => true,
            'message' => 'Reserva anulada correctamente'
        ]);
    }

    if ($action === 'mis_reservas') {
        $usuarioId = require_login();

        $stmt = $db->prepare('
            SELECT id, semana, dia, hora, fecha_reserva
            FROM reservas
            WHERE usuario_id = :usuario_id
            ORDER BY semana, dia, hora
        ');
        $stmt->bindValue(':usuario_id', $usuarioId, SQLITE3_INTEGER);
        $result = $stmt->execute();

        $rows = [];
        while ($fila = $result->fetchArray(SQLITE3_ASSOC)) {
            $rows[] = $fila;
        }

        json_response([
            'ok' => true,
            'reservas' => $rows
        ]);
    }

    if ($action === 'resumen_slots') {
        $result = $db->query('
            SELECT semana, dia, hora, COUNT(*) AS total
            FROM reservas
            GROUP BY semana, dia, hora
            ORDER BY semana, dia, hora
        ');

        $rows = [];
        while ($fila = $result->fetchArray(SQLITE3_ASSOC)) {
            $rows[] = $fila;
        }

        json_response([
            'ok' => true,
            'slots' => $rows
        ]);
    }

    json_response([
        'ok' => false,
        'error' => 'Acción no válida'
    ], 400);

} catch (Throwable $e) {
    json_response([
        'ok' => false,
        'error' => 'Error interno',
        'detalle' => $e->getMessage()
    ], 500);
}