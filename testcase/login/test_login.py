import logging

import allure
import pytest
import requests
from requests import post
import pytest

from config.config import file_paths, bash_host
from utils.Log_Utils import logs
from utils.ReadYaml_Utils import ReadYamlUtils
from utils.Requests_Utils import RequestsUtils


# from utils.Requests_Utils import RequestsUtils


class TestLogin:
    @allure.story("登录测试用例")
    @pytest.mark.parametrize("result", ReadYamlUtils.read_yaml(file_paths['login_yaml']))
    def test_logins(self, result):
        #
        res = RequestsUtils.auto_request(method=result['method'], url=bash_host + result['url'], json=result['json'])
        logs.error("接口%s" % {str(res.json())})
        # 获取token
        print(res.headers)
        print(res.raw)
        login_token = res.json()["data"]["token"]
        print(res.json()["data"]["token"])
        # 把token写入data.yaml 这边也要把写入方法抽取出来
        ReadYamlUtils.write_token_to_yaml(filepath="/Users/yang/Documents/pySpace8/data/data.yaml",
                                          token={"token": login_token})
        # allure.attach(res)

    @pytest.mark.parametrize("result", ReadYamlUtils.read_yaml(file_paths['login_yaml']))
    def test_aaa(self, result):
        print(type(result))
        print(RequestsUtils.real_request(request_yaml=result).headers)
        res = RequestsUtils.real_request(request_yaml=result).json()
        allure.attach(res["data"]["token"])

