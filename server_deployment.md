# Steps to deploy this application on server

The steps are reproduced according to the instructions in https://tutos.readthedocs.io/en/latest/source/ndg.html

# 1. mysql

1. Install server
   1. `apt install mariadb-client mariadb-server`
2. Create Database
   1. `create database django;`
3. Create User
   1. `create user 'django'@'localhost';`
   2. `grant all privileges on django.* to 'django'@'localhost' identified by '1q2w3e';`

# 2. Get application

```
/var/www# git clone https://github.com/BorisKGB/django.git
/var/www# cd django/
/var/www/django# git checkout hw6
```

# 3. Prepare venv

Install mysql package system level requirements `# apt install default-libmysqlclient-dev`
Create and init venv
```
/var/www/django# python3 -m venv venv
/var/www/django# source venv/bin/activate
(venv):/var/www/django# pip3 install -r requirements.txt
```

# 4. gunicorn

```
(venv):/var/www/django# pip3 install gunicorn
```

# 5. Configure your app

Create `.env` file according to your options

# 6. Checkout your app

Test launch app by some of the commands:
```
(venv) # gunicorn djangoproject.wsgi:application
(venv) # python3 manage.py runserver 7000^C

```

# 7. Create gunicorn launch scripts

gunicorn_start.sh
```
#!/bin/bash

NAME="djangoproject"                          #Name of the application (*)
DJANGODIR=/var/www/django                     # Django project directory (*)
SOCKFILE=/var/www/django/gunicorn.sock        # we will communicate using this unix socket (*)
USER=www-data                                 # the user to run as (*)
GROUP=www-data                                # the group to run as (*)
NUM_WORKERS=1                                 # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=djangoproject.settings # which settings file should Django use (*)
DJANGO_WSGI_MODULE=djangoproject.wsgi         # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /var/www/django/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /var/www/django/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
```

/etc/systemd/system/gunicorn_djangoproject.service
```
[Unit]
Description=Ourcase gunicorn daemon

[Service]
Type=simple
User=www-data
ExecStart=/var/www/django/gunicorn_start.sh

[Install]
WantedBy=multi-user.target
```

Ser correct directory permissions for data save by `/var/www/django# chown -R www-data:www-data .`

Do not forget to `#systemctl daemon-reload` and `# systemctl enable gunicorn_djangoproject`

# 8. Init project

```
# python3 manage.py migrate
# python3 manage.py createsuperuser
# python3 manage.py collectstatic
```

# 9. Run gunicorn service

`# systemctl start gunicorn_djangoproject`

# 10. Install and configure nginx

Install server
`apt install nginx`

Configure (modify default configuration in this case)
```
upstream django_server {
  server unix:/var/www/django/gunicorn.sock fail_timeout=10s;
}

server {
	listen 80;


	server_name _;
    charset utf8;

    location /static/ {
        autoindex on;
        alias   /var/www/django/static/;
    }

    location /media/ {
        autoindex on;
        alias   /var/www/django/media/;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        if (!-f $request_filename) {
            proxy_pass http://django_server;
            break;
        }
    }
}
```
Optionally test configuration by `# nginx -t`
Restart nginx by `# nginx -s reload`
