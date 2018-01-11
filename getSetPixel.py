#!/usr/bin/env python
# coding=utf-8

import cv2
import numpy as np

# 读取图像
oImg = cv2.imread("pic.jpg")


# 方法一：
# # 为了看效果 采用 for 修改了一条线
# for i in range(100, 200,1):
#     # 获取某个像素点
#     for j in  range(100,200,1):
#         # 这里进行的是值拷贝 修改 px 对象 对 oimg 没有影响……
#         px = oImg[i, j]
#         # 修改该像素的 rgb 值       [B,G,R]
#         oImg[i,j] = [255,0 , 0]


# 方法二：
# 使用 item
# 0 - B 1-G 2-R
print oImg.item(10, 10, 0)
# 使用循环 修改一个矩形
for i in range(100, 200, 1):
    # 获取某个像素点
    for j in range(100, 200, 1):
        # 修改该像素的 rgb 值       [B,G,R]
        oImg.itemset(( i, j, 0), 255)
        oImg.itemset(( i, j, 1), 255)
        oImg.itemset(( i, j, 2), 0)

cv2.imwrite("pixel.jpg", oImg)
