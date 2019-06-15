import serial
import time
temp="U2 L U' R2 U R B' R L' B2 D' L2 U F2 U2 D R2 F2 U'"
re=""
ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
k=3
try :   
    while re=="":
        ser.write(temp)
        re=ser.readline()      
        print(re)
        time.sleep(0.1)
        
except KeyboardInterrupt:
    ser.close()