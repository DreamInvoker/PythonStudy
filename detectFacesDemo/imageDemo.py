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
    r"D:/OpenSource/opencv/opencv/sources/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml"
)
images = cv2.imread("img/1.jpg")
faces = facescascades.detectMultiScale(images, scaleFactor=1.1, minNeighbors=20,minSize=(10, 10))
print faces
for x, y, w, h in faces:
    cv2.rectangle(images, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv2.imwrite("text.jpg", images)
