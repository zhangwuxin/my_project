from collections import deque

def sayhello(n):
    while n>0:
        print('hello~',n)
        yield n
        n-=1
    print('say hello')

def sayhi(n):
    x=0
    while x<n:
        print('hi~',x)
        yield
        x+=1
    print('say hi')

class TaskScheduler(object):
    def __init__(self):
        self._task_queue = deque()
    def new_task(self,task):
        '''
        向任务队列添加新任务
        :param task:
        :return:
        '''
        self._task_queue.append(task)
    def run(self):
        '''
        不断运行，直到队列中没有任务
        :return:
        '''
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                #生成器结束
                pass
if __name__ == "__main__":
    sched = TaskScheduler()
    sched.new_task(sayhello(10))
    sched.new_task(sayhi(15))
    sched.run()