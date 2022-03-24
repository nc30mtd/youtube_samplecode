import RPi.GPIO as GPIO
from time import sleep
import time

def reset_color():
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)

def set_color(r,g,b):
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(26, GPIO.HIGH)
    print(r,g,b)
# hotpink
# ff69b4

colors = [
    # RGB
    (0x00, 0x00, 0x00), 
    (0x00, 0xFF, 0x00), 
    (0xFF, 0x00, 0x00), 
    (0xFF, 0xFF, 0x00),
    (0x00, 0x00, 0xFF), 
    (0x00, 0xFF, 0xFF), 
    (0xFF, 0x00, 0xFF), 
    (0xFF, 0xFF, 0xFF), 
]
if __name__=='__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT) #R(シルク印刷上はG)
    GPIO.setup(16, GPIO.OUT) #G(シルク印刷上はR)
    GPIO.setup(26, GPIO.OUT) #B

    r = 0
    b = 0
    g = 0
    r = 0xff
    g = 0x69
    b = 0xb4
    idx = 5
    r = colors[idx][0]
    g = colors[idx][1]
    b = colors[idx][2]
    reset_color()

    duty = 0.1
    # 10msを1周期とする
    try:
        while True:
            if(r > 0):
                GPIO.output(12, GPIO.HIGH)
            if(g > 0):
                GPIO.output(16, GPIO.HIGH)
            if(b > 0):
                GPIO.output(26, GPIO.HIGH)

            sleep(0.5)

            reset_color()
            sleep(0.5)

        # while True:
        #     # start_time = time.time()
        #     GPIO.output(12, GPIO.HIGH)
        #     GPIO.output(16, GPIO.HIGH)
        #     GPIO.output(26, GPIO.HIGH)

        #     for i in range(0, 255):
        #         if(r == i):
        #             GPIO.output(12, GPIO.LOW)
        #             r = 0
        #         if(g == i):
        #             GPIO.output(16, GPIO.LOW)
        #             g = 0
        #         if(b == i):
        #             GPIO.output(26, GPIO.LOW)
        #             b = 0
        #         #sleep(0.01/255.0)
        #         #sleep(0.0001/256.0)
        #         #print(i, r,g,b)
                
        #     r = 0xff
        #     g = 0x69
        #     b = 0xb4
            
        #     GPIO.output(12, GPIO.LOW)
        #     GPIO.output(16, GPIO.LOW)
        #     GPIO.output(26, GPIO.LOW)
        #     # elapsed_time = time.time() - start_time
        #     # print(elapsed_time)

    except KeyboardInterrupt:
        # KeyboardInterruptをハンドリングして終了時に必ずGPIO.cleanup()が実行されるようにする
        pass

    GPIO.cleanup()
