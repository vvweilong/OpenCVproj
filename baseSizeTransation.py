#!/usr/bin/env python
# coding=utf-8
import cv2

# 读取原图
oImg = cv2.imread("pic.jpg")

# 存储容量
print oImg.size
# 维度尺寸  宽 高 像素点
print oImg.shape
# 获取原图片尺寸
width = oImg.shape[0]
heigh = oImg.shape[1]
rgb = oImg.shape[2]
print width, heigh

# 变换尺寸  Size 格式为 (h,w)
# float 转 int 类型转换
w = int(width * 0.1 + 0.5)
h = int(heigh * 0.1 + 0.5)

sizedImg = cv2.resize(oImg, (h, w))

cv2.namedWindow("window")
cv2.imshow("img", sizedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

