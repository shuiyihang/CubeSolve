# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys
import math
import json
import time
from multiprocessing import Pool
num=0
kernel_5 = np.ones((3,3),np.uint8)#5x5的卷积核
kernel_15 = np.ones((13,13),np.uint8)#15x15的卷积核
kernel_50 = np.ones((5,5),np.uint8)#50x50的卷积核
#处理图片
def colorMatch(cube_rgb):
    global num
    #cv2.imwrite("res.png",cube_rgb)
    cube_hsv = cv2.cvtColor(cube_rgb,cv2.COLOR_BGR2HSV)#颜色转换hsv
    #白色
    lower_white = np.array([0, 0, 150])
    upper_white = np.array([180,40,255])
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
    upper_orange = np.array([15,255,255])
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
    lower_blue = np.array([92,40,40])
    upper_blue = np.array([140,255,255])
    blue_mask = cv2.inRange(cube_hsv, lower_blue, upper_blue)
    blue_erosion = cv2.erode(blue_mask, kernel_15, iterations = 1)
    #总掩膜
    mask = red_erosion + green_erosion + yellow_erosion + blue_erosion + orange_erosion + white_erosion
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_50)#开运算分割色块
    mask = cv2.erode(mask, kernel_50, iterations = 1)
    res = cv2.bitwise_and(cube_hsv, cube_hsv, mask = mask)

    edges = cv2.Canny(mask, 50, 80, apertureSize=5)
    
    points = cv2.findNonZero(edges)
    min = np.amin(points, axis=0)#每一列
    max = np.amax(points, axis=0)

    x_max = max[0][0]
    y_max = max[0][1]
    x_min = min[0][0]
    y_min = min[0][1]
    height=width = int(x_max - x_min)

    def midpoint(x1,y1,x2,y2):
        global num
        x_mid = int((x1 + x2)/2)
        y_mid = int(((y1 + y2)/2))
        color = res[y_mid, x_mid]
        if num==3:
            while((color[0]==0 and color[1]==0 and color[2]==0)):
                x_mid+=1
                color=res[y_mid,x_mid]
        elif num==7:
            while((color[0]==0 and color[1]==0 and color[2]==0)):
                y_mid-=1
                color=res[y_mid,x_mid]
        num+=1
        return ([int(color[0]), int(color[1]), int(color[2])])
    mid_1 = midpoint(x_min, y_min, (x_min + int(width/3)), (y_min+int(height/3)))
    mid_2 = midpoint((x_min + int(width/3)), y_min, (x_min + int(width*2/3)), (y_min+int(height/3)))
    mid_3 = midpoint((x_min + int(width*2/3)), y_min, x_max, (y_min+int(height/3)))
    mid_4 = midpoint(x_min, (y_min+int(height/3)), (x_min + int(width/3)), (y_min+int(height*2/3)))
    mid_5 = midpoint((x_min + int(width/3)), (y_min +int(height/3)), (x_min + int(width*2/3)), (y_min + int(height*2/3)))
    mid_6 = midpoint((x_min + int(width*2/3)), (y_min +int(height/3)), x_max, (y_min+int(height*2/3)))
    mid_7 = midpoint(x_min, (y_min+int(height*2/3)), (x_min + int(width/3)), y_max)
    mid_8 = midpoint(x_min + int(width/3), (y_min+int(height*2/3)), (x_min + int(width*2/3)), y_max)
    mid_9 = midpoint(x_min + int(width*2/3), (y_min+int(height*2/3)), x_max, y_max)
    mids = [mid_1, mid_2, mid_3, mid_4, mid_5, mid_6, mid_7, mid_8, mid_9]
    s=''
    for rgb in mids:#hsv
        if ((0<=rgb[0]<=180 ) and (0<=rgb[1]<=30 ) and( 150<=rgb[2]<=255)):#white
            s+='U'
            print("W")
        elif ((3<=rgb[0]<=15)and (43<=rgb[1]<=255 )and (46<=rgb[2] <=255)):#orange
            s+='R'
            print("O")
        elif ((92<=rgb[0] <=140) and (40<=rgb[1]<=255) and (40<=rgb[2]<=255)):#blue
            s+='F'
            print("B")
        elif( (41<=rgb[0]<=90) and (140<=rgb[1]<=255) and (120<=rgb[2]<=245)):#green
            s+='B'
            print("G")
        elif ((20<=rgb[0]<=36) and (43<=rgb[1]<=255) and(46<=rgb[2]<=255)):#yellow
            s+='D'
            print("Y")
        elif (((156<=rgb[0]<=180)or (0<=rgb[0]<=3))and (43<=rgb[1] <=255 )and (46<=rgb[2]<=255 )):#red
            s+='L'
            print("R")
    num=0
    return s
    
def cube_cut(cube_rgb):
    str=colorMatch(cube_rgb)
    return str
    
    #time_start=time.time()
    #colorMatch("cube1.png")
    #time_end=time.time()
    #print (time_end-time_start)
    #cv2.waitKey(0)
