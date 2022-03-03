# TEAM_003

This branch contains code that was produced by following this tutorial: https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react

## Run the backend server

    $ cd backend
    $ python manage.py runserver

## Run the frontend server

    $ cd frontend
    $ npm start

## Activate the interactive python shell
View some use case examples here: https://docs.djangoproject.com/en/4.0/intro/tutorial02/#playing-with-the-api

    $ python manage.py shell

## Run automated tests
This will run all of the automated tests for a given app (i.e. polls).

    $ python manage.py test <app_name>

## Migrations

### Run migrations
This must be done at an apps inception and every time a migration is created. 

    $ python manage.py migrate


### Create a migration
This must be done everytime a change to our model is made. Django generates the migration automatically. You must run the migratons afterwards to apply the changes to your database. 

    $ python manage.py makemigrations polls


### Display SQL of a migration
This allows you to see the SQL that would be ran if you ran the given migration.

    $ python manage.py sqlmigrate polls <migration_number>


### Run problem checking software
This can be used to help identify any issues with migrations. 

    $ python manage.py check


## Using pipenv to manage your virtual environment (instructions written for mac)

### Install pipenv locally
In your source code root directory:

    $ pip install pipenv

### Activating the virtual environment
In your source code root directory:

    $ pipenv shell

### Deactivating the virtual environment
Do this when you woul dlike to leave the virtual environment:

    $ deactivate

### Updating the virtual environment
This will download any new dependancies added in version controll. 

    $ pipenv install

### Install a new package
Use this to install new packages. This will update the Pipenv file for version control. 

    $ pipenv install <package_name>

## Create an admin account
The online docs cover this: https://docs.djangoproject.com/en/4.0/intro/tutorial02/#creating-an-admin-user

    $ python manage.py createsuperuser

## View testing
To test a veiw as a user, we can use Selenium (much like Cucumber).
Selenium is cool because it actually opens a webbrowser to run the tests.
View it here: https://ordinarycoders.com/blog/article/testing-django-selenium

## Packaging and publishing our app
If we find it nessisary, this is how:

    https://docs.djangoproject.com/en/4.0/intro/reusable-apps/
