"""
yaml读取工具类
"""
# coding=utf-8
import time

import yaml

from config.config import file_paths


class ReadYamlUtils:
    @classmethod
    def read_yaml(cls, file_path):
        try:
            with open(file_path, 'r', encoding="utf-8") as f:
                yaml_data = yaml.safe_load(f)
                print(type(yaml_data))
                return yaml_data
        except Exception as e:
            print(e, "失败")

    @classmethod
    def write_token_to_yaml(cls, token, filepath):
        try:
            with open(filepath, "a", encoding="utf-8") as f:
                if isinstance(token, dict):
                    f.write(yaml.dump(token, allow_unicode=True))
                else:
                    print("要传入键值对形式")
        except Exception as e:
            print(e, "写入 失败")

    @classmethod
    def read_data_yaml(cls, first, twoname=None):
        """
        
        :param first: 
        :param twoname: 
        :return: 
        """""
        # 他妈的 怎么把她抽出来

        path = file_paths["data_yaml"]
        with open(path, 'r', encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            if twoname is None:
                return yaml_data[first]
            else:
                return yaml_data[first][twoname]

    def get_time(self):
        return time.ctime()


if __name__ == '__main__':
    # # file = "/Users/yang/Documents/pySpace8/testcase/login/login.yaml"
    read = ReadYamlUtils()
    print(read.read_data_yaml("token"))
    # print(result)
