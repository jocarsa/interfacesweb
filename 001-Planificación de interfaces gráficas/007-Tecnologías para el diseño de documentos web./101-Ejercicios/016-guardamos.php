<?php
  $f='basededatos/basededatos.json';
  $d=file_exists($f)?json_decode(file_get_contents($f),true):[];
  $d[]=$_POST;
  file_put_contents($f,json_encode($d,JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE));
?>
