# -*- coding:UTF-8 -*-
#不是装饰器的装饰器
import time
def decorator(fun):
    start = time.time()
    fun()
    runtime = time.time()-start
    print runtime

def do_something():
    for i in xrange(100000):
        pass
    print 'play game'

decorator(do_something)
