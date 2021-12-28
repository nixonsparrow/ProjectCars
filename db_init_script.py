import json

fixtures = []
golf = {'make': 'Volkswagen', 'model': 'Golf'}
passat = {'make': 'Volkswagen', 'model': 'Passat'}


def append_car(pk, make, model):
    fixtures.append({
        "model": "cars.car",
        "pk": pk,
        "fields": {
            "make": make,
            "model": model
        }
    })


def append_rate(pk, car_id, rate):
    fixtures.append({
        "model": "cars.rate",
        "pk": pk,
        "fields": {
            "car_id": car_id,
            "rate": rate
        }
    })


def create_fixtures():
    append_car(1, golf['make'], golf['model'])
    append_car(2, passat['make'], passat['model'])

    [append_rate(pk, 1, 5) for pk in range(1, 101)]
    [append_rate(pk, 2, 5) for pk in range(101, 122)]
    [append_rate(pk, 2, 4) for pk in range(122, 132)]

    with open('db_init.json', 'w') as write_file:
        json.dump(fixtures, write_file)


if __name__ == '__main__':
    create_fixtures()
