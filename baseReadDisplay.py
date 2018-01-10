#!/usr/bin/env python
# coding=utf-8

# openCV 基本用法  图片的读取和显示
from cv2 import imread, imshow,namedWindow,waitKey

# 读取
readInImg = imread("pic.jpg")



# 显示
namedWindow("pic")
imshow("pic", readInImg)
waitKey(0)
