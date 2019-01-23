# -*- coding:UTF-8 -*-
#最简单的装饰器
import time
def decorator(fun):
    def wrapper():
        start = time.time()
        fun()
        runtime = time.time()-start
        print runtime
    return wrapper

@decorator
def do_something():
    for i in xrange(100000):
        pass
    print 'play game'

do_something()
