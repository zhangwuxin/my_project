# -*- coding: utf-8 -*-
from celery.schedules import crontab
from tasks import *
import time

# 设置定时任务
app.conf.beat_schedule = {
    # 设置定时任务的参数,key可以自定义,见名知义,value为定时任务的相关参数的字典
    'contab_func1-every-1-minute': {
        # 指定要执行的任务函数
        'task': 'tasks.crontab_func1',
        # 设置定时启动的频率,没分钟执行一次任务函数
        'schedule': crontab(minute='*/1'),
        # 传入任务函数的参数,可以是一个列表或元组,如果函数没参数则为空列表或空元组
        'args': [time.time()]
    },
    # 'contab_func2-every-day': {
    #     'task': 'tasks.crontab_func2',
    #     # 每周一至周五早上8点执行任务函数
    #     'schedule': crontab(minute=0, hour=8, day_of_week=[1, 2, 3, 4, 5]),
    #     'args': []
    # },
}


# 实现定时任务的另一种方式
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # sender.add_periodic_task(间隔时间秒, 任务名.s(参数), name='自定义任务名')
#     sender.add_periodic_task(10.0, crontab_func1.s(), name='crontab_func1 every 10')
#     sender.add_periodic_task(
#         # 每分钟执行一次
#         crontab(minute='*/1'),
#         # .s()内传入任务函数需要的参数
#         crontab_func2.s()
#     )
