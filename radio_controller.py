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
    self.currentStationName = ""

    # init music player controller
    self.mpc = MusicPlayerController()

    # init queue for multithread communication
    self.msgQueue = Queue()

    # init lcd display
    self.lcdPrintUtil = LCDPrintUtil(self.msgQueue)
    self.lcdPrintUtil.start()

  def handleMenuLeftTurn(self):
    self.mpc.playPreviousStation()
    name = self.mpc.getName()
    self.msgQueue.put([WRC.MENU_LEFT_TURN_MSG,name])

  def handleMenuRightTurn(self):
    self.mpc.playNextStation()
    name = self.mpc.getName()
    self.msgQueue.put([WRC.MENU_RIGHT_TURN_MSG,name])

  def handleVolumeLeftTurn(self):
    self.mpc.decreaseVolume()
    vol = self.mpc.getVolume()
    self.msgQueue.put([WRC.VOLUME_LEFT_TURN_MSG,vol])

  def handleVolumeRightTurn(self):
    self.mpc.increaseVolume()
    vol = self.mpc.getVolume()
    self.msgQueue.put([WRC.VOLUME_RIGHT_TURN_MSG,vol])

  def handleVolumePress(self):
    self.mpc.pause()
    self.msgQueue.put([WRC.VOLUME_PRESSED_MSG])

  def handleShutdown(self):
    self.msgQueue.put([WRC.SHUTDOWN_MSG])
    sleep(1)
    self.mpc.stop()
    os.system("sudo shutdown -h now")




  

