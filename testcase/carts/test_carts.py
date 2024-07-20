import pytest

from config.config import file_paths, bash_host
from utils.ReadYaml_Utils import ReadYamlUtils
from utils.Replace_yaml_utils import ReplaceUtils
from utils.Requests_Utils import RequestsUtils


class TestCarts(RequestsUtils):
    # @pytest.mark.parametrize("result",
    #                          ReadYamlUtils.read_yaml(file_paths["carts_yaml"]))
    # def test_carts(self, result):
    #     replace_after = ReplaceUtils.replace_yaml_data(result)
    #     print(type(replace_after))
    #     # print(replace_after["replace_after"])
    #     # if "headers" in replace_after :
    #     #     print(111)
    #     #     print(replace_after["headers"])
    #     # else:
    #     #     print(222)
    #     #     print(replace_after["headers"])
    #     headers = {
    #         "Authorization": replace_after["headers"]["Authorization"]
    #
    #     }
    #     # print(headers)
    #     req = RequestsUtils.auto_request(url=bash_host + result['url'], method=result["method"],
    #                                      headers=headers)
    #     print(req.json())

    @pytest.mark.parametrize("result",
                             ReadYamlUtils.read_yaml(file_paths["carts_yaml"]))
    def test_carts2(self, result):
        data = file_paths["carts_yaml"]
        req = RequestsUtils.real_request(request_yaml=result)
        # print(req.text)
        ReplaceUtils.replace_yaml_by_extract(response_data=req.text, yaml_path=data, replace_value="message")
