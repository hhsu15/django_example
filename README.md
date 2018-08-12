[![Build Status](https://travis-ci.org/hhsu15/django_example.png?branch=master)](https://travis-ci.org/hhsu15/django_example)

# django_example
Example how to use django step by step 

## To get started
Create a project called mysite
```bash
$django-admin startproject mysite
```
Create an app called hello
```bash
$python manage.py startapp hello
```

## Manage the app
Refer to the actual files in the repo to see actual codes
* Under the hello app, `views.py` is where you create the functions (views) and define what needs to happen when user calls it by going into the route. For example, render html template.

* Next, create a new file called `urls.py` under the hello app. In this file, we use "urlpatterns" to associate the urls supported by this particular app (in this case hello). This is essentially creating the routes that call the functions in the `views.py`

* Then, go to the `urls.py` under the `mysite` folder. Here we need to tell the project (mysite) about the `urls.py` we created by adding a path using "include" function to route to hello.urls. 

## To start the webserver
Simply run this:
`$python manage.py runserver`

## Create Databases
Use classes to build ORM
* Under the app, `models.py` is where the database classes are defined
* Once the models are defined, go to the `settings.py` under the project (hello), locate INSTALLED_APPS and add something like hello.apps.HelloConfig - this is to tell the project thtat this app is installed for the project.
* Next, since the model is created, run the following to automatically migrate all the changes on the models
```bash
$python manage.py makemigrations
```
* You can run the following if you are interested in the acutal sql query that was run
```bash
$python manage.py sqlmigrate {name of the app} {migration code like 001}
```
* Then to actually migrate, run:
```bash
$python manage.py migrate
```
* You can also use Ipython shell to experiment your database with ease
```bash
$python manage.py shell
```

## Access Admin UI to manage models
Django provides UI to manage the models you created. 
* First, go to the `admin.py` to register your models. Refer to the example
* Then, run below to make yourself superuser
```bash
$python manage.py createsuperuser
```
* Then you go to '/admin' you will be able to use the UI and manage your models


## Create User Login
Django helps handle the user login. Refer to the code in `view.py`.
* To manage user account, you can use '/admin' UI or through the code as the following example:
```python
from django.contrib.auth.models import User

# create user account
user = User.objects.create_user('user_name', 'email_address', 'password')

# set user attribute, like first name
user.first_name = 'Firstname'
user.save()
```
