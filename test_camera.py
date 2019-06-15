# -*- coding: utf-8 -*-
import cv2 as cv
from cube import cube_cut
#import version2
# import serial
# import smbus
# import kociemba
import numpy as np
from time import sleep
from picamera import PiCamera
receive = ""
cube_temp = []
cube_face = []
def preview():
    try:
        with PiCamera() as camera:
            camera.resolution = (320, 240)
            camera.framerate = 24
            caget = np.empty((240 * 320 * 3), dtype=np.uint8)

            camera.capture(caget, "bgr")
            caget = caget.reshape((240, 320, 3))  # xun huan 6 ci
            cube_temp =cube_cut(caget)  # dan ge mian shuju
            cv.imshow("get",caget)
            cv.waitKey(0)
            # cube_face.extend(cube_temp)  #liu ge mian de shuju

            # str1="".join(cube_face)    #list  change to str
            # str2=kociemba.solve(str1)  #get a str,use i2c to send message
            # ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
            # try:
            #   while re=="":
            #       ser.write(str2)
            #       receive=ser.readline()
            #       print(re)
            #       sleep(0.1)
            # sheng xia d jiu shi arduino de gong zuo
            # except KeyboardInterrupt:
            #   ser.close()
    except:
        cv.destroyAllWindows()
        camera.close()
if __name__ == "__main__":
    preview()
