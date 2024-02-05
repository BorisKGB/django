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

---

for use django models need to make migrations
you can create migration logic for your models by
`python3 manage.py makemigrations [app]`

If app is not set it will apply for all apps. Use app name, not import like path.

You will need to rerun this command when you change your models

example `python3 manage.py makemigrations l2app`

---

after create 'migrations' you need to apply them to DataBase by doing
`python3 manage.py migrate [app]`
https://djangodoc.ru/3.2/ref/django-admin/#django-admin-migrate

If app not set it will apply for all apps. Use app name, not import like path.

example `python3 manage.py migrate l2app`

---

You can use separate database per app
For that you need to:
1) define new database
2) create dbRouter (see example in apps.lections.l2.l2app.dbRouter)
3) add dbRouter to $project.settings.py:DATABASE_ROUTERS
4) perform migration for app and set datatabase name `python3 manage.py migrate l2app --database=app_l2`

If you not set `--database` parameter Table structure will be applied to 'default' database

---

You can create custom commands for admin actions using `manage.py ...`  
Command name must be unique or will be overwritten https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#overriding-commands

For that inside your app create package `management` and inside that another package `commands` where you can store new commands
See `apps.lections.l2.l2app` for example

To run just do `python3 manage.py $your_command [argumants if any]`
add `-h` to get help

---

operations with SQL can be done through Model Objects

create:
```
  user = User(**user_data)  # create object
  user.save()  # dump object to sql
```

get:
```
  User.objects.all()  # get all data from table
  User.objects.get(key=val)  # get data where $key = $val. Will raise an error if nothing was founded
  User.objects.filter(key=val).first()
    # search first value for data where $key = $val. return None if nothing was founded
    # you can use `pk` (for primary key) to search by id
    # not exact filtering can be used by asking for `key__$modifier`
    #  for example filter(name__startswith="he")
    # some modifiers: exact, iexact, contains, in, gt, gte, lt, lte, startswith, endswith, range, date, year
    # all queries work as generators and will be executed only when something tryes to get data from them
    # you also can use all/filter with list slicing to implement OFFSET and LIMIT
    #  for example all()[5:10] -> OFFSET 5 LIMIT 5 (5 objects from 5 to 10)
    #  all()[:5] -> LIMIT 5 (get first 5 objects)
    #  negative indexing not available [-1] cann not be done
    #  all()[:10:2] -> will get every second object from first 10. This query will be executed at place because 'every second' will need to get the data
  You can get onjects from ManyToMany relation fields like in normal get request
    order = OrderModel.objects.filter(pk=order_id).first()
    order.products.all() # and other get options
``` 
  more https://metanit.com/python/django/5.13.php https://djangodoc.ru/3.2/topics/db/queries/ 

update:
```
  user = User.objects.filter(pk=1).first()  # get existing record
  user.name = "new name"  # change it
  user.save()
```

delete:
```
  user = User.objects.filter(pk=1).first()  # get existing record
  if user is not None:  # check record existence
    user.delete()  # delete it
```

---

It is possible to create hooks on some actions.
read https://docs.djangoproject.com/en/5.0/topics/signals/

As Example in apps.hw.shopapp i use m2m_changed signal to update field after related objects change
You need to create signal method and register it in app.ready method

---

views represent logic that process http requests

Put them in app.views.py  
You can use methods or classes for describe that logic, see example in l3app.views

---

Views itself does nothing, you need to connect your views to urls using url manager
1) create $app.urls.py and set urlpatterns list according to your views
2) Connect $app.urls to global urls in $project/urls.py

---

You can use urls to encode variables like
```
path('<int:year>/<int:month>/<slug:slug>/', do_some, name='my_view')

some of available types in urls:
  str (default)
  int
  slug - [a-z0-9-_] (maybe it also allow for RU letters)
  uuid
  path
```

---

html templates stored in $app/templates/$app_name/$template_name.html
reason of that path is: django imports templates from all apps to one big list,
  so if you have more than one app you have to use unique names for templates 
  or use $app directories as delimiter

To use them from view do
```
context = {'a': 'b'}
return render(request, "$app_name/$template_name.html", context)
```

You can use jinja2 syntax in templates
More on that https://docs.djangoproject.com/en/5.0/ref/templates/language/#variables
https://metanit.com/python/django/2.4.php

templates operations examples:
```
for
  {% for item in my_list %}
  <li>{{ item }}</li>
  {% endfor %}
  {% for key, val in my_dict.items %}
  <li> {{ key }} - {{ val }}</li>
  {% endfor %}
inheritance (in view need to use (latest)child.html)
  base.html
    {% block content %}
      content for no such block in child
    {% endblock %}
  child.html
    {% extends 'base.html' %}
    {% block content %}
      <h1>text</h1>
    {% endblock %}
links can be generated by `{% url 'urlpattern_name_app_independent' [parameters] %}`
  for example `{% url 'index' parameter1 parameter2 parameterN %}`
```

---

You can set additional global path for templates by changing list $project/$projectname/settings.py:TEMPLATES['DIRS']
For example adding record `BASE_DIR / 'templates'` will allow you to drop all your templates in global path

---

