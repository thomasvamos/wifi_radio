#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from queue_message import Message

class RotaryEncoder(object):

	CCW = "counterclockwise"
	CW = "clockwise"
	BTN = "button"

	def __init__(self, pin_a, pin_b, pin_button, queue, msg_id):
		self.PIN_A = pin_a
		self.PIN_B = pin_b
		self.PIN_BUTTON = pin_button
		self.queue = queue
		self.msg_id = msg_id
		self.prev_seq = 0
	
		# set pins as input with pull up resistor
		GPIO.setup(self.PIN_A, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(self.PIN_B, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(self.PIN_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)

		# setup interrupt listeners for rotary pins and button pin
		GPIO.add_event_detect(self.PIN_A, GPIO.FALLING, callback = self.rotary_isr)
		GPIO.add_event_detect(self.PIN_B, GPIO.FALLING, callback = self.rotary_isr)
		GPIO.add_event_detect(self.PIN_BUTTON, GPIO.FALLING, callback = self.button_isr)

	# ISR
	def rotary_isr(self, channel): 
		if channel != self.PIN_A and channel != self.PIN_B:
			return

		a_state= not GPIO.input(self.PIN_A)
		b_state= not GPIO.input(self.PIN_B)
		seq = (a_state ^ b_state) | b_state << 1
		
		if seq != self.prev_seq:
			if seq == 1 or seq == 3:
				self.prev_seq = seq
			elif seq == 2:
				if self.prev_seq == 1:
					self.prev_seq = 0
					self.queue.put(Message(self.msg_id, RotaryEncoder.CW))
				elif self.prev_seq == 3:
					self.prev_seq = 0
					self.queue.put(Message(self.msg_id, RotaryEncoder.CCW))

	def button_isr(self, channel):

		if channel != self.PIN_BUTTON:
			return

		self.queue.put(Message(self.msg_id, RotaryEncoder.BTN))




	
