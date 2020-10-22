# coding=utf-8
'''
封装生成日志的类
'''

import logging
from common.handlepath import *
from common.readconfig import conf
import os

class HandleLog(object):
    @staticmethod
    def create_logger():
        # 创建日志的收集器，设置日志等级
        mylog = logging.getLogger(conf.get('log', 'name'))
        mylog.setLevel(conf.get('log', 'level'))

        # 创建输出到控制台的处理器，设置等级
        sh = logging.StreamHandler()
        sh.setLevel(conf.get('log', 'sh_level'))
        # 将输出到控制台的处理器加入到日志
        mylog.addHandler(sh)

        # 创建输出到文件的处理器，设置等级
        fh = logging.FileHandler(filename=os.path.join(LOGSDIR, 'log.log'),
                                 encoding='utf8')
        fh.setLevel(conf.get('log', 'fh_level'))
        # 将输出到w文件的处理器加入到日志
        mylog.addHandler(fh)

        # 设置日志输出格式
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)
        fh.setFormatter(fm)

        return mylog


log = HandleLog.create_logger()
# log.info('debug')