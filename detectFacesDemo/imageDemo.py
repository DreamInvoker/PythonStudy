# encoding=utf-8


'''
1，引入opencv2模块
2，加载分类器 cv2.CaseadeClassifier：加载用于检测脸的文件
3，加载目标图片：加载要检测的图片
4，多尺度检测人脸：detectMultiScale
5，遍历图片中的脸
6，每个人脸画一个框
7，保存检测后的图片
'''

import cv2

facescascades = cv2.CascadeClassifier(
    r"D:/OpenSource/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml"
)
images = cv2.imread("img/2.jpg")
faces = facescascades.detectMultiScale(images)
print faces
for x, y, w, h in faces:
    cv2.rectangle(images, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imwrite("text.jpg", images)
