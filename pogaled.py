import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 4

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
         button_state = GPIO.input(button)
         if button_state == GPIO.HIGH:
             GPIO.output(18,GPIO.HIGH)
             print('pods ir nospiests')
             time.sleep(1)
         else:
             GPIO.output(18,GPIO.LOW)
except:
    GPIO.cleanup()