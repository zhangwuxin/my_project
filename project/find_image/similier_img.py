#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Date: 19-6-6 下午1:43
# Author:张印
# Desc：
import matplotlib.pyplot as plt
import cv2
import numpy as py

img = cv2.imread("/home/yf/图片/111.jpg")
img1 = cv2.imread("/home/yf/图片/222.jpg")
# 计算图img的直方图
H1 = cv2.calcHist([img], [1], None, [256], [0, 256])
H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)  # 对图片进行归一化处理

# 计算图img2的直方图
H2 = cv2.calcHist([img1], [1], None, [256], [0, 256])
H2 = cv2.normalize(H2, H2, 0, 1, cv2.NORM_MINMAX, -1)
print H1
print 3333333333
print H2
# 利用compareHist（）进行比较相似度
similarity = cv2.compareHist(H1, H2, 0)
print(similarity)

# img和img1直方图展示
plt.subplot(2, 1, 1)
plt.plot(H1)
plt.subplot(2, 1, 2)
plt.plot(H2)
plt.show()