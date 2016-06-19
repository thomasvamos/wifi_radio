#!/usr/bin/python

import threading
import time
from time import sleep
from wifi_radio_constants import WifiRadioConstants as WRC
from threading import Timer


class LCDControl(threading.Thread):

	def __init__(self, lcd, lcd_util, queue):
		threading.Thread.__init__(self)
		self.daemon = True
		self.lcd = lcd
		self.lcd_util = lcd_util
		self.queue = queue
		self.running = True

	def run(self):
		while self.running:
			if not self.queue.empty():
				item = self.queue.get()
				print "Handling incoming message" + str(item)
				self.handleMsg(item)

		print "Stopped lcd control thread"

	def handleMsg(self, item):
		print "Msg Item: " + str(item)
		if item == WRC.MENU_LEFT_TURN_MSG:
			print "MENU LEFT TURN"
			self.lcd_util.printPreviousStation()
		elif item == WRC.MENU_RIGHT_TURN_MSG:
			print "MENU RIGHT TURN"
			self.lcd_util.printNextStation()
		elif item == WRC.VOLUME_LEFT_TURN_MSG:
			print "VOLUME LEFT TURN"
			self.lcd_util.printVolumeDown()
		elif item == WRC.VOLUME_RIGHT_TURN_MSG:
			print "VOLUME RIGHT TURN"
			self.lcd_util.printVolumeUp()
		elif item == WRC.TICK:
			print "TICK"
			self.lcd_util.printCurrentStation()
		else:
			print "DEFAULT"
			self.lcd_util.printCurrentStation()


	




	

