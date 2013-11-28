all: index.html index.json

index.html: pi/
	./index.cgi > index.html
index.json: pi/
	./create-json.sh > index.json
