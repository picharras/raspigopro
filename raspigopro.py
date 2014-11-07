#!/usr/bin/env python

import RPi.GPIO as GPIO
import picamera
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(31, GPIO.IN, pull_up_down = GPIO.PUD_UP)
camera = picamera.PiCamera()
camera.led = False
is_recording = False
index_video = 1

#def shutdown_pi(channel):
#  if is_recording:
#    camera.stop_recording()
#  os.system("sudo shutdown -h now")
#  print "APAGANDO..."

#GPIO.add_event_detect(31, GPIO.FALLING, callback = shutdown_pi, bouncetime = 2000)

def recording():
  global index_video
  current_path = os.path.dirname(__file__) +'/videos/'
  name = current_path + time.strftime("%Y-%m-%d") + '.h264'
  while os.path.isfile(name):
    name = current_path + time.strftime("%Y-%m-%d_") + str(index_video) + '.h264'
    index_video += 1
  camera.start_recording(name)
  camera.led = True

def stop_recording():
  camera.stop_recording()
  camera.led = False

print "Estamos listos :)"
try:
  while True:
    if(GPIO.input(17) == 1 and is_recording == False):
      print "Grabando"
      is_recording = True
      recording()
      time.sleep(1)
    elif(GPIO.input(17) == 1 and is_recording == True):
      print "Dejando de grabar"
      is_recording = False
      stop_recording()
      time.sleep(1)
  
except KeyboardInterrupt:
  print "Programa finalizado por usuario"


finally:
  camera.close()
  GPIO.cleanup()
