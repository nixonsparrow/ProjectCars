# Project Cars

A simple REST API for car rating.

To build in Docker container run:
~~~~
$ docker-compose up
~~~~
Create a venv directory inside your app:
~~~~
$ virtualenv -p /usr/bin/python3 venv/
$ source venv/bin/activate
~~~~
To install all needed modules for your app run:
~~~~
$ pip install -r requirements.txt
~~~~
All tests are in directory:
~~~~
tests/
~~~~
Interesting endpoints:
======================
~~~~
/cars/      # GET, POST
/cars/{id}  # DELETE
/rate/      # POST
/popular/   # GET
~~~~
To add a car to database send POST request \
(values are checked here: https://vpic.nhtsa.dot.gov/api/):
~~~~
POST ENDPOINT: /cars/
CONTENT:
{
    "make": "VALID_CAR_MAKE",
    "model": "VALID_CAR_MODEL"
}
~~~~
To rate a car send POST request:
~~~~
POST ENDPOINT: /rate/
CONTENT:
{
    "car_id": CarObject.id
    "rate": (int value from 1 to 5)
}
~~~~
To delete a car just send DELETE here:
~~~~
DELETE ENDPOINT: /cars/{id}
~~~~
All cars by id with average ratings:
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
All cars by id with ratings count (number of votes):
~~~~
GET ENDPOINT: /popular/
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