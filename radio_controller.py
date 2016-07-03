#!/usr/bin/python

from wifi_radio_constants import WifiRadioConstants as WRC
import threading
import time
from wifi_radio_constants import WifiRadioConstants
from mpc import MusicPlayerController
from lcd import CharLCD
from lcd_print_util import LCDPrintUtil

class RadioController(threading.Thread):

  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.daemon = True
    self.running = True
    self.queue = queue

    # init LCD Display
    self.lcd = CharLCD( pin_rs = WRC.LCD_RS,
            pin_e  = WRC.LCD_E,
            pin_d4 = WRC.LCD_D4,
            pin_d5 = WRC.LCD_D5,
            pin_d6 = WRC.LCD_D6,
            pin_d7 = WRC.LCD_D7)

    # init music player controller
    self.mpc = MusicPlayerController()

    # init lcd display
    self.lcdPrintUtil = LCDPrintUtil(self.lcd, self.mpc, nameShiftEnabled=True)
    self.lcdPrintUtil.start()

    #print current station name
    name = self.mpc.getName()
    self.lcdPrintUtil.setCurrentStation(name)

    #init = Init(self.mpc)
    #init.start()

  def run(self):
    self.running = True
    while self.running:
      if not self.queue.empty():
        item = self.queue.get()
        print "Handling incoming message" + str(item)
        self.handleMsg(item)

    print "Stopped lcd control thread"

  def handleMsg(self, item):
    print "Msg Item: " + str(item)
    if item == WRC.MENU_LEFT_TURN_MSG:
      self.handleMenuLeftTurn()
    elif item == WRC.MENU_RIGHT_TURN_MSG:
      self.handleMenuRightTurn()
    elif item == WRC.VOLUME_LEFT_TURN_MSG:
      self.handleVolumeLeftTurn()
    elif item == WRC.VOLUME_RIGHT_TURN_MSG:
      self.handleVolumeRightTurn()
    else:
      print "DEFAULT"
      self.lcdPrintUtil.printCurrentStation()

  def handleMenuLeftTurn(self):
    self.lcdPrintUtil.printPreviousStation()
    self.mpc.playPreviousStation()
    name = self.mpc.getName()
    self.lcdPrintUtil.setCurrentStation(name)

  def handleMenuRightTurn(self):
    self.lcdPrintUtil.printNextStation()
    self.mpc.playNextStation()
    name = self.mpc.getName()
    self.lcdPrintUtil.setCurrentStation(name)

  def handleVolumeLeftTurn(self):
    self.lcdPrintUtil.printVolumeDown()
    self.mpc.decreaseVolume()

  def handleVolumeRightTurn(self):
    self.lcdPrintUtil.printVolumeUp()
    self.mpc.increaseVolume()



  

