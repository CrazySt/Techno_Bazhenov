
server {
	listen 80;
	root /home/serjio/Techno_Bazhenov/public;
	index index.html index.htm index.nginx-debian.html;
	server_name bazh_chat.ru www.bazh_chat.ru;
	
	
	location /api/ {
		proxy_pass http://127.0.0.1:8000; 
	}
	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}

	


}


# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#	listen 80;
#	listen [::]:80;
#
#	server_name example.com;
#
#	root /var/www/example.com;
#	index index.html;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}
