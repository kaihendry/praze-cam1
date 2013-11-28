#!/bin/sh

if test "$REQUEST_METHOD"
then
	echo -e "Cache-Control: no-cache\nContent-Type: text/html\n\n"
fi

cat <<END
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Webcam viewer</title>
<style>
body {
	font-family: "Helvetica Neue", sans-serif;
}
img {
	width: 100%;
	height: auto;
}
button {
	font-size: 2em;
	border:1px solid #A78B53;
}
.active { background-color: yellow; }
</style>
<script src="/jquery.js"></script>
<script src="/main.js"></script>
</head>

<body>

<div id="cam"><h1>No image files found!</h1></div>
<h3 id="date"></h3>
<button onclick="prev();">&larr;</button>
<button onclick="next();">&rarr;</button>

<ul id="pix">
END

find . -name old -a -type d -prune -o -iname '*.webp' -type f ! -size 0 -printf "%f %P\n" |
sort -r |
while read time image; do echo "<li><a href=\"$image\">$image</a></li>"; done
cat <<END
</ul>
<p><a href="https://github.com/kaihendry/Praze/tree/cam.hackerspace.sg">MIT licensed source</a></p>
</body>
</html>
END
