#!/usr/bin/env python
# coding=utf-8

# 剪切一块区域 放到其他位置


import cv2
import numpy


def setPixelRed(i,j,img):
    img.itemset((i,j,0),0)
    img.itemset((i,j,1),0)
    img.itemset((i,j,2),255)


# 读取图像
oImg = cv2.imread("pic.jpg")

# 取一块矩形区域 ':'是 numpy 索引 代表 100到200之间
square = oImg[100:200, 200:400]
# 覆盖到 目标矩形区域
oImg[300:400, 500:700] = square
# 绘制一个红色边框 宽度1px
# 上边框
for r in range(300,401):
    # 上边框
    setPixelRed(r,500,oImg)
    # 下边框
    setPixelRed(r,700,oImg)


for c in range(500,701):
    # 左边框
    setPixelRed(200,c,oImg)
    # 右边框
    setPixelRed(400,c,oImg)


cv2.imwrite("roi.jpg", oImg)
