import pytest

from client.req_res_client import ReqResRequestClient


@pytest.fixture(scope="session")
def req_res_client(env: str):
    req_res_client = ReqResRequestClient(env)
    return req_res_client


