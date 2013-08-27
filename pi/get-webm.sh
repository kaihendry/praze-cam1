port=$(curl -s http://pi.dabase.com/hendry/ | tail -n1 | awk '{print $3}')

options="-n -ex night"
if test "$port" -gt 9999
then
	ssh root@pi.dabase.com -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p $port "/root/capture.sh $options" > /srv/www/cam.hackerspace.sg/pi/$(date +%s)-$(echo $options | tr -d ' ').webp
fi
