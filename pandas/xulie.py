#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:张印
# datetime:2019/6/10 22:39
# software: PyCharm

import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print s

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print s


