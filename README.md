[![Build Status](https://travis-ci.org/devinstevenson/intoflask.svg?branch=master)](https://travis-ci.org/devinstevenson/intoflask)


##To setup on server

##Upstart
```copy introflask.conf file to /etc/init/
change env vars in introflask.conf```

##Nginx
```copy nginx.conf to /etc/nginx/
copy blockips.conf to /etc/nginx/
copy introflask.conf to /etc/nginx/sites-available
run $ ln -s /etc/nginx/sites-available/introflask /etc/nginx/sites-enabled/```

##SSL
download certbot
run 
```$ certbot-auto certonly -d www.example.com -d example.com
copy privkey.pem and fullchain.pem from /etc/letsencrypt/live/example.com/ to desired path that matches nginx config
change permissions of files as needed to match user running Upstart introflask.conf```
