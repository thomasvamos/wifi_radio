#!/usr/bin/python
#
# Raspberry Pi Wifi Radio
# 
# Author : Thomas Pieronczyk
# Site   : impierium.de
# 
# Date   : 14.09.2014
#
# Based on code from the following resources:
# Matt Hawkins: http://www.raspberrypi-spy.co.uk/2012/08/20x4-lcd-module-control-using-python/
# http://usualpanic.com/2013/05/raspberry-pi-internet-radio/

import RPi.GPIO as GPIO
from wifi_radio_constants import WifiRadioConstants as WRC
from radio_controller import RadioController
import time
from time import sleep
from Queue import Queue
import signal


class WifiRadio(object):

    def __init__(self):

        self.gpioInit()

        # init queue for multithread communication
        self.msgQueue = Queue()

        self.radioController = RadioController(self.msgQueue)
        self.radioController.start()

        # set up GPIOs as inputs.
        GPIO.setup(WRC.MENU_ROTARY_LEFT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(WRC.MENU_ROTARY_RIGHT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.setup(WRC.VOLUME_ROTARY_LEFT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(WRC.VOLUME_ROTARY_RIGHT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(WRC.MENU_ROTARY_LEFT_TURN_PIN, GPIO.RISING, callback=self.isr_menu_left)  
        GPIO.add_event_detect(WRC.MENU_ROTARY_RIGHT_TURN_PIN, GPIO.RISING, callback=self.isr_menu_right)  

        GPIO.add_event_detect(WRC.VOLUME_ROTARY_LEFT_TURN_PIN, GPIO.RISING, callback=self.isr_volume_left)  
        GPIO.add_event_detect(WRC.VOLUME_ROTARY_RIGHT_TURN_PIN, GPIO.RISING, callback=self.isr_volume_right)  

        # pause thread
        while True:
            sleep(0.5)

    def gpioInit(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def isr_volume_left(self, channel):
        print "Volume turn left"
        self.msgQueue.put(WRC.VOLUME_LEFT_TURN_MSG)

    def isr_volume_right(self, channel):
        print "Volume turn right"
        self.msgQueue.put(WRC.VOLUME_RIGHT_TURN_MSG)

    def isr_menu_left(self, channel):
        print "Menu turn left"
        self.msgQueue.put(WRC.MENU_LEFT_TURN_MSG)

    def isr_menu_right(self, channel):
        print "Menu turn right"
        self.msgQueue.put(WRC.MENU_RIGHT_TURN_MSG)

if __name__ == '__main__':
    radio = WifiRadio()