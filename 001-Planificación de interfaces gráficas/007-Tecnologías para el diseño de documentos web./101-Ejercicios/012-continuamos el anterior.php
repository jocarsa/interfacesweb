<!doctype html>
<html>
  <head>
    <title>CRUD</title>
    <!--
      Create = Formulario
      Read = Tabla
      Update = Boton + formulario
      Delete = Boton
    -->
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
        "ciudad" => "Valencia",
        "profesion" => "Médico"
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
    <form action="?" method="POST">
      <?php
        foreach ($cliente as $clave => $valor) {
            echo "<input type='text' placeholder='".$clave."'><br>
      ";
        }
      ?>
      <input type="submit">
    </form>
  </body>
</html>
