# Make your robot's antenna flash on and off a number of times. 

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)

#while True: 
for x in range (0,5):
  print("Beep!")
  GPIO.output(17,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(17,GPIO.LOW)
  time.sleep(1)
  
# If you want the LED to flash repeatedly, replace the following line
# for x in range (0,5):
# with the line below
# while True:  
# Press Ctrl + C to quit 
