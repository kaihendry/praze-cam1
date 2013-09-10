# Praze

Demo site: <http://cam.hackerspace.sg>

* Features low <150 [source lines of code](http://en.wikipedia.org/wiki/Source_lines_of_code)
* Simple caching to make next image load quickly
* Assumes images are retrieved in Epoch format
* Supports WebP to JPEG conversion on the fly

# Requirements

CGI support

# Setup

Assuming your **VirtualDocumentRoot** is `/web/%0`.

Git clone into /web/praze.example.com

Link image directory into cloned directory:

	ln -s ~/imagedirectory /web/praze.example.com/

# webp to jpeg

Nginx configuration:

	server {
		server_name cam.hackerspace.sg;
		root /srv/www/cam.hackerspace.sg;
		include cgi.conf;
		location / {
			add_header Access-Control-Allow-Origin "*";
			if ($http_accept !~* "webp") {
				rewrite ^/(.*\.webp)$ /webp2jpg.php?f=$1 last; break;
			}
		}
	}

[webp2jpg.php](webp2jpg.php)
