import RPi.GPIO as GPIO
import time
#17 27 22 
# 18 - 6 10 7

waist_pin = 18

def open():
    pin = 18
    try:
        while True:
            duty_cycle = 7
            pin.ChangeDutyCycle(duty_cycle)
    except KeyboardInterrupt:
        pin.stop()
    finally:
        GPIO.cleanup()

def move(pin, angle):
    pin = set_pin(pin)

    try:
        while True:
            duty_cycle = float(input("Enter Duty Cycle (Left = 5 to Rigth 10):"))
            pin.ChangeDutyCycle(duty_cycle)
    except KeyboardInterrupt:
        pin.stop()
    finally:
        GPIO.cleanup()

def set_pin(pin):
    duty_cycle = 7.5
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    pin = GPIO.PWM(pin, 50)
    pin.start(duty_cycle)
    return pin

move(waist_pin)