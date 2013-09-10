<?php
header("Content-Type: image/jpeg");
$webp = $_REQUEST["f"];
if (file_exists($webp)) {
	// convert is part of the imagemagick suite
	system("dwebp " . escapeshellarg($webp) . " -o - | convert - jpg:-");
} else {
	die("$webp did not exist");
}
?>
