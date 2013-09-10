#!/bin/bash
cat <<END
Cache-Control: no-cache
Content-Type: text/plain

END
exec 2>&1

port=$(curl -s http://pi.dabase.com/hendry/ | tail -n1 | awk '{print $3}')

options="-n -ex night"

if test "$port" -gt 9999
then
	output=$(dirname $0)/../$(date +%s)-$(echo $options | tr -d ' ').webp
	echo Attempting to save $output

	if ssh -v cam@pi.dabase.com -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p $port "/root/capture.sh $options" > $output
	then
		echo Successful wrote $output
	else
		echo Failed $?
	fi

fi

test -s "$output" || rm "$output"
