import datetime
import logging
import os
# 日志的格式，以时间来开如命名
import time

from config.config import file_paths

log_path = file_paths["logs"]
print(log_path)

# 进行一个判断，如果这个路径不存在，就创建这个路径
if not os.path.exists(log_path):
    os.mkdir(log_path)
else:
    print("logs这个路径已经存在了，不需要再去创建了。。。")

logfile_name = log_path + "/{}.log".format(time.strftime("%Y%m%d%H%M%S"))


class LogUtils:
    def __init__(self):
        self.handle_overdue_log()
        print("走了LogUtils的init方法。。。")

    # 日志保存的时间
    def handle_overdue_log(self):
        """处理过期日志文件"""
        # 获取系统的当前时间
        now_time = datetime.datetime.now()
        print("当前的时间是:", now_time)
        # 日期偏移30天，最多保留30的日志文件，超过自动清理
        offset_date = datetime.timedelta(days=-1)
        # 获取前一天时间戳
        before_date = (now_time + offset_date).timestamp()
        # 找到目录下的文件
        files = os.listdir(log_path)
        for file in files:
            if os.path.splitext(file)[1]:
                filepath = log_path + "/" + file
                file_create_time = os.path.getctime(filepath)  # 获取文件创建时间,返回时间戳
                # dateArray = datetime.datetime.fromtimestamp(file_createtime) #标准时间格式
                # print(dateArray.strftime("%Y--%m--%d %H:%M:%S"))
                if file_create_time < before_date:
                    os.remove(filepath)
                else:
                    continue

    def create_logger(*args, **kwargs):
        # 创建自己的日志收集器
        my_log = logging.getLogger("my_log")
        # 设置收集的日志等级，设置为DEBUG等级
        my_log.setLevel("INFO")
        # 日志输出渠道
        # 创建一个日志输出渠道（输出到控制台），并且设置输出的日志等级为INFO以上
        l_s = logging.StreamHandler()
        l_s.setLevel("INFO")
        # 创构建一个日志输出渠道（输出到文件），并且设置输出的日志等级为DEBUG以上
        l_f = logging.FileHandler(logfile_name, encoding='utf8')
        l_f.setLevel("INFO")
        ''''
        第一个参数是 日志的文件名
        第二个参数是日志的大小
        第三个参数是  日志的个数
        第四个参数是 编码格式
        '''
        # rf = RotatingFileHandler(filename=logfile_name,
        #                          maxBytes=1024*10,
        #                          backupCount=5,
        #                          encoding="utf8")

        # 将日志输出渠道添加到日志收集器中
        my_log.addHandler(l_f)

        # 将日志输出渠道添加到日志收集器中
        my_log.addHandler(l_s)
        # my_log.addHandler(l_f)
        # 设置日志输出的格式
        ft = "%(asctime)s - [%(filename)s -->line:%(lineno)d] - %(levelname)s: %(message)s"
        ft = logging.Formatter(ft)
        # 设置控制台和日志文件输出日志的格式
        l_s.setFormatter(ft)
        # l_f.setFormatter(ft)
        l_f.setFormatter(ft)
        return my_log


logutils = LogUtils()

logs = logutils.create_logger()
