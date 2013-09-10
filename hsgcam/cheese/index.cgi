#!/bin/sh
cd $(dirname $0)

n=$(date +%s).jpg

wget --user=hsgcam --password='moonWalker97' "http://hsgpi.codersg.com:8080?action=snapshot" -O /tmp/$n

if ! test -s /tmp/$n
then
	rm -f /tmp/$n
	n="lastfetched.jpg"
else
	mv /tmp/$n $n
	cwebp -quiet $n -o $(basename $n .jpg).webp
	rm $(readlink ../../lastfetched.jpg)
	ln -sf $n ../../lastfetched.jpg
	echo $n > ../../lastfetched.txt
fi
