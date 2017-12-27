#!/usr/bin/python

from wifi_radio_constants import WifiRadioConstants as WRC
import threading
import time
import sys
from wifi_radio_constants import WifiRadioConstants
from mpc import MusicPlayerController
from lcd import CharLCD
from lcd_print_util import LCDPrintUtil
import os
from time import sleep

class RadioController(threading.Thread):

  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.daemon = True
    self.running = True
    self.queue = queue
    self.currentStationName = ""

    # init music player controller
    self.mpc = MusicPlayerController()

    # init lcd display
    self.lcdPrintUtil = LCDPrintUtil()
    self.lcdPrintUtil.start()

  def run(self):
    self.running = True
    while self.running:
      try:
        if not self.queue.empty():
          item = self.queue.get()
          print "Handling incoming message " + str(item)
          self.handleMsg(item)

        if not self.currentStationName:
          self.currentStationName = self.mpc.getName()
          self.lcdPrintUtil.setCurrentStation(self.currentStationName)
      except:
        print "Unexpected error: ", sys.exc_info()[0]

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
    elif item == WRC.VOLUME_PRESSED_MSG:
      self.handleVolumePress()
    elif item == WRC.SHUTDOWN_MSG:
      self.handleShutdown()
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
    self.mpc.decreaseVolume()
    vol = self.mpc.getVolume()
    self.lcdPrintUtil.printVolume(vol)

  def handleVolumeRightTurn(self):
    self.mpc.increaseVolume()
    vol = self.mpc.getVolume()
    self.lcdPrintUtil.printVolume(vol)

  def handleVolumePress(self):
    print "handlevolumepress"
    self.lcdPrintUtil.printPause()
    self.mpc.pause()

  def handleShutdown(self):
    self.lcdPrintUtil.printGoodbye()
    sleep(1)
    self.mpc.stop()
    os.system("sudo shutdown -h now")




  

