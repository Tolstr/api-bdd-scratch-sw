import requests
from pytest_bdd import scenarios, given, then, parsers, when
scenarios('')

@when ('I am making request I am getting right name, birth_year, url, status_code')
def validate_people(name, birth_year, url, status_code):
    r=requests.get(f"https://swapi.dev/api/{url}")
    j=r.json()
    assert int(status_code) == r.status_code,\
        f'actual status code is {r.status_code} and expected is {status_code}'
    assert name == j["name"],\
        f'actual name is {j["name"]} and expected is {name}'
    assert birth_year == j["birth_year"],\
        f'actual birth_year is {j["birth_year"]} and expected is {birth_year}'
