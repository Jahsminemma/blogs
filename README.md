# Blog app
 Link to the project deployed app on heroku
 [https://zuriblog-app.herokuapp.com](https://zuriblog-app.herokuapp.com)


#### Dependencies

* django-heroku
* psycopg2-binary
* whitenoise

### Virtualenv Used
  * pipenv
  
See `Requirements.txt` for specific required versions of these packages.

#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8
--------------- | --- | --- | ---
2.2  |  *  |  *  |  *
3.0  |  *  |  *  |  *


## Documentation
To start the project:
```shell
      cd Desktop
```
```shell
      mkdir Blog
```

### Installation

To start the virtual environment run:

```shell
    $ pipenv shell
```
or Download pipenv on your machine

Install Django 
```shell
      pipenv install Django
```
### ```Create Django Project with "django-admin startproject project_name```
### ```Create Django App with "python manage.py startapp app_name```

To run the Development server on your localserver
```shell
      python manage.py runserver
 ```
 The server will open on ```lacalhost:8000```
 
 ### Deployment
 The app is deployed on heroku
 
 
