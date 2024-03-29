TJ Rapid
========

This is the source code of the web site http://www.tjrapid.sk.
It is based on the web development framework Django. Some of the applications
present in the project are generally reusable, notably **attachment**
for attaching files to arbitrary django objects and **eventapp**
for running an event registration system.

Prerequisites
-------------

Make sure you have these programs and packages installed:

* Python 3
* git

Installation
------------

1. Create a new python virtual environment, and activate it:

        python3 -m venv tjr
        cd tjr
        . bin/activate

2. Install required python packages:

        pip3 install -r requirements.txt

3. Clone the tjrapid repository:

        git clone git://github.com/peterkuma/tjrapid.git
        cd trapid

4. Customize the project settings:

        cp tjrapid/settings_local-example.py tjrapid/settings_local.py
        vim tjrapid/settings_local.py

5. If you have a dump of the database, restore it as db/tjrapid.sqlite.
   Synchronize the database with Django models:

        ./manage.py makemigrations
		./manage.py migrate
		# or
		./manage.py migrate --fake-initial

6. Collect static files into the static directory:

        ./manage.py collectstatic --noinput

7. Run the development server:

        ./manage.py runserver

Deployment
----------

For deployment, follow the instructions above, but take these additional steps:

1. Set DEBUG = False in settings\_local.py and configure
   EMAIL\_* and SECRET_KEY appropriately.

2. Set up a postgresql database by restoring a database dump.
   Configure DATABASES in settings_local.py.

3. Set up apache and mod_wsgi or nginx and gunicorn to serve the web site.
