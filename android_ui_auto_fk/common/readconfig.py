# coding=utf-8
'''
此模块封装读取解析配置文件的类
'''

from configparser import ConfigParser
import os
from common.handlepath import *

class ReadConfig(ConfigParser):
    def __init__(self, file_path):
        ConfigParser.__init__(self)
        self.file_path = file_path
        # 读取ini文件
        self.read(file_path)
        # 之后就可以通过实例的get(section, option)获取value

    def write_data(self, section, option, value=None):
        # 往ini文件写入数据
        self.set(section, option, value)
        self.write(fp=open(self.file_path))


conf = ReadConfig(os.path.join(CONFIGDIR, 'config.ini'))
# print(conf.get('log', 'name'))
