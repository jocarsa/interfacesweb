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
        "ciudad" => "Valencia",
        "provincia" => "Valencia",
        "codigo_postal" => "46001",
        "pais" => "España",
        "empresa_nombre" => "López Consultores S.L.",
        "empresa_cif" => "B12345678",
        "empresa_direccion" => "Av. del Puerto, 123",
        "empresa_actividad" => "Consultoría empresarial",
        "fecha_alta" => "2024-09-15",
        "activo" => true
      ];
      
      echo $cliente['id'];
      echo $cliente['nombre'];
      
    ?> 
  </body>
</html>
