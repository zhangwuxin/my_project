# -*- coding:UTF-8 -*-
#让装饰器带参数
import time
def decorator(max):
    def _decorator(fun):
        def wrapper(*args,**kwargs):
            start = time.time()
            for i in xrange(max):
                fun(*args,**kwargs)
            runtime = time.time()-start
            print runtime
        return wrapper
    return _decorator
@decorator(2)
def do_something(name):
    for i in xrange(100000):
        pass
    print 'play game '+name
do_something('lol')

