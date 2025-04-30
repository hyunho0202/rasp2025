import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED = 12

Duty_ratio = [0,1,2,3,4,5,6,7,8,9,10,15,20,30,50,70,100,200,400]

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

PWM_led = GPIO.PWM(LED,500)
PWM_led.start(0)

try:
    while 1:
        for val in Duty_ratio :
            PWM_led.ChangeDutyCycle(val)
            time.sleep(0.5)

finally:
    PWM_led.stop()
    GPIO.cleanup()