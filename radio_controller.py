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
from Queue import Queue

class RadioController(object):

  def __init__(self):
    

    # init music player controller
    self.mpc = MusicPlayerController()

    # init lcd display
    self.lcdPrintUtil = LCDPrintUtil()
    self.lcdPrintUtil.setCurrentStation(self.mpc.getName())
    self.lcdPrintUtil.printCurrentStation()

  def tick(self):
    self.lcdPrintUtil.printCurrentStation()

  def handleMenuLeftTurn(self):
    self.mpc.playPreviousStation()
    name = self.mpc.getName()
    self.lcdPrintUtil.printPreviousStation()

  def handleMenuRightTurn(self):
    self.mpc.playNextStation()
    name = self.mpc.getName()
    self.lcdPrintUtil.printNextStation()

  def handleVolumeLeftTurn(self):
    self.mpc.decreaseVolume()
    vol = self.mpc.getVolume()
    self.lcdPrintUtil.printVolume(vol)

  def handleVolumeRightTurn(self):
    self.mpc.increaseVolume()
    vol = self.mpc.getVolume()
    self.lcdPrintUtil.printVolume(vol)

  def handleVolumePress(self):
    self.mpc.pause()
    self.lcdPrintUtil.printPause()

  def handleShutdown(self):
    self.lcdPrintUtil.printGoodbye()
    sleep(1)
    self.mpc.stop()
    os.system("sudo shutdown -h now")




  

