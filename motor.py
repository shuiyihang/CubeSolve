import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(29,gpio.OUT)#left_serve
gpio.setup(31,gpio.OUT)#right_serve
gpio.setup(35,gpio.OUT)#left_dir
gpio.setup(36,gpio.OUT)#left_pul
gpio.setup(37,gpio.OUT)#right_dir
gpio.setup(38,gpio.OUT)#right_pul
left=gpio.PWM(29,50)
right=gpio.PWM(31,50)
left.start(0)
right.start(0)
def step_degree(which,degree,dire):
    if which=="left":
        if dire=="positive":#zheng
            gpio.output(35,gpio.HIGH)
        else:
            gpio.output(35,gpio.LOW)
        for i in range(degree*800):
            gpio.output(36,gpio.HIGH)
            time.sleep(0.0001)
            gpio.output(36,gpio.LOW)
            time.sleep(0.0001)
    else:
        if dire=="positive":#zheng
            gpio.output(37,gpio.HIGH)
        else:
            gpio.output(37,gpio.LOW)
        for i in range(degree*800):#800 degree
            gpio.output(38,gpio.HIGH)
            time.sleep(0.0001)
            gpio.output(38,gpio.LOW)
            time.sleep(0.0001)
def serve_use(which,degree):
    if which=="left":
        left.ChangeDutyCycle(degree)
        time.sleep(0.6)
        left.ChangeDutyCycle(0)   
    else:
        right.ChangeDutyCycle(degree)
        time.sleep(0.6)
        right.ChangeDutyCycle(0)
def posi_group(hand,deg):#########hand:left|deg:1,2
    if hand=="left":
        serve_use("right", 12)
    else:
        serve_use("left", 12)
    step_degree(hand,deg, "positive")
    if hand=="left":
        serve_use("right",6)
    else:
        serve_use("left",6)
    if deg!=2:
        serve_use(hand, 12)
        step_degree(hand,deg, "negative")
        serve_use(hand, 6)
def nega_group(hand,deg):#########hand:left|deg:1,2
    if hand=="left":
        serve_use("right", 12)
    else:
        serve_use("left", 12)
    step_degree(hand,deg, "negative")
    if hand=="left":
        serve_use("right",6)
    else:
        serve_use("left",6)
    if deg!=2:
        serve_use(hand, 12)
        step_degree(hand,deg, "positive")
        serve_use(hand, 6)
def posi_unit(hand,deg):#########hand:left|deg:1,2
    step_degree(hand,deg, "positive")
    if deg!=2:
        serve_use(hand, 12)
        step_degree(hand,deg, "negative")
        serve_use(hand,6)
def nega_unit(hand,deg):#########hand:left|deg:1,2
    step_degree(hand,deg, "negative")
    if deg!=2:
        serve_use(hand, 12)
        step_degree(hand,deg, "positive")
        serve_use(hand, 6)
#if __name__=="__main__":
#    serve_use("left", 12)
#    serve_use("right",12)
    
    