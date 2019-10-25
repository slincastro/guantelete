import RPi.GPIO as GPIO
import time
#17 27 22 
# 18 - 6 107

waist_pin = 18

def move(pin):
    duty_cycle = 7.5
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    p = GPIO.PWM(pin, 50)
    p.start(duty_cycle)

    try:
        while True:
            duty_cycle = float(input("Enter Duty Cycle (Left = 5 to Rigth 10):"))
            p.ChangeDutyCycle(duty_cycle)
    except KeyboardInterrupt:
        p.stop()
    finally:
        GPIO.cleanup()

move(waist_pin)