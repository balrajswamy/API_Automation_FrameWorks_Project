#API TestCAse
#URL - from api_constants.py
#Headers - from utility.py
#payload - from payload_manager.py
#HTTP Requests/methds - from api_request_wrapper.py
#verification - from common_verification.py
import json

import pytest
import requests
import allure

from src.helpers.api_request_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.utils.utility import Utils
from src.helpers.common_verification import *
import logging




class TestCreateBooking():

    @allure.title("Verify that Creating booking status and Booking Id should not be null")
    @allure.description("Create a booking from payload and verify that booking id should not be null")
    @pytest.mark.positive
    def test_Create_booking_positive(self):
        Logger = logging.getLogger(__name__)
        Logger.info("Starting the TestCase TC#1 - positive")
        response = post_request(url = APIConstants().url_create_booking(),
                                headers = Utils().common_headers_json(),
                                auth = None,
                                data = payload_create_booking(),in_json=True)



        print("response.json:\t", response.json())
        verify_http_status_code(response_data= response,expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        Logger.info("Booking Id is: "+ str(response.json()["bookingid"]))
        Logger.info("End of the TestCase TC#1 - positive")

    @allure.title("Verify that Create booking does not work with no payload")
    @allure.description("Create a booking with no payload and verifying/checking a booking id")
    @pytest.mark.negative
    def test_Create_booking_negative(self):
        Logger = logging.getLogger(__name__)
        Logger.info("Starting the TestCase TC#2 - negative")
        response = post_request(url=APIConstants().url_create_booking(),
                                headers=Utils().common_headers_json(),
                                auth=None, data={},
                                in_json=False)

        verify_http_status_code(response_data=response, expected_data=500)
        verify_json_key_for_not_null(response.json()["bookingid"])
        Logger.info("Booking Id is: " + str(response.json()["bookingid"]))
        Logger.info("End of the TestCase TC#2 - negative")

