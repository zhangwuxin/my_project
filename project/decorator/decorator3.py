# -*- coding:UTF-8 -*-
#目标函数带固定参数的装饰器
import time
def decorator(fun):
    def wrapper(name):
        start = time.time()
        fun(name)
        runtime = time.time()-start
        print runtime
    return wrapper

@decorator
def do_something(name):
    for i in xrange(100000):
        pass
    print 'play game '+name

do_something('lol')
