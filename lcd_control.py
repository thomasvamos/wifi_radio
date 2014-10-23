#!/usr/bin/python

import threading
import time


class LCDControl(threading.Thread):

	def __init__(self, lcd, mpc, lcd_util, queue):
		threading.Thread.__init__(self)
		self.daemon = True
		self.lcd = lcd
		self.mpc = mpc
		self.lcd_util = lcd_util
		self.queue = queue
		self.running = True

	def run(self):
		self.running = True
		while self.running:
			if not self.queue.empty():
				item = self.queue.get()
				if item.id == "menu_rotary":
					self.handleRotaryMenuEvent(item.msg)


		print "Stopped lcd control thread"

	def handleRotaryMenuEvent(self, msg):
		if msg == "clockwise":
			print "clockwise"
			self.lcd_util.printNextStation()
		elif msg == "counterclockwise":
			print "counterclockwise"
			self.lcd_util.printPreviousStation()
		elif msg == "button":
			print "button"
		else:
			print "undefined"




	

