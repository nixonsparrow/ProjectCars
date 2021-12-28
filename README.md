# Project Cars

A simple REST API for car rating.

## Running from Docker

The easiest way to start is to build in a Docker container:

~~~~
$ docker-compose up
~~~~

## Running locally

To build the app locally, create a venv directory inside your app:

~~~~
$ virtualenv -p /usr/bin/python3 venv/
$ source venv/bin/activate
~~~~

To install all needed Python modules for your app, run:

~~~~
$ pip install -r requirements.txt
~~~~

To start the application, run:

~~~~
$ python manage.py runserver
~~~~

## Tests

All tests are located in the ``tests/`` directory.

To run tests, call:

~~~~
$ python manage.py test
~~~~

## Config.json

It is recommended to create your own config file in app's main folder. 
It has to have all 3 variables. 
Information about SECRET_KEY are to found here: https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key 

Here's config.json file scheme: 

~~~~
{
  "SECRET_KEY": "D4qGKi#ptAq@o`5QW9iv4$eNLc6xl4Rwi*Ffes6oOc_YhkYnc",
  "ALLOWED_HOSTS": ["YOUR SITE", "localhost"],
  "DEBUG": true/false
}
~~~~


Interesting endpoints:
======================

~~~~
/cars/      # GET, POST
/cars/{id}  # DELETE
/rate/      # POST
/popular/   # GET
~~~~

To add a car to the database, send a POST request \
(values are checked here: https://vpic.nhtsa.dot.gov/api/):

~~~~
POST ENDPOINT: /cars/
CONTENT:
{
    "make": "VALID_CAR_MAKE",
    "model": "VALID_CAR_MODEL"
}
~~~~

To rate a car, send a POST request:

~~~~
POST ENDPOINT: /rate/
CONTENT:
{
    "car_id": CarObject.id
    "rating": (int value from 1 to 5)
}
~~~~

To delete a car, just send DELETE here:

~~~~
DELETE ENDPOINT: /cars/{id}
~~~~

To list cars by id with their average ratings:

~~~~
GET ENDPOINT: /cars/
EXAMPLE CONTENT:
[
    {
        "id": 1,
        "make": "Volkswagen",
        "model": "Passat",
        "avg_rating": 4.7
    },
    {
        "id": 2,
        "make": "Dodge",
        "model": "Viper",
        "avg_rating": 5.0
    }
]
~~~~

To list all cars by id with their ratings count (number of votes):

~~~~
GET ENDPOINT: /popular/
EXAMPLE CONTENT:
[
    {
        "id": 1,
        "make": "Volkswagen",
        "model": "Passat",
        "rates_number": 80
    },
    {
        "id": 2,
        "make": "Dodge",
        "model": "Viper",
        "rates_number": 15
    }
]
~~~~
