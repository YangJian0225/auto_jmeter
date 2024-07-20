import os

"""
配置了路径拼接
"""
dir_path = os.path.dirname(os.path.dirname(__file__))
# print(dir_path)
bash_host = "https://you-gateway.mashibing.com"

file_paths = {
    # token的存放位置
    "data_yaml": os.path.join(dir_path, "data", "data.yaml"),
    # 多层目录要把前一层加上去
    "login_yaml": os.path.join(dir_path, "testcase/login", "login.yaml"),
    "carts_yaml": os.path.join(dir_path, "testcase/carts", "carts.yaml"),
    "logs": os.path.join(dir_path, "logs")


}
# print(file_paths["login_yaml"])
