#!/bin/bash
cat <<END
Cache-Control: no-cache
Content-Type: text/plain

END
exec 2>&1

cd $(dirname $(dirname $(readlink -f $0)))
n=$(date +%s).jpg

wget --user=hsgcam --password='moonWalker97' "http://hsgpi.codersg.com:8080?action=snapshot" -O /tmp/$n

if ! test -s /tmp/$n
then
	rm -f /tmp/$n
	n="lastfetched.jpg"
else
	mv /tmp/$n $n
	cwebp -quiet $n -o $(basename $n .jpg).webp
	cd ..
	rm "$(readlink lastfetched.jpg)"
	ln -sf hsgcam/$n lastfetched.jpg
	echo hsgcam/$n > lastfetched.txt
fi
