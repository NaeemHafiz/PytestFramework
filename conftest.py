import pytest
from constants import GET_USER_LIST_END_POINT_URL, GET_SINGLE_USER_END_POINT_URL, GET_LIST_RESOURCE_END_POINT_URL, \
    GET_SINGLE_RESOURCE_END_POINT_URL, CREATE_USER_END_POINT_URL, \
    DELETE_SINGLE_USER_END_POINT_URL, UPDATE_SINGLE_USER_END_POINT_URL, REGISTER_SINGLE_USER_END_POINT_URL, \
    LOGIN_SUCCESSFUL_USER_END_POINT_URL, DELAYED_RESPONSE_END_POINT_URL
from client.req_res_client import ReqResRequestClient


# Generic Fixture
@pytest.fixture(scope="session", autouse=True)
def req_res_client(env: str):
    req_res_client = ReqResRequestClient(env)
    return req_res_client


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help="Environments to run test: prod"
    )


@pytest.fixture(scope="session")
def env(pytestconfig):
    valid_env = ["prod"]
    given_env = pytestconfig.getoption("env")
    assert given_env in valid_env, "Not a valid environment - valid environment: prod"
    return given_env


# Get User List Fixture
@pytest.fixture(scope="class")
def get_user_list_fixture(req_res_client):
    response = req_res_client.get_req(url=GET_USER_LIST_END_POINT_URL, path_params={'page': 2})
    return response


# GET SINGLE USER
@pytest.fixture(scope="class")
def get_single_user_fixture(req_res_client):
    response = req_res_client.get_req(url=GET_SINGLE_USER_END_POINT_URL)
    return response


# GET SINGLE USER NOT FOUND
@pytest.fixture(scope="class")
def get_single_user_not_found_fixture(req_res_client):
    response = req_res_client.get_req(url=GET_SINGLE_USER_END_POINT_URL)
    return response


# GET LIST OF RESOURCE
@pytest.fixture(scope="class")
def get_list_resource_fixture(req_res_client):
    response = req_res_client.get_req(url=GET_LIST_RESOURCE_END_POINT_URL)
    return response


# GET SINGLE RESOURCE
@pytest.fixture(scope="class")
def get_signle_resource_fixture(req_res_client):
    response = req_res_client.get_req(url=GET_SINGLE_RESOURCE_END_POINT_URL)
    return response


# CREATE USER
@pytest.fixture(scope="class")
def get_create_user_fixture(req_res_client):
    response = req_res_client.get_req(url=CREATE_USER_END_POINT_URL, json_payload={
        "name": "morpheus",
        "job": "leader"
    })
    return response


# UPDATE SINGLE USER USING PUT
@pytest.fixture(scope="class")
def update_single_user_using_put_fixture(req_res_client):
    response = req_res_client.get_req(url=UPDATE_SINGLE_USER_END_POINT_URL, json_payload={
        "name": "Naeem Hassan",
        "job": "SQA Engineer"
    })
    return response


# UPDATE SINGLE USER USING PATCH
@pytest.fixture(scope="class")
def update_single_user_using_patch_fixture(req_res_client):
    response = req_res_client.get_req(url=UPDATE_SINGLE_USER_END_POINT_URL, json_payload={
        "name": "Hafiz Naeem Hassan",
        "job": "SQA Engineer"
    })
    return response


# DELETE SINGLE USER
@pytest.fixture(scope="class")
def delete_single_user_fixture(req_res_client):
    response = req_res_client.get_req(url=DELETE_SINGLE_USER_END_POINT_URL)
    return response


# REGISTER SINGLE USER WITH INVALID PAYLOAD
@pytest.fixture(scope="class")
def register_single_user_with_invalid_payload_fixture(req_res_client):
    response = req_res_client.get_req(url=REGISTER_SINGLE_USER_END_POINT_URL, json_payload={
        "email": "eve.holt@reqres.in"
    })
    return response


# REGISTER SINGLE USER WITH VALID PAYLOAD
@pytest.fixture(scope="class")
def register_single_user_with_valid_payload_fixture(req_res_client):
    response = req_res_client.get_req(url=REGISTER_SINGLE_USER_END_POINT_URL, json_payload={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })
    return response


# LOGIN  USER
@pytest.fixture(scope="class")
def login_user_fixture(req_res_client):
    response = req_res_client.get_req(url=LOGIN_SUCCESSFUL_USER_END_POINT_URL, json_payload={
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    })
    return response


# DELAY RESPONSE
@pytest.fixture(scope="class")
def delay_response_fixture(req_res_client):
    response = req_res_client.get_req(url=DELAYED_RESPONSE_END_POINT_URL)
    return response
