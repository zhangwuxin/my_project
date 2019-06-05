#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Date: 19-6-4 上午9:45
# Author:张印
# Desc：
import os,time


def run():
    num = 0
    pid = os.fork()
    if pid == 0:
        num +=1
        print 1,num,id(num)
    else:
        time.sleep(1)
        num+=1
        print 2,num,id(num)
# run()

from multiprocessing import Process
def run_proc(name):
    print '子进程运行中,name={},pid={}'.format(name,os.getpid())

if __name__=='__main__':
    print '父进程',os.getpid()
    p=Process(target=run_proc,args=('test',))
    print '子进程将要执行'
    p.start()
    p.join()
    print '子进程结束'

