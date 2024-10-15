"""
a file named payload_manager.py inside a helpers directory is typically used to manage and
generate different payloads (data sent in HTTP requests) for API testing.
Instead of hardcoding payloads in test files, payload_manager.py centralizes the creation and
manipulation of request bodies, making tests more maintainable, readable, and reusable

"""



import json
def payload_create_booking():
    payload = {
                "firstname": "Ramana",
                "lastname": "Brown",
                "totalprice": 112,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2018-01-01",
                    "checkout": "2019-01-01"
                },
                "additionalneeds" : "Breakfast"
            }

    return json.dumps(payload)