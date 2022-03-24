from flask import Flask, request, render_template
from datetime import datetime
import json
import threading
from queue import Queue
import RPi.GPIO as GPIO
from time import sleep

PORT = 5000
app = Flask(__name__)

task_queue = Queue()
result_queue = Queue()

class GpioControl(threading.Thread):
    def __init__(self, task_queue, result_queue):
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        r = 255
        g = 0
        b = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT) #R(シルク印刷上はG)
        GPIO.setup(16, GPIO.OUT) #G(シルク印刷上はR)
        GPIO.setup(26, GPIO.OUT) #B
        
        try:
            while True:

                while self.task_queue.empty():
                    sleep(0.1)
                    pass
                
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(26, GPIO.LOW)

                data = task_queue.get()
                r = data[0]
                g = data[1]
                b = data[2]

                if(r > 0):
                    GPIO.output(12, GPIO.HIGH)
                if(g > 0):
                    GPIO.output(16, GPIO.HIGH)
                if(b > 0):
                    GPIO.output(26, GPIO.HIGH)

                print("gpioThread.run()")
                sleep(0.5)

        except KeyboardInterrupt:
            # KeyboardInterruptをハンドリングして終了時に必ずGPIO.cleanup()が実行されるようにする
            pass

        GPIO.cleanup()


@app.route('/')  #追加
def index():
    return render_template("index.html")

@app.route('/set_color', methods=["POST"])
def set_color():
    value = 'None'

    if request.method == 'POST':
        data = json.loads(request.data) 
        value = data['color']

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

        task_queue.put(colors[value])
    
    return str(value)

if __name__ == "__main__":
    gpio_control = GpioControl(task_queue, result_queue)


    gpio_thread = threading.Thread(target=gpio_control.run)
    gpio_thread.start()

    app.run(port=PORT, host='0.0.0.0', debug=True)