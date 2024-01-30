init project
`$ django-admin startproject djangoproject`
project can be root of git repo tree

---

start project
`$ python3 manage.py runserver 0.0.0.0:8000`
ip:port is optional parameters

Or use django.core.management.call_command, see example in main.py

---

project/$projectname/settings.py:ALLOWED_HOSTS describes hosts ON which server allowed to execute http requests

otherwise you get error like
`django.core.exceptions.DisallowedHost: Invalid HTTP_HOST header: '192.168.148.252:8000'. You may need to add '192.168.148.252' to ALLOWED_HOSTS.
`

---

create app in custom directory
1. create directory
   * `$ mkdir -p apps/lections/l1/l1app`
2. create app
   * `$ python3 manage.py startapp l1app apps/lections/l1/l1app`

---

after create app add it to project by simply adding app name to
project/$projectname/settings.py:INSTALLED_APPS list

if you app not in main project dir or you are getting Import errors on project start, then you need to:
1. go to $appPath/apps.py
   * set `name` to python import like path to your app
   * as for l1app it will be `apps.lections.l1.l1app`
2. in settings.py:INSTALLED_APPS use same app name as in $appPath/apps.py

---

first steps

1. Create view methods in $appPath/views.py
2. Map urls inside app for them in $appPath/urls.py
3. Include app urls to main project urls in project/$projectname/urls.py

Final URL consists of the project and application paths
so
```
(project)path('lections/l1', include('apps.lections.l1.l1app.urls'))
(app)path('', views.index, name='index')
```
will lead to http://localhost:8000/lections/l1 as an index page
and
so
```
(project)path('lections/l1/', include('apps.lections.l1.l1app.urls'))
(app)path('', views.index, name='index')
```
will lead to http://localhost:8000/lections/l1/ as an index page. Be aware of '/' at the end

---

for logging configuration you can set project/$projectname/settings.py:LOGGING to needed logging.config.dictConfig structure
see created example in file