import pytest
import requests
import response

base_url = 'https://restful-booker.herokuapp.com/booking'
auth_url = 'https://restful-booker.herokuapp.com/auth'


# def sum_it(x,y):
#     return x + y

# def test_equal():
#     assert sum_it(4,6) == 10
#
# def test_not_equal():
#     assert sum_it(4,8)== 11

def test_get_code():
    result = requests.get(base_url)
    print(result)
    assert result.status_code == 200


def test_get_booking_by_id():
    response = requests.get(f'{base_url}/19')
    response_data = response.json()
    print(response_data)
    expected_keys = [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates"
        #"additionalneeds"
    ]

    assert response.status_code == 200
    for key in expected_keys:
        assert key in response_data.keys()
    assert isinstance(response_data.get('firstname'),str)
    assert isinstance(response_data.get('totalprice'),int)


def test_create_bboking():
    payload = {
        "firstname": "Alex",
        "lastname": "Brown",
        "totalprice": 700,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2024-01-02"
        }
    }

    response = requests.post(base_url, json=payload)
    print(response.json()["bookingid"])
    booking_id = (response.json()["bookingid"])
    return booking_id
    assert response.status_code == 200


def test_check_created_booking():

    response = requests.get(f'{base_url}')
    print(response.json())
    assert response.status_code == 200
    assert response.json()["firstname"] == "Alex"
    #assert data["booking']["firstname"] == "Jim"


def test_update_booking():
    payload = {
        "firstname": "Alex",
        "lastname": "Brown",
        "totalprice": 700,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2024-01-02"
        },
        "additionalneeds": "Lunch"

    }


def test_get_token():
    authdata = {
        "username": "admin",
        "password": "password123"
    }
    resource = requests.post(auth_url, json=authdata)
    token = response.json()["token"]
    print(token)
    assert response.status_code == 200




