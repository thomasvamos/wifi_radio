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
from time import sleep
from lcd import CharLCD
from lcd_print_util import LCDPrintUtil
from mpc import MusicPlayerControl
from Queue import Queue
from rotary_encoder import RotaryEncoder
from lcd_control import LCDControl
from mpc_control import MPCControl
from wifi_radio_constants import WifiRadioConstants as WRC
import threading

class WifiRadio(object):

  def __init__(self):

    self.gpioInit()
    self.lcd = CharLCD( pin_rs = WRC.LCD_RS,
                        pin_e  = WRC.LCD_E,
                        pin_d4 = WRC.LCD_D4,
                        pin_d5 = WRC.LCD_D5,
                        pin_d6 = WRC.LCD_D6,
                        pin_d7 = WRC.LCD_D7)

    self.queue = Queue()
    self.lcdQueue = Queue()
    self.mpcQueue = Queue()
    self.mpc = MusicPlayerControl()
    self.lcdPrintUtil = LCDPrintUtil(self.lcd, self.mpc, nameShiftEnabled=True)
    self.lcdPrintUtil.printWelcomeScreen()
    self.threadLock = threading.Lock()

    # initialize menu rotary switch
    self.menuRotary = RotaryEncoder( WRC.MENU_ROTARY_PIN_A,
                                     WRC.MENU_ROTARY_PIN_B,
                                     WRC.MENU_ROTARY_PIN_BTN,
                                     self.queue,
                                     WRC.MENU_MSG_ID)

    # intialize volume rotary switch
    self.volumeRotary = RotaryEncoder(  WRC.VOLUME_ROTARY_PIN_A,
                                        WRC.VOLUME_ROTARY_PIN_B,
                                        WRC.VOLUME_ROTARY_PIN_BTN,
                                        self.queue,
                                        WRC.VOLUME_MSG_ID)


    self.lcdControl = LCDControl(self.lcd, self.lcdPrintUtil, self.lcdQueue)
    self.lcdControl.start()

    self.mpcControl = MPCControl(self.mpc, self.mpcQueue)
    self.mpcControl.start()

    while True:
      if not self.queue.empty():
        self.threadLock.acquire()
        item = self.queue.get()
        self.lcdQueue.put(item)
        self.mpcQueue.put(item)
        self.threadLock.release()


  def gpioInit(self):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)



if __name__ == '__main__':
  radio = WifiRadio()