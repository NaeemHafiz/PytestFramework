import configparser

import requests

from constants import CONFIG_FILE


class ReqResRequestClient:
    def __init__(self, env: str):
        config_loader = configparser.ConfigParser()
        config_loader.read_file(open(CONFIG_FILE))
        self.env = env
        self.service_url = config_loader.get(env, "base_url")

    def get_req(self, url, headers=None, json_payload=None, path_params=None, form_data=None, file=None):
        response = requests.get(
            url=self.build_url(self.service_url, url),
            data=form_data,
            headers=headers,
            params=path_params,
            json=json_payload,
            files=file
        )
        return response

    def post_req(self, url, headers=None, json_payload=None, path_params=None, form_data=None, files=None):
        response = requests.post(
            url=self.build_url(self.service_url, url),
            data=form_data,
            headers=headers,
            params=path_params,
            json=json_payload,
            files=files
        )
        return response

    def delete_req(self, url, headers=None, json_payload=None, path_params=None, form_data=None, files=None):
        response = requests.delete(
            url=self.build_url(self.service_url, url),
            data=form_data,
            headers=headers,
            params=path_params,
            json=json_payload,
            files=files
        )
        return response

    def put_req(self, url, headers=None, json_payload=None, path_params=None, form_data=None, files=None):
        response = requests.put(
            url=self.build_url(self.service_url, url),
            data=form_data,
            headers=headers,
            params=path_params,
            json=json_payload,
            files=files
        )
        return response

    def patch_req(self, url, headers=None, json_payload=None, path_params=None, form_data=None, files=None):
        response = requests.patch(
            url=self.build_url(self.service_url, url),
            data=form_data,
            headers=headers,
            params=path_params,
            json=json_payload,
            files=files
        )
        return response

    @staticmethod
    def build_url(base_url, tail_end):
        return base_url + tail_end
