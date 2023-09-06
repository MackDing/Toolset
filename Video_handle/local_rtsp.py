#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Author: Mack
# @Time: 2022/12/11 19:28 
# @File: local_rtsp.py
# @Software: PyCharm


import cv2
from matplotlib import pyplot as plt

# 通过cv2中的类获取视频流操作对象cap
cap = cv2.VideoCapture('rtsp://admin:123456@192.168.43.50:554/ch1/main/av_stream')
# 调用cv2方法获取cap的视频帧（帧：每秒多少张图片）
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
# 获取cap视频流的每帧大小
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)

# 定义编码格式mpge-4
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
# 定义视频文件输入对象
outVideo = cv2.VideoWriter('1211_saveDir.MP4', fourcc, fps, size)

# 获取视频流打开状态
if cap.isOpened():
    rval, frame = cap.read()
    print('ture')
else:
    rval = False
    print('False')

tot = 1
c = 1
# 循环使用cv2的read()方法读取视频帧
while rval:
    rval, frame = cap.read()
    cv2.imshow('test', frame)
    # 每间隔20帧保存一张图像帧
    # if tot % 20 ==0 :
    #     cv2.imwrite('cut/'+'cut_'+str(c)+'.jpg',frame)
    #     c+=1
    tot += 1
    print('tot=', tot)
    # 使用VideoWriter类中的write(frame)方法，将图像帧写入视频文件
    outVideo.write(frame)
    cv2.waitKey(1)
cap.release()
outVideo.release()
cv2.destroyAllWindows()

