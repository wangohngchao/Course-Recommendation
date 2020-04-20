import cv2
import numpy as np
r, h, c, w = 0, 150, 0, 150# 设置初始化的跟踪窗口参数
track_window = (c, r, w, h)
cap = cv2.VideoCapture(0)
frame = cv2.imread('F:/Machinevision/test/2.jpg')
# 将rgb转换成hsv
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# 将低于和高于阈值的值设为0，取值hsv值在(0,60,32)到(180,255,255)之间的部分，去除背景
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
# 计算图像的彩色直方图
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
# 归一化
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
# 设置迭代的终止标准，最多十次迭代
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
while (1):
    ret, frame = cap.read()
    if ret == True:
        # 计算每一帧的hsv图像
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 计算反向投影
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # 调用meanShift算法在dst中寻找目标窗口，找到后返回目标窗口
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        x, y, w, h = track_window
        img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
        cv2.imshow('img2', img2)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
