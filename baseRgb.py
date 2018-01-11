#!/usr/bin/env python
# coding=utf-8
import cv2
import numpy

oImg = cv2.imread("pic.jpg")

# 对图像进行 RGB 拆分  合并
b, g, r = cv2.split(oImg)

cv2.imwrite("pic_r.jpg", r)
cv2.imwrite("pic_b.jpg", b)
cv2.imwrite("pic_g.jpg", g)

# 这个图像合并 必须是三通道  merge 接受的参数必须是个完整的 rgb 图
mergeImg = cv2.merge((b, g, r))
cv2.imwrite("picmerge.jpg", mergeImg)

# 拆分
