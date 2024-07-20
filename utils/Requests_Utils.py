import json

import pytest
import requests

from config.config import bash_host, file_paths
from utils.ReadYaml_Utils import ReadYamlUtils
from utils.Replace_yaml_utils import ReplaceUtils


class RequestsUtils:
    @classmethod
    def auto_request(cls, method, url, params=None, data=None, json=None, headers=None, cookies=None, **kwargs):
        """

        :param method:
        :param url:
        :param params:
        :param data:
        :param json:
        :param headers:
        :param cookies:
        :param kwargs:
        :return:
        """
        real_resp = requests.request(method, url, params=params, data=data, json=json, headers=headers, cookies=cookies,
                                     **kwargs)
        return real_resp

    @classmethod
    def real_request(cls, request_yaml):
        # yaml 文件 赋值给replace_after
        replace_after = ReplaceUtils.replace_yaml_data(request_yaml)
        if "data" in replace_after:
            real_resp = requests.request(method=replace_after["method"], url=bash_host + replace_after["url"],
                                         headers=replace_after["headers"], data=replace_after["data"])
            return real_resp
        elif "json" in replace_after:
            real_resp = requests.request(method=replace_after["method"], url=bash_host + replace_after["url"],
                                         headers=replace_after["headers"], json=replace_after["json"])
            return real_resp
        elif "params" in replace_after:
            real_resp = requests.request(method=replace_after["method"], url=bash_host + replace_after["url"],
                                         headers=replace_after["headers"], params=replace_after["params"])
            return real_resp
        else:
            real_resp = requests.request(method=replace_after["method"], url=bash_host + replace_after["url"],
                                         headers=replace_after["headers"])
            return real_resp

# replace_after = ReplaceUtils.replace_yaml_data(ReadYamlUtils.read_yaml(file_paths["carts_yaml"]))
# print(RequestsUtils.real_request(request_yaml=replace_after))


