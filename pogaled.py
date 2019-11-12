import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 4
button2 = 17
button3 = 23

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button32, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

try:
    while True:
         button_state = GPIO.input(button)
         if button_state == GPIO.LOW:
             GPIO.output(18,GPIO.HIGH)
             print('pods ir nospiests')
             time.sleep(1)
         else:
             GPIO.output(18,GPIO.LOW)

         button_state = GPIO.input(button2)
         if button_state == GPIO.LOW:
             GPIO.output(27,GPIO.HIGH)
             print('pods v2 ir nospiests')
             time.sleep(1)
         else:
             GPIO.output(27,GPIO.LOW)   

         button_state = GPIO.input(button3)
         if button_state == GPIO.LOW:
             GPIO.output(24,GPIO.HIGH)
             print('pods v2 ir nospiests')
             time.sleep(1)
         else:
             GPIO.output(24,GPIO.LOW)  
except:
    GPIO.cleanup()