# Notes about using Django

## Older docu:

> ## Setting up a Django App:
>
> ## Models, views and registering the app
>
> * Set up models in the `<app>/models.py` file
> * run `python manage.py makemigrations <app>` to create DB scripts
> * next step

## Getting Started

Follow the following points to get the Django Db and Server up and running:

### Django - Create new DB steps (MySQL / MariaDb)

First create the DB in MySQL

```SQL
CREATE DATABASE darts_cam_new DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
GRANT ALL PRIVILEGES ON darts_cam_new.* to 'darts_admin'@'localhost' IDENTIFIED BY 'R04X7qpA1dAoZ0Q';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'darts_admin'@localhost;
```

### From within PyCharm / CLI

Run the `manage.py` script (PyCharm -> `ALT + r`)

* You need to run the migrations (all of them the first time through)
* You need to create a superuser for the dev ENV:
* Start the server

Examples:

```bash
$ python manage.py migrate
... migrations are run
$ python manage.py createsuperuser
... follow tghe prompts ...
$ python manage.py runserver
...
```

## Admin user

| type  | value              |
|-------|--------------------|
| name  | pgetal             |
| email | w.benica@gmail.com |
| pass  | eU99AJETzqIcQcp    |