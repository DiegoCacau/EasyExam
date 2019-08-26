# EasyExam


# Preparing enviroment

* Create and activate a virtualenv

	```
	$ virtualenv -p python3 env
	$ source env/bin/activate
	```

* Clone this repository
* Create a database and user in MySQL 
* Crete a `.env` file under `es_project` following `.env.example`;
* Create a symbolic link to `settings.dev.py` named `settings.py` under `es_project`;
      * On Windows open cmd as administrator and do `$ MKLINK settings.py settings.dev.py`;
      * On Linux do `$ ln -s settings.dev.py settings.py`;

* Install requirements and migrate:

	```
	$ pip install -r requirements.txt
	$ python manage.py migrate
	```

* Install fixtures:
	```
	$ python initial_data.py
	```


# Working with

* To start server:
	```
	$ python manage.py runserver
	```


* To create a super user do:

	```
	$ python manage.py createsuperuser
	```


* To run tests:

	```
	$ python manage.py  test --verbosity=2 -k
	```