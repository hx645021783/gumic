# coding=utf-8

'''
PageObject类:采用Java中的page object设计模式 P0设计模式，封装所有的页面公共方法
               使得页面中的每一个控件元素都变成了对象的属性
               只要继承这个基类，就可以拿到这个类中的一切类方法，进行定位元素
set_driver:传入一个driver对象
get_driver:获取driver对象
find_element()方法封装定位方法，只需传入属性名和属性值就能获得所定位的元素
单列设计模式
'''

import unittest
from appium import webdriver
from time import sleep
from android.AndroidBase import android_base
from common.handlelogs import log

class PageObject(object):
    '''

    '''
    def __init__(self):
        android_base.install_app()
        android_base.get_desired_caps()
        self.driver = webdriver.Remote(android_base.appium_url, android_base.desired_caps)

    def get_driver(self):
        return self.driver

    def do_something(self):
        # android_base.install_app()
        log.info('正在启动APP')
        self.driver = webdriver.Remote(android_base.appium_url, android_base.desired_caps)
        log.info('连接成功，延迟5秒')
        sleep(10)
        log.info('点击同意')
        self.driver.find_element_by_id('button1').click()
        sleep(3)
        log.info('手动')
        self.driver.find_element_by_id('account_login').click()
        # sleep(10)
        # log.info('账号')
        # cls.driver.find_element_by_id('account_tex').send_keys('900016')
        # log.info('密码')
        # cls.driver.find_element_by_id('pwd_tex').send_keys('FUTUnn88')
        # log.info('延迟5秒')
        # sleep(3)
        # log.info('关闭app')
        # cls.driver.close_app()
        # log.info('延迟2秒')
        # sleep(3)
        # log.info('启动app')
        # cls.driver.launch_app()
        # log.info('延迟3秒')
        # sleep(3)
        # log.info('后台')
        # cls.driver.background_app(3)
        # sleep(10)
        self.driver.quit()




po = PageObject()
po.do_something()

