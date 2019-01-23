# -*- coding:UTF-8 -*-
#目标函数带不固定参数的装饰器
import time
def decorator(fun):
    def wrapper(*args,**kwargs):
        start = time.time()
        fun(*args,**kwargs)
        runtime = time.time()-start
        print runtime
    return wrapper

@decorator
def do_something(name):
    for i in xrange(100000):
        pass
    print 'play game '+name

@decorator
def do_something2(name,user='zy'):
    for i in xrange(100000):
        pass
    print user,'play game '+name

do_something('lol')
do_something2('dnf')
do_something2('dnf',user='zhang yin')
