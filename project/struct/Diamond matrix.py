#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Date: 19-6-6 下午1:32
# Author:张印
# Desc：菱形矩阵

def create(height):
    height = height
    length = height * 2
    arr = [([00] * length) for i in range(height)]
    i = height
    j = 0
    for i in range(height):
        arr[i][length/2] = i * 2 + 1
    i=0
    j=length/2
    index=0
    while j < length-1:
        while i < height-index-1:
            arr[index+i + 1][j + 1] = arr[i+index][j] + arr[i+index + 1][j]
            i+=1
        index+=1
        j+=1
        i=0

    i=0
    j=0
    while i<height:
        while j<length/2:
            arr[i][j]=arr[height-1-i][length-1-j]
            j+=1
        i+=1
        j=0
    print arr
if __name__=='__main__':
    create(8)