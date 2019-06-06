#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Date: 19-6-5 下午2:29
# Author:张印
# Desc：
def bubble_sort(alist):
    for j in range(len(alist)-1,0,-1):
        for i in range(j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

li = [1,55,22,7,909,32,123,76680,-1,32,44]
bubble_sort(li)
print li
