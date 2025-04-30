import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 11
SW = 10

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

flag = False

while True:
    if GPIO.input(SW) == GPIO.HIGH:
        GPIO.output(LED, flag)
        flag = not flag
        time.sleep(1)
    