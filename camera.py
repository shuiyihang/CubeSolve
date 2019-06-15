# -*- coding: utf-8 -*-
import cv2 as cv
from cube import cube_cut
import execute
#import version2
import kociemba
import motor
import numpy as np
from time import sleep
from picamera import PiCamera
receive = ""
blue_pack=[]
white_pack=[]
green_pack=[]
yellow_pack=[]
red_pack=[]
orange_pack=[]
cube_face = []
def active():
    def get_value():
        try:
            with PiCamera() as camera:
                camera.resolution = (320, 240)
                camera.framerate = 24
                sleep(0.1)
                caget = np.empty((240 * 320 * 3),dtype=np.uint8)
                camera.capture(caget,"bgr")
                
                caget = caget.reshape((240, 320, 3))  # xun huan 6 ci
                #cv.imwrite("new.jpg",caget)
                cube_temp =cube_cut(caget)  # dan ge mian shuju
                camera.close()
                return cube_temp
        except:
            pass             
        #fetch color_value      
    #blue_pack=get_value()#1 blue
    sleep(1)
    motor.serve_use("right",12)#open right_serve
    motor.step_degree("left",1,"positive")
    #white_pack=get_value()#2 white
    sleep(1)
    motor.step_degree("left",1,"positive")
    #green_pack=get_value()#3 green
    sleep(1)
    motor.step_degree("left",1,"positive")
    #yellow_pack=get_value()#4 yellow
    sleep(1)
    motor.step_degree("left",1,"positive")
    motor.serve_use("right",6)#close right_serve  2.5 grep
    motor.serve_use("left",12)#
    motor.step_degree("right",1,"positive")
    #red_pack=get_value()#5 red
    sleep(1)
    motor.step_degree("right",2,"negative")#fan zhuan
    #orange_pack=get_value()#6 orange
    sleep(1)
    motor.step_degree("right",1,"positive")
    motor.serve_use("left",6)#
    #reset all motor
    return " "#str2
    
if __name__ == "__main__":  
    try:
        motor.serve_use("left",8)
        motor.serve_use("right",8) 
        sleep(2)
        motor.serve_use("left",6)
        sleep(2)
        motor.serve_use("right",6)       
        sleep(2)
        output=active()
        
        output=kociemba.solve("BFLUURDUDLFBBRUFRRFBFLFLRDUUBLLDBUUDUFRDLFFDBDDLRBRBLR")
        print(output)
        execute.str_split(output)
    except KeyboardInterrupt:
        motor.cleanup()