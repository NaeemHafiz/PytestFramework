import requests
import http

BASE_URL = "https://reqres.in/api/"
GET_USER_LIST = BASE_URL + "users?page=2"
GET_SINGLE_USER = BASE_URL + "users/2"
GET_SINGLE_USER_NOT_FOUND = BASE_URL + "users/23"
GET_LIST_RESOURCE = BASE_URL + "unknown"
GET_SINGLE_RESOURCE = BASE_URL + "unknown/2"
GET_SINGLE_RESOURCE_NOT_FOUND = BASE_URL + "unknown/23"
CREATE_USER = BASE_URL + "users"
UPDATE_SINGLE_USER = BASE_URL + "users/2"
DELETE_SINGLE_USER = BASE_URL + "users/2"
REGISTER_SINGLE_USER = BASE_URL + "register"
LOGIN_SUCCESSFUL_USER = BASE_URL + "login"
DELAYED_RESPONSE = BASE_URL + "users?delay=3"


# GET USER LIST
def test_get_user_list():
    response = requests.get(GET_USER_LIST)
    assert response.status_code == http.HTTPStatus.OK
    print(response.content)


# GET SINGLE USER
def test_get_signle_user():
    response = requests.get(GET_SINGLE_USER)
    assert response.status_code == http.HTTPStatus.OK
    print(response.content)


# GET SINGLE USER NOT FOUND
def test_get_single_user_not_found():
    response = requests.get(GET_SINGLE_USER_NOT_FOUND)
    assert response.status_code == http.HTTPStatus.NOT_FOUND, "Not Found"
    print(response.content)


# GET LIST OF RESOURCE
def test_get_list_resource():
    response = requests.get(GET_LIST_RESOURCE)
    assert response.status_code == http.HTTPStatus.OK, "Not Found"
    print(response.content)


# GET SINGLE RESOURCE
def test_get_single_resource():
    response = requests.get(GET_SINGLE_RESOURCE_NOT_FOUND)
    assert response.status_code == http.HTTPStatus.OK, "Not Found"
    print(response.content)


# CREATE USER
def test_create_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(CREATE_USER, data)
    assert response.status_code == http.HTTPStatus.CREATED, "Not Created"
    print(response.status_code)


# UPDATE SINGLE USER USING PUT
def test_update_user_put():
    data = {
        "name": "Naeem Hassan",
        "job": "SQA Engineer"
    }
    response = requests.put(UPDATE_SINGLE_USER, data)
    assert response.status_code == http.HTTPStatus.OK, "Not Updated"
    print(response.status_code)


# UPDATE SINGLE USER USING PATCH
def test_update_user_patch():
    data = {
        "name": "Hafiz Naeem Hassan",
        "job": "SQA Engineer"
    }
    response = requests.patch(UPDATE_SINGLE_USER, data)
    assert response.status_code == http.HTTPStatus.OK, "Not Updated"
    print(response.status_code)


# DELETE SINGLE USER
def test_delete_user():
    response = requests.delete(DELETE_SINGLE_USER)
    assert response.status_code == 204, "Not Deleted"
    print(response.status_code)


# REGISTER SINGLE USER WITH VALID PAYLOAD
def test_register_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(REGISTER_SINGLE_USER, data)
    assert response.status_code == http.HTTPStatus.OK,"Not Registered"
    print(response.content)


# REGISTER SINGLE USER WITH INVALID PAYLOAD
def test_register_user_with_invalid_payload():
    data = {
        "email": "eve.holt@reqres.in"
    }
    response = requests.post(REGISTER_SINGLE_USER, data)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST, "Not Registered"
    print(response.content)


# LOGIN USER
def test_login_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(LOGIN_SUCCESSFUL_USER, data)
    assert response.status_code == http.HTTPStatus.OK, "Not Login"
    print(response.content)


# DELAY RESPONSE
def test_delay_response():
    response = requests.get(DELAYED_RESPONSE)
    assert response.status_code == http.HTTPStatus.OK, "No Response"
    json_data = response.json()
    print(json_data['data'][1])
