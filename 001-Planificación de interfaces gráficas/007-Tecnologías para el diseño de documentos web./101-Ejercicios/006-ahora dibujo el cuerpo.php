<!doctype html>
<html>
  <head>
  </head>
  <body>
    <?php
      $cliente = [
        "id" => 101,
        "nombre" => "María López García",
        "dni" => "12345678Z",
        "email" => "maria.lopez@example.com",
        "telefono" => "+34 600 123 456",
        "calle" => "Calle Mayor, 45",
        "ciudad" => "Valencia"
      ];
      
      $claves = array_keys($cliente);
      //var_dump($claves);
      
    ?> 
    <table>
      <thead>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<th>".$clave."</th>
          ";
            }
          ?>
        </tr>
      </thead>
      <tbody>
        <tr>
          <?php
            foreach ($cliente as $clave => $valor) {
                echo "<td>".$valor."</td>
          ";
            }
          ?>
        </tr>
      </tbody>
    </table>
  </body>
</html>
