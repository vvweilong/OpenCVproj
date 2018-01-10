#!/usr/bin/env python
# coding=utf-8
import cv2

# 读取
oImg = cv2.imread("pic.jpg")

# 复制

copyImg = oImg.copy()

# 显示
# cv2.namedWindow("copy")
# cv2.imshow("copy",copyImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 保存
cv2.imwrite("copy.jpg", copyImg)
# 设置保存级别 QUALITY  0~100 质量递增

for i in range(0, 101, 20):
    name = 'copy' + str(i) + '.jpg'

    cv2.imwrite(name, copyImg, [cv2.IMWRITE_JPEG_QUALITY, i])
