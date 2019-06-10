#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:张印
# datetime:2019/6/10 22:53
# software: PyCharm

import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print df

data = [['Alex',10],['Bob',22],['Ajax',22]]
df = pd.DataFrame(data,columns=['name','age'],dtype=float)
print df

data = {'name':['Tom','Jack','Steve','Ricky'],'Age':[23,41,12,41]}
df = pd.DataFrame(data)
print df

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data,index=['rank1','rank2','r3','r4'])
print  df

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print df

