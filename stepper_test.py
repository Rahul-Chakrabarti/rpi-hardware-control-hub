#!/usr/bin/python
# Made by Rahul Chakrabarti 
"""
This file enables functionality for a stepper motor, serving as a test.
Requires: 
- Pin connection via a breadboard
- GPIO and Python language
- A stepper motor
- A raspberry pi microcomputer
- A laptop/pc with PuTTY

"""
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
stepper_pins=[5,6,20,21]

GPIO.setup(stepper_pins,GPIO.OUT)

stepper_sequence=[]
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.LOW,GPIO.HIGH])


try:
	while True:
#		for row in reversed (stepper_sequence):
		for row in stepper_sequence:
			GPIO.output(stepper_pins,row)
			time.sleep(0.01)

except KeyboardInterrupt:
	pass

GPIO.cleanup()

