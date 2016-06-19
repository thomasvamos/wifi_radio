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
from lcd import CharLCD
from lcd_print_util import LCDPrintUtil
from mpc import MusicPlayerControl
from wifi_radio_constants import WifiRadioConstants as WRC
from commands.init import Init
import time
from time import sleep
from radio_control import RadioControl
from lcd_control import LCDControl
from Queue import Queue
import signal


class WifiRadio(object):

    def __init__(self):

        self.gpioInit()
        self.lcd = CharLCD( pin_rs = WRC.LCD_RS,
            pin_e  = WRC.LCD_E,
            pin_d4 = WRC.LCD_D4,
            pin_d5 = WRC.LCD_D5,
            pin_d6 = WRC.LCD_D6,
            pin_d7 = WRC.LCD_D7)

         # init music player controller
        self.mpc = MusicPlayerControl()

        self.lcdPrintUtil = LCDPrintUtil(self.lcd, self.mpc, nameShiftEnabled=True)
        self.lcdPrintUtil.start()

        # init lcd controller
        self.lcdMsgQueue = Queue()
        self.lcdControl = LCDControl(self.lcd, self.lcdPrintUtil, self.lcdMsgQueue)
        self.lcdControl.start()

        # set up GPIOs as inputs.
        GPIO.setup(WRC.MENU_ROTARY_LEFT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(WRC.MENU_ROTARY_RIGHT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.setup(WRC.VOLUME_ROTARY_LEFT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(WRC.VOLUME_ROTARY_RIGHT_TURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(WRC.MENU_ROTARY_LEFT_TURN_PIN, GPIO.RISING, callback=self.isr_menu_left)  
        GPIO.add_event_detect(WRC.MENU_ROTARY_RIGHT_TURN_PIN, GPIO.RISING, callback=self.isr_menu_right)  

        GPIO.add_event_detect(WRC.VOLUME_ROTARY_LEFT_TURN_PIN, GPIO.RISING, callback=self.isr_volume_left)  
        GPIO.add_event_detect(WRC.VOLUME_ROTARY_RIGHT_TURN_PIN, GPIO.RISING, callback=self.isr_volume_right)  

        init = Init(self.mpc)
        init.start()

        # pause thread
        while True:
            sleep(0.5)

    def gpioInit(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def isr_volume_left(self, channel):
        print "Volume turn left"
        self.lcdMsgQueue.put(WRC.VOLUME_LEFT_TURN_MSG)

    def isr_volume_right(self, channel):
        print "Volume turn right"
        self.lcdMsgQueue.put(WRC.VOLUME_RIGHT_TURN_MSG)

    def isr_menu_left(self, channel):
        print "Menu turn left"
        self.lcdMsgQueue.put(WRC.MENU_LEFT_TURN_MSG)

    def isr_menu_right(self, channel):
        print "Menu turn right"
        self.lcdMsgQueue.put(WRC.MENU_RIGHT_TURN_MSG)

if __name__ == '__main__':
    radio = WifiRadio()