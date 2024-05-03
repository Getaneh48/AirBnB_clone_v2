#!/usr/bin/env bash
# a Bash script that sets up a web server for the deployment of web_static

if ! [ -x "$(command -v nginx)" ]; then
sudo apt-get update
sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
sudo echo "<html>
  <head>
  </head>
  <body>
	Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo chown -R ubuntu:ubuntu /data
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '54i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
