# LED_Blinker.py
import RPi.GPIO as GPIO
import time

# Pin configuration
LED_PIN = 17

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED on
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)   # LED off
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()