echo '{ "data": ['
find . -name old -a -type d -prune -o -iname '*.webp' -type f ! -size 0 -printf "%f %P\n" |
sort -r |
while read time image; do echo -n \"$image\", ; done | sed '$s/,$//'
echo '] }'
