import allure
import pytest
import requests
from src.helpers.api_request_wrapper import post_request,get_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.utils.utility import Utils
from src.helpers.common_verification import *
import logging



@allure.title("A Sample Test Case TC#1")
@pytest.mark.smoke
def test_sample_testcase_1():

    assert True == True
    assert 5+5 == 10
    assert 5+2 == 7
    print("Test is done!")

class TestCreateBooking():

    @allure.title("Verify that Creating booking status and Booking Id should not be null")
    @allure.description("Create a booking from payload and verify that booking id should not be null")
    @pytest.mark.positive
    def test_Create_booking_positive(self):
        Logger = logging.getLogger(__name__)
        Logger.info("Starting the TestCase TC#1 - positive")
        response = post_request(url = APIConstants().url_create_booking(),
                                headers = Utils().common_headers_json(),
                                data = payload_create_booking(),
                                in_json=True)
        print("response.json:\t", response.json())
        verify_http_status_code(response_data= response,expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        Logger.info("Booking Id is: "+ str(response.json()["bookingid"]))
        Logger.info("End of the TestCase TC#1 - positive")

    @allure.title("Getting all the booking Ids TestCase#2")
    @allure.description("Fetching all the booking Ids")
    @pytest.mark.positive
    def get_bookingids(self):
        response = get_request(url=APIConstants().base_url(),auth=None)

        response_data = response.json()
        print(response_data)
