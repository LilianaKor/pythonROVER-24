import pytest
import requests

base_url = "https://restful-booker.herokuapp.com/booking"
auth_url = "https://restful-booker.herokuapp.com/auth"
# def sum_it(x, y):
#         return x + y
#
# def test_equal():
#     assert sum_it(5, 3) == 8
#
# def test_not_equal():
#     assert sum_it(4, 8) == 11

def test_get_code():
    result = requests.get(base_url)
    print(result)
    assert result.status_code == 200

    def test_create_booking():
        responce = requests.post(base_url)
        payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            }
        "additionalneeds": "Breakfast"
    }
        responce =  requests.post(base_url,json=payload)
        print(responce,json()['bookingid'])
        assert  responce.status_code == 200

def test_check_created_booking():
    result = requests.get(f"{base_url}/2107")
    print(result.json())
    assert result.status_code == 200
    assert result.json()['firstname'] == "James"

#gef test_update_booking


def test_get_token():
    authdata = {
        "username":  "admin",
        "password": "password123"
    responce = requests.post(auth_url, json=authdata)
    token =
    }