#!/usr/bin/env python

# -*- coding:utf-8 -*-

s = """

---------------------------------------------------------------

author:moriweiji

Date:

python verison:2.7.11

---------------------------------------------------------------

"""

import logging
import os

def log_file(file, mode):
    """

    file: log file path

    mode: wirte log use mode ,you can use  'a' or 'w'

    """
    logging.basicConfig(level=logging.DEBUG,

                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                        datefmt='%a, %d %b %Y %H:%M:%S',

                        filename=file,

                        filemode=mode)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    return logging
  
def read_to_list(file):
    """



    :param file: file is read file path

    :return: list

    """
    with open(file, 'r') as f:
        return [i.strip() for i in f.readlines()]


def write_to_list(file, list, wirte_mode):
    """



    :param file: writed  file path

    :param list: list write to file

    :param wirte_mode: use mode ,you can use  'a' or 'w'

    :return:

    """
    with open(file, wirte_mode) as w:
        for i in list:
            try:
                w.write(i)
            except Exception as e:
                print e


def chock_dir(dir):
    u"""

    检查文件夹是否存在

    :param dir: 文件夹路径

    :return: 打印文件夹

    """
    if not os.path.exists(dir):
        try:
            os.mkdir(dir)
            return 'Create folder --------> %s  [OK]' % dir
        except Exception as e:
            return 'Create folder --------> {} [Fail] reason:{}'.format(dir, e)
    else:
        return 'The folder %s already exists ! [OK]' % dir


def file_size(file):
    """

    :param file: 文件路径

    :return: 文件大小,文件创建时间

    """
    filesize = os.path.getsize(file)
    filectime = os.path.getmtime(file)
    return filesize, filectime
