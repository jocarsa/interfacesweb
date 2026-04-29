Yo soy HTML puro
<br>
<?php
	echo "Y yo soy PHP<br>";

	$output = shell_exec("/usr/bin/python3 002-python.py");
	echo "<pre>$output</pre>";
?>