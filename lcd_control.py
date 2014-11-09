#!/usr/bin/python

import threading
import time
from wifi_radio_constants import WifiRadioConstants


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
				if item.id == WifiRadioConstants.MENU_MSG_ID:
					self.handleRotaryMenuEvent(item.msg)
				if item.id == WifiRadioConstants.VOLUME_MSG_ID:
					self.handleRotaryVolumeEvent(item.msg)


		print "Stopped lcd control thread"

	def handleRotaryMenuEvent(self, msg):
		if msg == "clockwise":
			print "menu clockwise"
			self.lcd_util.printNextStation()
		elif msg == "counterclockwise":
			print "menu counterclockwise"
			self.lcd_util.printPreviousStation()
		elif msg == "button":
			print "menu button"
			self.lcd_util.printButtonPress()
		else:
			print "menu undefined"

	def handleRotaryVolumeEvent(self, msg):
		if msg == "clockwise":
			print "volume clockwise"
			self.lcd_util.printVolumeUp()
		elif msg == "counterclockwise":
			print "volume counterclockwise"
			self.lcd_util.printVolumeDown()
		elif msg == "button":
			print "volume button"
			self.lcd_util.printButtonPress()
		else:
			print "volume undefined"




	

