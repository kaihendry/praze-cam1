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
<link rel="stylesheet" href="style.css" />
<script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<script src="main.js"></script>
</head>

<body>

<!--
<button id=signin><img src="email_sign_in_black.png"></button>
<button id=signout>Signout</button>
-->

<div id="cam"><h1>No JPG image files found!</h1></div>

<button onclick="prev();">&larr;</button>
<button onclick="next();">&rarr;</button>

<ul id="pix">
END
ls -t *.jpg | sort -r |  while read image
do
	if test "$image" = "lastfetched.jpg"
	then
		continue
	fi
	e=$(basename $image .jpg)
	desc=$(TZ='Asia/Singapore' date --iso-8601=minutes --date="@$e")
	echo "<li><a href=\"$image\">$desc</a></li>"
done
cat <<END
</ul>
<p><a href="https://github.com/kaihendry/Praze/tree/cam.hackerspace.sg">MIT licensed source</a></p>
</body>
</html>
END
