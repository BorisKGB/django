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

You can use forms in django, for that you need:
* ensure you set SECRET_KEY in project settings for csrf_token generation
* create `$app/forms.py` with your form objects describes form fields
* create correspond views (see example for form request handling in l4app)
  * To get data from form you need on POST request get form object and access data by dictionary `form.cleaned_data`
* connect view to urls
* create template and add form to it.
  * You can just use in template `{{ form }}` it will create basic html code for form fields
    * But you still need to add "send" button and form html block
    * You can use `{{ form.as_p }}` to render form fields in `<p>` tags, by default it will render with `<div>`
      * also there is `.as_p`, `.as_ul`, `.as_div`, `.as_table`
  * You also need to add csrf_token to form html block

---

In forms you can use
https://docs.djangoproject.com/en/5.0/ref/forms/fields/#built-in-field-classes, some of them: 
```
    CharField
    EmailField
    IntegerField
    FloatField
    BooleanField
    DateTimeField
    FileField - upload file
    ImageField - upload exactly image
    ChoiceField - Enum like field
```

All forms automatically have their widget set according to field type
For some types you may want to set widget type manually

https://docs.djangoproject.com/en/5.0/ref/forms/widgets/, some widgets:
```
    TextInput
    TextArea - multyline text
    PasswordInput - hidden text
    NumberInput
    CheckboxInput
    DateTimeInput
    FileInput
    Select
    RadioSelect - Select variant
```

also you can use widgets to set html element attributes like
`message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))`
will set this field html tag class to 'form-control'
or set 'placeholder' for empty field message like `widget=forms.TextInput(attrs={'placeholder': 'help str here'})`

---

You can add custom validators for you form fields

For that in form class add methods named by f'clean_{field_name}' and raise forms.ValidationError on unexpected data
https://docs.djangoproject.com/en/5.0/ref/forms/validation/#cleaning-a-specific-field-attribute

---

If you want to upload files in you project you need to:
* set project level settings
  * MEDIA_URL defines url addr for access uploaded files
    * Need to be connected to app.urls to be able to use it
  * MEDIA_ROOT defines path in project to store files, will be created by django when needed
* in template set `enctype="multipart/form-data"` for form tag 
* get file in form view from `cleaned_data`
  * On create form object also need to access `request.FILES`
* save file using `django.core.files.storage.FileSystemStorage.save(name, file_obj_from_cleaned_data)`

---

By default django has enabled admin web interface
It`s language corresponds to project LANGUAGE_CODE setting

For being able to use admin interface need to create superuser
`python manage.py createsuperuser [--username username] [--email email] [and other optional parameters]`
command will interactively ask for username, email and password

you can also change password using
`python manage.py changepassword <username>`

Be shure to apply service level application migrations (admin, auth, ...) or just make them for all apps

By default you can perform CRUD operations over internal users and groups

---

To be able to perform CRUD operations over custom models you need:
* create model (makegigration/migrate)
* if you not admin - add permissions to edit model
* add model to admin panel in $app:admin.py using `admin.site.register(Model)` for each model
  * see l3app.admin as example

You can modify how admin interface represent Model for this you need to
* create a class inherited from `admin.ModelAdmin`
* Use this class to describe modifications for admin interface
* Connect this class to model registration in $app:admin.py for example `admin.site.register(MyModel, MyModelAdminConfig)`

Using `ModelAdmin` you can perform
* for model object table
  * change list of default fields to represent model object in a table
    * by default it will use __str__ method of model
    * you can set `list_display = ['model_field_name_1', 'model_field_name_N']` to show only this fields 
      * after set this option interface will allow you to use order by this fields
  * add default field ordering
    * using `ordering = ['field_name_to_order_1', 'field_name_to_order_N']` (multy level ordering allowed)
    * by adding '-' before field_name you reverse ordering
  * add filtering to fields
    * using `list_filter = ['field_to_filter_1', 'field_to_filter_N']`
    * available filters will depend on field type
  * allow search operations on fields
    * using `search_fields = ['field_to_search_1', 'field_to_search_N']`. If set multiple fields it will be OR(field) search
    * and `search_help_text = 'Use to search by ....`. Only one help string
  * add custom actions
    * create action method with decorator `@admin.adtion()`
      * decorator parameter `description='Action description'`
      * preferred method parameters
        * modeladmin
        * request
        * queryset - objects to which action will be applied
        * https://docs.djangoproject.com/en/5.0/ref/contrib/admin/actions/#writing-action-functions
    * connect method to `ModelAdmin` using `actions = [action_method_1, action_method_N]`
* for model object itself (change block)
  * set field list to show
    * using `fields = ['model_field_name_1', 'model_field_name_N']`
    * as example may be needed to show fields with default values
  * mark fields to read only
    * using `readonly_fields = ['model_field_name_1', 'model_field_name_N']`
  * more detailed fields config using fieldsets
    * conflicts with `fields` parameter
    * allow to control fields layouts, groups, ...
    * https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
* https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#modeladmin-objects

---

django debug toolbar https://django-debug-toolbar.readthedocs.io/en/latest/

1. install package `django-debug-toolbar`
2. configure project settings
   1. add `INTERNAL_IPS` list
   2. add 'debug_toolbar' to `INSTALLED_APPS`
   3. add 'debug_toolbar.middleware.DebugToolbarMiddleware' to `MIDDLEWARE`
3. add it to urlpatterns `path('__debug__', include("debug_toolbar.urls"))`

---

publish project

1. modify project settings
   1. disable DEBUG
   2. add boolean true parameters `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`
   3. make `SECRET_KEY` more secret, for example by `os.getenv('SECRET_KEY')`
      1. after that test server can be launched by `$ SECRET_KEY="dasdasd" python3 manage.py ...` 
   4. ensure all media and static root variables point inside project directory using `BASE_DIR / 'static/'`
2. reconfigure your database to something project related
   1. optionally set COLLATE to utf-8
   2. for DB options like password you also are able to use `os.getenv()`
3. optionally disable all not required urlpatterns
4. create requirements.txt
   1. optionally manual add to requirements `python-dotenv` and your sql client python library
5. create wsgi file for your django app
6. 