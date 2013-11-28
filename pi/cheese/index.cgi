#!/bin/bash
cat <<END
Cache-Control: no-cache
Content-Type: text/plain

END
exec 2>&1

port=$(curl -s http://pi.dabase.com/hendry/ | tail -n1 | awk '{print $3}')

options="-n -hf"

if test "$port" -gt 9999
then
	output="$(dirname $0)/../$(date +%s)-$(echo $options | tr -d ' ').webp"
	echo Attempting to save $output

	if ssh cam@pi.dabase.com -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p $port "~/capture.sh $options" > $output
	then
		if test $(stat -c %s "$output") -lt 60000
		then
			rm "$output"
			echo "Failed, file too small (probably too dark or transfer error)"
		else
			echo pi/$(basename $output) > /srv/www/cam.hackerspace.sg/lastfetched.txt
		fi
	else
		echo Failed $?
	fi

fi
