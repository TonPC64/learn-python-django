# Learn Django

## Install

```sh
# prepare start project
pip3 install pipenv
pipenv shell --python=python3
pipenv install Django

# check Django
django-admin # pipenv shell first if can't run django

# start project
django-admin startproject istagram
cd istagram # ls and find manage.py

 # start server
python manage.py runserver
python manage.py migrate # add admin page by default
python manage.py createsuperuser # create account
python manage.py startapp home # add page home
```

update `views.py` in /home

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("My homepage <3")
```