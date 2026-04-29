<?php
  // Defino el nombre en el que voy a guardar el archivo
  $filename = 'basededatos/'.date('Y').'-'.date('m').'-'.date('d').'-'.date('H').'-'.date('i').'-'.date('s').'.json';
  // Codifica un array PHP a un objeto JSON
  $jsonData = json_encode($_POST, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
  // Este comando realmente guarda el archivo en el disco duro
  file_put_contents($filename, $jsonData);

?>
