"""
a file named common_verification.py inside a helpers directory is typically used to
centralize common validation logic or assertions that multiple test cases might require.
This structure promotes code reusability and keeps test files clean by abstracting repetitive checks
into helper functions.

The helpers directory often contains utility functions that support the main test cases,
and common_verification.py may specifically focus on reusable verification or assertion functions.
"""

def verify_http_status_code(response_data,expected_data):
    assert response_data.status_code == expected_data, "Failed status code match"

def verify_response_key(key, expected_data):
    assert key == expected_data

def verify_json_key_for_not_null(key):
    assert key!=0,"Failed - key is non empty"
    assert key > 0, "Failed - key is not greater than zero"

def verify_json_key_for_not_null_token(key):
    assert key!=0, "Failed - key is non empty"

def verify_response_delete(response):
    assert "created" in response
