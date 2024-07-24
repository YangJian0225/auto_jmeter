import json
import re

import yaml

from config.config import file_paths
from utils.ReadYaml_Utils import ReadYamlUtils


class ReplaceUtils:
    """
    替换token
    """

    # filepath是对应要替换的yaml文件路径
    @classmethod
    def replace_yaml_data(cls, filepath):
        """
        实现逻辑：
        解析完成的yaml流作为入参赋值给str_data
        先for循环${做作为关键字检索，拿到yaml文件里面一共有几个需要替换的数据，然后获取他们对应的index值，
        在通过str_data[切片index]来获取需要替换的整个字段，然后在通过切片分别取出方法名和参数，
        实例化了ReadYamlUtils，这里面放着是yaml对应的方法名，还需要判断处理是否方法有参数，
        通过getattr，去实现通过类---方法调用返回，赋值给data_yaml完成替换 这边需要优化把路径从read_data_yaml的路径抽取出来


        :param filepath:
        :return:
        """
        str_data = json.dumps(filepath, ensure_ascii=False)
        print(type(str_data))
        for i in range(str_data.count("${")):
            #     # 取头尾数据
            str_data_start = str_data.index("$")
            str_data_end = str_data.index("}")
            # 把需要替换的data取出
            want_replace_data = str_data[str_data_start:str_data_end + 1]
            # want_replace_name ==方法名
            want_replace_name = want_replace_data[2:want_replace_data.index("(")]
            # want_replace_para ==参数
            want_replace_para = want_replace_data[want_replace_data.index("(") + 1:want_replace_data.index(")")]
            # 实例化类变量
            read_yaml_utils = ReadYamlUtils()
            # 调用${read_data_yaml(token)} 取read_yaml_utils里面的对应want_replace_name方法传入want_replace_para参数
            # 额外处理无参数状态
            if want_replace_para == '':
                data_yaml = getattr(read_yaml_utils, want_replace_name)()
            else:
                data_yaml = getattr(read_yaml_utils, want_replace_name)(
                    *want_replace_para.split(",") if want_replace_data else "")
            # print(data_yaml)
            # 如果data_yaml返回的不是一个字符串，而是是个列表，要把他转成字符串形式
            if isinstance(data_yaml, list):
                data_yaml = ",".join(x for x in data_yaml)
            # for item in data_yaml:
            # 进行字符串替换
            str_data = str_data.replace(want_replace_data, data_yaml)
            # 如果 new_data是字符换类型，把她转换成字段类型，为了后面去取数据
        else:
            if isinstance(str_data, str):
                str_data = json.loads(str_data)
            # print(str_data)
            # print(type(str_data))
            return str_data
        # return new_data

    """
    接口关联  入参：yaml文件路径、接口返回报文
    先判断 关联字段存不存在yaml字段
    存在即去除正则表达字段，去报文里面取
    取出来之后存在本地
     
    """

    @classmethod
    def replace_yaml_by_extract(cls, yaml_path, response_data=None, replace_value=None, replace_key="extract"):
        """
        传入yaml地址、需要替换的关键字，默认为"extract"，replace_value为提取的正则
        :param response_data: 响应体用于提取
        :param yaml_path: 传入yaml地址
        :param replace_key: 需要提取的关键字，默认为"extract"
        :param replace_value: replace_value为提取的正则 默认none
        :return:
        """
        with open(yaml_path, "r", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            for dict_yaml in yaml_data:
                if replace_key in dict_yaml and replace_value is not None:
                    # 取出traceid
                    re_keyword = dict_yaml[replace_key][replace_value]
                else:
                    re_keyword = dict_yaml[replace_key]
                re_data = (re.search(re_keyword, response_data)).group(1)
                print(re_data)
                # print(type(re_data))
                ReadYamlUtils.write_token_to_yaml(token={replace_value: re_data}, filepath=file_paths["data_yaml"])


if __name__ == '__main__':
    # firsrdata = ReadYamlUtils.read_yaml(file_paths["carts_yaml"])
    # print(firsrdata)
    # ReplaceUtils.replace_yaml_data(filepath=firsrdata)
    data = file_paths["carts_yaml"]
    replace = ReplaceUtils()
    replace.replace_yaml_data(filepath=data)
