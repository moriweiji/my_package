#!/usr/bin/env python
#-*- coding:utf-8 -*-
s = u"""
---------------------------------------------------------------
author:simpleness
Date:
python verison:2.7.11
config模块
---------------------------------------------------------------
"""


from ConfigParser import ConfigParser


class Config_opt(object):
    def __init__(self,file):
        self.file = file
        self.con_option = ConfigParser()
        self.con_option.read(self.file)

    def get_sections(self):
        return self.con_option.sections()

    def get_options(self,section):
        return self.con_option.options(section)

    def get_items(self,section):
        return dict(self.con_option.items(section))

    def get_str(self,section,option):
        return self.con_option.get(section,option)

    def get_int(self,section,option):
        return self.con_option.get(section,option)


if __name__ == '__main__':
    print s
    cf = Config_opt('..\\config\\config.ini')
    device_dict =  cf.get_items('devices')
    device = ':'.join((device_dict.get('ip'),device_dict.get('port')))
    print device
    """
    自动获取所有参数
    cf_dict = cf.get_items('config')
    for k, v in cf_dict.items():
        locals()[k] = v
    """
    # cf =ConfigParser()
    # cf.read('..\\config\\config.ini')
    # config_dict = dict(cf.items('devices'))
    # deivce = ':'.join((config_dict['ip'],config_dict['port']))
    # print deivce