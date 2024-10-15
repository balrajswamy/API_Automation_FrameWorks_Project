import json

import pytest
import requests


def get_request(url,auth):

    response = requests.get(url=url,auth=auth)
    return response.json()

def post_request(url,headers,payload, in_json): # in_json is a boolean
    post_response = requests.post(url=url, headers=headers, data = json.dumps(payload),in_json=True)
    #post_response = requests.post(url=url, headers=headers, data=payload)

    if in_json is True:
        return post_response.json()
    return post_response

def patch_request(url,auth, headers, payload, in_json): # in_json is a boolean
    patch_response = requests.patch(url=url, headers=headers, auth = auth, data=payload)

    if in_json is True:
        return patch_response.json()
    return patch_response

def put_request(url,auth, headers, payload, in_json): # in_json is a boolean
    put_response = requests.put(url=url, headers=headers, auth = auth, json=payload)

    if in_json is True:
        return put_response.json()
    return put_response

def delete_request(url,auth, headers, in_json): # in_json is a boolean
    delete_response = requests.delete(url=url,headers=headers, auth=auth)

    if in_json is True:
        return delete_response.json()
    return delete_response