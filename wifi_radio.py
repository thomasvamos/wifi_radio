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

class WifiRadio(object):

  # GPIO input pins for the back and forth buttons 
  BUTTON_BACK = 17
  BUTTON_FORWARD = 27

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

    self.mpc = MusicPlayerControl()

    self.lcdPrintUtil = LCDPrintUtil(self.lcd, self.mpc, nameShiftEnabled=True)

    self.lcdPrintUtil.printWelcomeScreen()

    self.mpc.stop()
    self.mpc.clearPlaylist()
    self.mpc.loadPlaylist("playlist.m3u")
    self.mpc.play()
    sleep(1)
    self.lcdPrintUtil.setCurrentStation(self.mpc.getName())
    
    # main loop
    while True:
      btn_input = self.readButtonInputs()
      if(btn_input == 1):
        self.mpc.playNextStation()
        self.lcdPrintUtil.setCurrentStation(self.mpc.getName())
        self.lcdPrintUtil.printNextStation()
      elif(btn_input ==2):
        self.mpc.playPreviousStation()
        self.lcdPrintUtil.setCurrentStation(self.mpc.getName())
        self.lcdPrintUtil.printPreviousStation()
      self.lcdPrintUtil.printCurrentStation()
        
  def gpioInit(self):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #set GPIO 0 as input
    GPIO.setup(self.BUTTON_BACK, GPIO.IN)

    #set GPIO 2 as input
    GPIO.setup(self.BUTTON_FORWARD, GPIO.IN)

  def readButtonInputs(self):  
  
    # Initialize  
    got_prev = False  
    got_next = False  

    # Read switches  
    sw1_prev = not GPIO.input(self.BUTTON_BACK)  
    sw2_next = not GPIO.input(self.BUTTON_FORWARD)  

    # Debounce switches and look for two-button combo  
    while(sw1_prev or sw2_next):  

      if(sw1_prev):  
        got_prev = True  

      if(sw2_next):  
        got_next = True  

      sleep(0.001)
      sw1_prev = not GPIO.input(self.BUTTON_BACK)  
      sw2_next = not GPIO.input(self.BUTTON_FORWARD)  

    if(got_prev and got_next):  
      return 3  
    if(got_next):
      return 2  
    if(got_prev):  
      return 1  
    return 0  

if __name__ == '__main__':
  radio = WifiRadio()