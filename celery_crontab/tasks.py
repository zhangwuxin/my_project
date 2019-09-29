# -*- coding: utf-8 -*-
from config import app


@app.task
def crontab_func1(time):
    print 'now time is:',time

@app.task
def crontab_func2():
    print 2

