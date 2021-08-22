import requests

def test_people_200():
    r=requests.get ('https://swapi.dev/api/people/')
    assert 200 == r.status_code

def test_luke_200():
    r=requests.get ('https://swapi.dev/api/people/1/')
    j=r.json()#j set to json request
    assert 'Luke Skywalker' == j["name"]