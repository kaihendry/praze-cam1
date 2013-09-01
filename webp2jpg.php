<?php
header("Content-Type: image/jpeg");
$webp = $_REQUEST["f"];
if (file_exists($webp)) {
	system("dwebp " . escapeshellarg($webp) . " -o - | convert - jpg:-");
} else {
	echo "$webp did not exist";
}
?>
