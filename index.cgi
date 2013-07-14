#!/bin/sh

cat <<END
Cache-Control: no-cache
Content-Type: text/html

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

img{
   max-width:100%;
}

button {
	font-size: 2em;
	border:1px solid #A78B53;
}
.active { background-color: yellow; }
</style>
<script src="/jquery.js"></script>
<script src="main.js"></script>
</head>

<body>

<div id="cam"><h1>No image files found!</h1></div>

<button onclick="prev();">&larr;</button>
<button onclick="next();">&rarr;</button>

<ul id="pix">
END
ls -t *.webp | sort -r |  while read image
do
	if test "$image" = "lastfetched.jpg"
	then
		continue
	fi
	e=$(basename $image .webp)
	desc=$(TZ='Asia/Singapore' date --iso-8601=minutes --date="@$e")
	echo "<li><a href=\"$image\">$desc</a></li>"
done
cat <<END
</ul>
<p><a href="https://github.com/kaihendry/Praze/tree/cam.hackerspace.sg">MIT licensed source</a></p>
</body>
</html>
END
