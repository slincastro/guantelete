import RPi.GPIO as GPIO
import time

servo_pin = 17
duty_cycle = 7.5
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin, 50)
p.start(duty_cycle)

try:
    while True:
        duty_cycle = float(input("Enter Duty Cycle (Left = 5 to Rigth 10):"))
        p.ChangeDutyCycle(duty_cycle)
except KeyboardInterrupt:
    p.stop()
finally:
    GPIO.cleanup()