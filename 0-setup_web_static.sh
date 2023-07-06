#!/usr/bin/env bash
# setting up my web servers for the
#+ deployment of web_static

package_name="nginx"

if dpkg -s "$package_name" >/dev/null 2>&1; then
    pass
else
    sudo apt-get install -y nginx
fi

sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

cont="
<html>
  <head>
  </head>
  <body>
    Well my config file works fine!!
  </body>
</html>
"

echo "$cont" |
sudo tee /data/web_static/releases/test/index.html

link="/data/web_static/current"
dst="/data/web_static/releases/test/"

if [ -L "$link" ]; then
    sudo rm "$link"
else
    sudo ln -s "$dst" "$link"
fi

sudo chown -R ubuntu:ubuntu /data/

Config_file="/etc/nginx/sites-available/default"
confg="location /hbnb_static {\n\talias /data/web_static/current/;}"
sudo sed -i "/server_name _;/a\\$confg" "$Config_file"

sudo service nginx restart
