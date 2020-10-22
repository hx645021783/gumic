# coding=utf-8

'''
封装执行系统命令类
可以通过此类的方法获取包名等
'''

import os
import re
import subprocess
from common.handlelogs import log
from common.handlepath import *
from common.readconfig import conf

class AndroidBase(object):
    def __init__(self):
        self.app_path = self.get_app_path()
        self.appium_url = conf.get('android', 'appiumUrl')
        self.platfrom_name = conf.get('android', 'platformName')
        self.package_name = None
        self.activity_name = None
        self.platfrom_version = None
        self.device_name = None
        self.desired_caps = None

    def get_app_path(self):
        app_list = os.listdir(APPDIR)
        if len(app_list) == 0:
            raise Exception('app目录下不存在apk安装包')
        return os.path.join(APPDIR, app_list[0])

    def run_cmd(self, cmd, encoding='gbk'):
        log.info('执行 {}'.format(cmd))
        process_obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
        out, err = process_obj.communicate()
        exit_status = process_obj.returncode
        result = out.decode('gbk', 'ignore') if exit_status == 0 else err.decode('gbk', 'ignore')
        process_obj.terminate()
        if exit_status == 1:
            log.error('执行失败{}'.format(cmd))
            log.error('{}'.format(result))
            raise Exception('cmd命令执行失败')
        else:
            return result

    def install_app(self):
        cmd = 'adb install ' + self.app_path
        try:
            self.run_cmd(cmd)
            log.info('app安装成功')
        except:
            log.info('检测到app已安装，正在尝试卸载重装')
            try:
                log.info('正在尝试卸载已有app')
                if self.package_name is None:
                    self.get_packageName_and_activityName()
                self.uninstall_app()
                log.info('重新安装app')
                self.install_app()
            except:
                log.info('卸载失败')

    def uninstall_app(self):
        if self.package_name:
            cmd = 'adb uninstall ' + self.package_name
            self.run_cmd(cmd)
        else:
            log.error('package_name = None')
            raise Exception('找不到包名')

    def get_packageName_and_activityName(self):
        cmd =  'aapt d badging ' + self.app_path
        result = self.run_cmd(cmd)
        package_name = re.findall("package: name='(.+?)'", result)
        activity_name = re.findall("launchable-activity: name='(.+?)'  label='' icon=''", result)
        if len(package_name) == 0:
            raise Exception('找不到包名')
        elif len(activity_name) == 0:
            raise Exception('找不到活动名')
        else:
            self.package_name = package_name[0]
            self.activity_name = activity_name[0]
            return package_name[0], activity_name[0]

    def get_platformVersion(self):
        cmd = 'adb shell getprop ro.build.version.release'
        self.platfrom_version = self.run_cmd(cmd).strip('\n').strip('\r')
        return self.platfrom_version

    def get_deviceName(self):
        cmd = 'adb devices -l'
        result = self.run_cmd(cmd)
        self.device_name = re.findall("model:(.+?) ", result)[0]
        return self.device_name

    def get_desired_caps(self):
        self.get_packageName_and_activityName()
        self.get_platformVersion()
        self.get_deviceName()
        desired_caps = {
            'platformName': self.platfrom_name,
            'platformVersion': self.platfrom_version,
            'deviceName': self.device_name,
            'appPackage': self.package_name,
            'appActivity': self.activity_name,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.desired_caps = desired_caps
        return desired_caps

android_base = AndroidBase()
# android_base.get_packageName_and_activityName()
# print(android_base.install_app())
# android_base.get_desired_caps()
# print(android_base.get_desired_caps())
# my.install_app()
# my.uninstall_app()
# print(my.get_deviceName())
# print(AndroidBase().get_packageName_and_activityName())