import requests

# response = requests.get('https://restful-booker.herokuapp.com/booking')
# print(response.headers)

def create_booking(name, surname):
    url = 'https://restful-booker.herokuapp.com/booking'

    data = {
    "firstname": name,
    "lastname": surname,
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"}

    response = requests.post(url=url, json=data)
    #print(response.json())
    return(response.json())

#create_booking()
def get_booking_by_id(id_):
    url = f'https://restful-booker.herokuapp.com/booking/:id{id_}'

    response = requests.get(url)
    #return response.json()
    print(response.json())

#booking = create_booking()
##print(booking)
#id = booking['booking']
#get_booking_by_id(id_)

def create_token():
    url = 'https://restful-booker.herokuapp.com/auth'
    data = {
    "username" : "admin",
    "password" : "password123"}

    response = requests.post(url=url, json=data)
#    print(response.json()) #{'token': '1f2a136efd0c954'}
    return response.json()['token']
# create_token()
# print(create_token())
def test_create_booking():
    name = 'Mike'
    surname = 'Simpson'

    booking = create_booking(name=name, surname=surname)
    id_ = booking['bookingid']

    new_booking = get_booking_by_id(id_)

    print(new_booking)


    #print(booking)