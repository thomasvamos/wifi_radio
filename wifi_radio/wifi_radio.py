#!/usr/bin/env python
'''
Raspberry Pi Wifi Radio

Created: 14.09.2014
'''

import RPi.GPIO as GPIO
from wifi_radio_constants import WifiRadioConstants as WRC
from radio_controller import RadioController
import time
from time import sleep
import signal
import serial
import logging
import configuration as cfg

__author__ = "Thomas Vamos"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Thomas Vamos"
__email__ = "mail@thomasvamos.de"

class WifiRadio(object):

    def __init__(self):

        self.initLogger()

        # initialize serial port
        ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

        self.initGpio()

        self.radioController = RadioController()

        self.tickInterval = 10
        self.tickExecCounter = self.tickInterval
        
        # pause thread
        try:
            while 1:
                response = ser.readline().strip()
                if response == "66":
                    self.isr_menu_right(0)
                elif response == "99":
                    self.isr_menu_left(0)
                elif response == "15":
                    self.isr_menu_press(0)

                self.radioController.tick()

        except KeyboardInterrupt:
            GPIO.cleanup()
            ser.close()

    def initLogger(self):
        logging.basicConfig(filename=cfg.log_file,level=logging.DEBUG)

    def initGpio(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # set up GPIOs as inputs.

        # set up press buttons
        GPIO.setup(WRC.VOLUME_ROTARY_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(WRC.VOLUME_ROTARY_BUTTON_PIN, GPIO.RISING, callback=self.isr_volume_press)  

        # set up volume rotary encoder
        GPIO.setup(WRC.VOLUME_ROTARY_LEFT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(WRC.VOLUME_ROTARY_RIGHT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(WRC.VOLUME_ROTARY_LEFT_TURN_PIN, GPIO.RISING, callback=self.isr_volume_left)  
        GPIO.add_event_detect(WRC.VOLUME_ROTARY_RIGHT_TURN_PIN, GPIO.RISING, callback=self.isr_volume_right)  

        GPIO.setup(WRC.SHUTDOWN_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(WRC.SHUTDOWN_INPUT, GPIO.FALLING, callback=self.shutdown)

    def isr_volume_left(self, channel):
        # print "Volume turn left"
        self.radioController.handleVolumeLeftTurn()

    def isr_volume_right(self, channel):
        # print "Volume turn right"
        self.radioController.handleVolumeRightTurn()

    def isr_volume_press(self, channel):
        # print "Volume button pressed"
        self.radioController.handleVolumePress()

    def isr_menu_left(self, channel):
        # print "Menu turn left"
        self.radioController.handleMenuLeftTurn()

    def isr_menu_right(self, channel):
        # print "Menu turn right"
        self.radioController.handleMenuRightTurn()

    def isr_menu_press(self, channel):
        self.radioController.handleMenuPress()

    def shutdown(self, channel):
        # print "Shutdown..."
        self.radioController.handleShutdown()

if __name__ == '__main__':
    WifiRadio()