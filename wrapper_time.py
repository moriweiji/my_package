#!/usr/bin/env python
#-*- coding:utf-8 -*-
s = u"""
---------------------------------------------------------------
author:simpleness
Date: 2017/8/7 10:31
python verison:2.7.13
Effect：
need lib：
---------------------------------------------------------------
"""
import time

def timeer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        back = func(*args,**kwargs)
        end_time = time.time()
        print end_time - start_time
        return back
    return wrapper

def exeTime(func):
    """检测函数用时"""
    def newFunc(*args, **args2):
        t0 = time.time()
        print "start:%s, {%s} start" % (time.strftime("%X", time.localtime()), args) #func.__name__
        back = func(*args, **args2)
        print "end:@%s, {%s} end" % (time.strftime("%X", time.localtime()), args)
        print "use:%.3fs taken for {%s}" % (time.time() - t0, args)
        return back
    return newFunc


@timeer
@exeTime
def get_html(n):
    print n
    time.sleep(5)


if __name__ == '__main__':
    print s
    n = 'ssssss'
    get_html(n)