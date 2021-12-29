from http import HTTPStatus

import pytest


class TestGetUserListApi:

    @pytest.mark.run(order=2.1)
    def test_get_user_list(self, get_user_list_fixture):
        response = get_user_list_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK
        json_data = response.json()
        print(json_data)

    @pytest.mark.run(order=2.2)
    def test_get_signle_user(self, get_single_user_fixture):
        response = get_single_user_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK
        json_data = response.json()
        print(json_data)

    @pytest.mark.run(order=2.3)
    def test_get_single_user_not_found(self, get_single_user_not_found_fixture):
        response = get_single_user_not_found_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK, "Not Found"

    @pytest.mark.run(order=2.4)
    def test_get_list_resource(self, get_list_resource_fixture):
        response = get_list_resource_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK
        json_data = response.json()
        print(json_data)

    @pytest.mark.run(order=2.5)
    def test_get_single_resource(self, get_signle_resource_fixture):
        response = get_signle_resource_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK
        json_data = response.json()
        print(json_data)

    @pytest.mark.run(order=2.5)
    def test_create_user(self, get_create_user_fixture):
        response = get_create_user_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK, "Not Created"
        json_data = response.json()
        print(json_data)

    @pytest.mark.run(order=2.6)
    def test_update_user_put(self, update_single_user_using_put_fixture):
        response = update_single_user_using_put_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK, "Not Updated"

    @pytest.mark.run(order=2.7)
    def test_update_user_patch(self, update_single_user_using_patch_fixture):
        response = update_single_user_using_patch_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK, "Not Updated"

    @pytest.mark.run(order=2.8)
    def test_delete_user(self, delete_single_user_fixture):
        response = delete_single_user_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK, "Not Updated"

    @pytest.mark.run(order=2.9)
    def test_register_user_with_invalid_payload(self, register_single_user_with_invalid_payload_fixture):
        response = register_single_user_with_invalid_payload_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK, "Not Registered"

    @pytest.mark.run(order=2.10)
    def test_register_user_with_valid_payload(self, register_single_user_with_valid_payload_fixture):
        response = register_single_user_with_valid_payload_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK, "Registered"

    @pytest.mark.run(order=2.11)
    def test_login_user(self, login_user_fixture):
        response = login_user_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK, "Not Login"

    @pytest.mark.run(order=2.12)
    def test_delay_response(self, delay_response_fixture):
        response = delay_response_fixture
        status_code = response.status_code
        assert status_code == HTTPStatus.OK, "No Response"
