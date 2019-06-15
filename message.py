#import smbus
#from time import sleep
#bus=smbus.SMBus(1)
#while True:
#    bus.write_byte(0x0a,9)
#    sleep(1)
import serial
import time
ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
try:
    ser.write("hello")
    time.sleep(3)
    size = ser.inWaiting()
    print size
    if size != 0:
        print("end")
        response = ser.read(size)
        print response
        ser.flushInput()
    
except KeyboardInterrupt:
    ser.close()
    
    
