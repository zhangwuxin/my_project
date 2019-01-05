def consumer():
    r=''
    while True:
        n = yield r
        if not n:
            return
        print ('[CONSUMER]Consuming {}'.format(n))
        r = 'OK'
def produce(c):
    c.send(None)
    n=0
    while n<5:
        n+=1
        print('[PRODUCER]Producing {}'.format(n))
        r=c.send(n)
        print('[PRODUCER]Consumer return : {}'.format(r))
    c.close()
c=consumer()
produce(c)
