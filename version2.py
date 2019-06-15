# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys
import math
import json
import time
from multiprocessing import Pool
order=["s0","s1","s2","s3","s4","s5","s6","s7","s8","s9"]
class cube:
    def __init__(self,pos_x=0,pos_y=0):
        self.x=pos_x
        self.y=pos_y
for a in range(10):
    order[a] = cube()
kernel_5 = np.ones((3,3),np.uint8)#5x5的卷积核
kernel_15 = np.ones((15,15),np.uint8)#15x15的卷积核
kernel_50 = np.ones((3,3),np.uint8)#50x50的卷积核
def sort():
    # 对y排序
    temp_order = cube()
    for a in range(0, 8):
        for b in range(0,8 - a):
            if order[b].y > order[b + 1].y:
                temp_order = order[b]
                order[b] = order[b + 1]
                order[b + 1] = temp_order
    # 对x排序
    for a in range(0, 3):
        for b in range(0, 2):
            for c in range(0, 2 - b):
                if order[a * 3 + c].x > order[a * 3 + c + 1].x:
                    temp_order = order[a * 3 + c]
                    order[a * 3 + c] = order[a * 3 + c + 1]
                    order[a * 3 + c + 1] = temp_order
#处理图片
def colorMatch(cube_rgb):
    cube_hsv = cv2.cvtColor(cube_rgb,cv2.COLOR_BGR2HSV)#颜色转换hsv
    #白色
    lower_white = np.array([0, 0, 150])
    upper_white = np.array([180,30,255])
    white_mask = cv2.inRange(cube_hsv, lower_white, upper_white)
    white_erosion = cv2.erode(white_mask, kernel_15, iterations = 1)
    #红色
    lower_red = np.array([156,43,46])
    upper_red = np.array([180,255,255])
    red_mask0 = cv2.inRange(cube_hsv, lower_red, upper_red)
    #红2  red_2_erosion
    lower_red = np.array([0,43,46])
    upper_red = np.array([3,255,255])
    red_mask1 = cv2.inRange(cube_hsv, lower_red, upper_red)
    red_mask = red_mask0 + red_mask1
    red_erosion = cv2.erode(red_mask, kernel_15, iterations = 1)
    #橙色
    lower_orange = np.array([3,43,46])
    upper_orange = np.array([10,255,255])
    orange_mask = cv2.inRange(cube_hsv, lower_orange, upper_orange)
    orange_erosion = cv2.erode(orange_mask, kernel_15, iterations = 1)
    #黄色
    lower_yellow = np.array([26,43,46])
    upper_yellow = np.array([36,255,255])
    yellow_mask = cv2.inRange(cube_hsv, lower_yellow, upper_yellow)
    yellow_erosion = cv2.erode(yellow_mask, kernel_15, iterations = 1)
    #绿色
    lower_green = np.array([41,40,40])
    upper_green = np.array([90,255,255])
    green_mask = cv2.inRange(cube_hsv, lower_green, upper_green)
    green_erosion = cv2.erode(green_mask, kernel_15, iterations = 1)
    #蓝色
    lower_blue = np.array([95,40,40])
    upper_blue = np.array([140,255,255])
    blue_mask = cv2.inRange(cube_hsv, lower_blue, upper_blue)
    blue_erosion = cv2.erode(blue_mask, kernel_15, iterations = 1)
    #总掩膜
    mask = red_erosion + green_erosion + yellow_erosion + blue_erosion + orange_erosion + white_erosion
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_50)#开运算分割色块
    mask = cv2.erode(mask, kernel_50, iterations = 1)
    res = cv2.bitwise_and(cube_hsv, cube_hsv, mask = mask)
    cv2.imwrite("res.png", res)
    edges = cv2.Canny(mask, 50, 80, apertureSize=5)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    mids=[]
    for j, element in enumerate(contours):
        cv2.drawContours(cube_rgb, element, -1, (0, 0, 255), 2)
        cnt = contours[j]
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        order[j].x=cx
        order[j].y=cy
    sort()
    for num in range(0,9):
        print(order[num].x,order[num].y)
        color=res[order[num].y,order[num].x]
        mids.append(([int(color[0]), int(color[1]), int(color[2])]))
    cv2.imshow("canny",edges)
    s=''
    for rgb in mids:#hsv
        if ((0<=rgb[0]<=180 ) and (0<=rgb[1]<=30 ) and( 150<=rgb[2]<=255)):#white
            s+='D'
            print("W")
        elif ((3<=rgb[0]<=9 )and (43<=rgb[1]<=255 )and (46<=rgb[2] <=255)):#orange
            s += 'B'
            print("O")
        elif ((95<=rgb[0] <=140) and (40<=rgb[1]<=255) and (40<=rgb[2]<=255)):#blue
            s+='L'
            print("B")
        elif( (41<=rgb[0]<=90) and (40<=rgb[1]<=255) and (40<=rgb[2]<=245)):#green
            s+='R'
            print("G")
        elif ((20<=rgb[0]<=36) and (43<=rgb[1]<=255) and(46<=rgb[2]<=255)):#yellow
            s+='U'
            print("Y")
        elif (((156<=rgb[0]<=180)or (0<=rgb[0]<=3))and (43<=rgb[1] <=255 )and (46<=rgb[2]<=255 )):#red
            s+='F'
            print("R")
    return s
def cube_out(cube_rgb):
    str=colorMatch(cube_rgb)
    return str