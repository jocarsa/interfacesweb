<!doctype html>
<html>
  <head>
  </head>
  <body>
    <table>
    <tr>
    <?php
      for($dia = 1;$dia<31;$dia++){
        echo "<th>".$dia."</th>";
      }
    ?>
    </tr>
    <?php
      for($fila = 1;$fila<20;$fila++){
    ?>
      <tr>
        <?php
        for($dia = 1;$dia<31;$dia++){
          echo "<td>".rand(1,10000)."</td>";
        }
      ?>
    </tr>
    <?php } ?>
    </table>
  </body>
</html>
