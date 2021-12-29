import os

import pytest

user_create_data = {
    "name": "morpheus",
    "job": "leader"
}

update_user_put = {
    "name": "Naeem Hassan",
    "job": "SQA Engineer"
}

update_user_patch = {
    "name": "Hafiz Naeem Hassan",
    "job": "SQA Engineer"
}

register_user_with_valid_payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

register_user_with_invalid_payload = {
    "email": "eve.holt@reqres.in"
}

login_user = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
