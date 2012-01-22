#!/bin/sh

cat <<END
Cache-Control: no-cache
Content-Type: text/html

<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width = 640, height = 480, user-scalable = no">
<title>Webcam viewer</title>
<link rel="stylesheet" href="style.css" />
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script src="main.js"></script>
</head>

<body>

<div id="cam"><h1>No JPG image files found!</h1></div>

<button onclick="next();">&gt;</button>
<button onclick="prev();">&lt;</button>

<ul id="pix">
END
find -L . -iname '*.jpg' -printf "%P\n" | sort -r | while read image
do
	echo "<li><a href=\"$image\">$image</a></li>"
done
cat <<END
</ul>
</body>
</html>
END
