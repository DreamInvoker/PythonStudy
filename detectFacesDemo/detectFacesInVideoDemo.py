# encoding=utf-8

'''
    1,导入木块
    2,获取摄像头设备
    3,读取摄像头内容
    4,不断刷新图像
    5,显示在窗口中
'''
import cv2

facescascades = cv2.CascadeClassifier(
    r"haarcascade_eye_tree_eyeglasses.xml"
)

video = cv2.VideoCapture(0)
while True:
    rect, imgs = video.read()  # 摄像机图像数据
    faces = facescascades.detectMultiScale(imgs, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))
    print faces

    for x, y, w, h in faces:
        cv2.rectangle(imgs, (x, y), (x + w, y + h), (0, 0, 255), 2)
    key = cv2.waitKey(1)  # 每1ms刷新一次
    cv2.imshow("Faces", imgs)
    if key == 27:
        cv2.imwrite("face.jpg", imgs)
        video.release()
        cv2.destroyAllWindows()
        break
