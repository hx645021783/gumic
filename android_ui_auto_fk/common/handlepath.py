# coding=utf-8
'''
此模块生成项目所需路径
'''

import os

# 项目目录路径
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASEDIR)

# app目录路径
APPDIR = os.path.join(BASEDIR, 'app')
# print(APPDIR)

# config包路径
CONFIGDIR = os.path.join(BASEDIR, 'config')
# print(CONFIGDIR)

# common包路径
COMMONDIR = os.path.join(BASEDIR, 'common')
# print(COMMONDIR)

# data包路径
DATADIR = os.path.join(BASEDIR, 'data')
# print(DATADIR)

# logs包路径
LOGSDIR = os.path.join(BASEDIR, 'logs')
# print(LOGSDIR)

# report包路径
REPORTDIR = os.path.join(BASEDIR, 'report')
# print(REPORTDIR)

# testcase包路径
TESTCASEDIR = os.path.join(BASEDIR, 'testcase')
# print(TESTCASEDIR)
