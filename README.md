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

set template in `settings.py`
add folder templates
update views.py

using auth from `https://docs.djangoproject.com/en/2.2/topics/auth/default/#module-django.contrib.auth.views`

## add posts page

```sh
django-admin startapp posts
```

update models in post `posts/models.py`

```py
class Post(models.Model):
    text = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='posts', null=False, blank=False)
    user = models.ForeignKey('auth.User', null=False, blank=False, on_delete=models.CASCADE)
    created = models.TimeField(auto_now=True)
```

add posts to project via `settings.py` in install_app
and install Pillow

```sh
pipenv install Pillow
```


css
https://github.com/parnpresso/django-workshop