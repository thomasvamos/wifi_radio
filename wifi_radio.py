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

class WifiRadio(object):

  # GPIO input pins for the menu rotary encoder 
  MENU_ROTARY_PIN_A = 17
  MENU_ROTARY_PIN_B = 27
  MENU_ROTARY_PIN_BTN = 4

  # GPIO input pins for the volume rotary encoder 
  # VOLUME_ROTARY_PIN_A = 10
  # VOLUME_ROTARY_PIN_B = 9
  # VOLUME_ROTARY_PIN_BTN = 11

  # GPIO output pins for the LCD mapping
  LCD_RS = 7
  LCD_E  = 8
  LCD_D4 = 25 
  LCD_D5 = 24
  LCD_D6 = 23
  LCD_D7 = 18
  LED_ON = 15

  def __init__(self):

    self.gpioInit()
    self.lcd = CharLCD( pin_rs=self.LCD_RS,
                   pin_e=self.LCD_E,
                   pin_d4=self.LCD_D4,
                   pin_d5=self.LCD_D5,
                   pin_d6=self.LCD_D6,
                   pin_d7=self.LCD_D7)

    self.queue = Queue()
    self.mpc = MusicPlayerControl()
    self.lcdPrintUtil = LCDPrintUtil(self.lcd, self.mpc, nameShiftEnabled=True)
    self.lcdPrintUtil.printWelcomeScreen()
    self.menuRotary = RotaryEncoder( self.MENU_ROTARY_PIN_A,
                                     self.MENU_ROTARY_PIN_B,
                                     self.MENU_ROTARY_PIN_BTN,
                                     self.queue,
                                     "menu_rotary")
    self.lcdControl = LCDControl(self.lcd, self.mpc, self.lcdPrintUtil, self.queue)
    self.lcdControl.start()
    
    self.mpc.stop()
    self.mpc.clearPlaylist()
    self.mpc.loadPlaylist("playlist.m3u")
    self.mpc.play()
    sleep(1)
    self.lcdPrintUtil.setCurrentStation(self.mpc.getName())

  def gpioInit(self):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)



if __name__ == '__main__':
  radio = WifiRadio()
  while True:
    sleep(0.1)