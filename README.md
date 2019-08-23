# Django API Boilerplate

Boilerplate for Django backend with REST API. Uses [Django REST Framework](http://www.django-rest-framework.org/) and [Django REST Knox](http://james1345.github.io/django-rest-knox/) to power the API and authentication.

Comes with:

 - Requirements file listing all dependencies.
 - Django REST Framework and Django REST Knox pre-configured.
 - A config app to store and retrieve key/value parameters.
 - Extra endpoint `POST /token/` to validate a token.
 - An example endpoint just to ilustrate.

To use just fork and do

```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

To test use a Web browser to navigate to [http://localhost:8000/app_boilerplate/endpoint_boilerplate/](http://localhost:8000/app_boilerplate/endpoint_boilerplate/). You should the Django REST Framework browsable API page displaying the following JSON response:
```
{
    "example": true
}
```

To create a super user do:

```
$ python manage.py createsuperuser
```

Than you can navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) to access Django admin site.

You want to replace "myproject" with your project name and "myapp" with an app name.# EasyExam
