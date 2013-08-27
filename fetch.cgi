#!/bin/sh
cd $(dirname $0)

n=$(date +%s).jpg
wget --quiet --user=hsgcam --password='moonWalker97' "http://hsgpi.codersg.com:8080?action=snapshot" -O /tmp/$n

if ! file /tmp/$n | grep -q JPEG
then
	rm /tmp/$n
	exit
fi

if ! test -s /tmp/$n # || perceptualdiff -threshold 200000 /tmp/$n lastfetched.jpg > /dev/null
then
	rm -f /tmp/$n
	n="lastfetched.jpg"
else
	mv /tmp/$n $n
	cwebp -quiet $n -o $(basename $n .jpg).webp
	rm $(readlink lastfetched.jpg)
	ln -sf $n lastfetched.jpg
	echo $n > lastfetched.txt
fi

cat <<END
Location: $n


END
