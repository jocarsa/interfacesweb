<?php
	function JVformulario($campos){
  	$salida = '<form>';
    foreach($campos as $campo){
    	$salida .= '<input type="text" placeholder="'.$campo.'">';
    }
    $salida .= '<input type="reset">';
    $salida .= '<input type="submit">';
    $salida .= '</form>';
    return $salida;
  }
  
  echo JVformulario(['nombre','apellidos','email']);
  echo "<br>";
  echo JVformulario(['producto','precio','descripcion']);
?>