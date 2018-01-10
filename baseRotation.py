#!/usr/bin/env python
# coding=utf-8

import cv2
import numpy as np
import numpy
# 读取图片
oImg = cv2.imread("pic.jpg")

c,r,rgb=oImg.shape

print c/2,r/2
# 这步是获取 旋转矩阵
M=cv2.getRotationMatrix2D((r/2,c/2),180,1)

# 根据变换矩阵重新生成图像
dst = cv2.warpAffine(oImg,M,(r,c))

cv2.imwrite("rotationImg.jpg",dst)
