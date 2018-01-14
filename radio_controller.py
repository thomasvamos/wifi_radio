#!/usr/bin/python

from mpc import MusicPlayerController
from lcd_print_util import LCDPrintUtil
import os
from time import sleep

from mode.playback_mode import PlaybackMode
from mode.menu_mode import MenuMode

class RadioController(object):

  def __init__(self):
    self.lcd = LCDPrintUtil()
    self.mpc = MusicPlayerController()
    self.modes = dict()
    self.initModes()
    self.switchMode(PlaybackMode.__name__)
  
  def switchMode(self, mode):
    self.mode = self.modes[str(mode)]

  def initModes(self):
    playbackMode = PlaybackMode(self.lcd, self.mpc, self.switchMode)
    menuMode = MenuMode(self.lcd, self.mpc, self.switchMode)

    self.modes[str(PlaybackMode.__name__)] = playbackMode
    self.modes[str(MenuMode.__name__)] = menuMode


  def tick(self):
    self.mode.tick()

  def handleMenuLeftTurn(self):
    self.mode.handleMenuLeftTurn()

  def handleMenuRightTurn(self):
    self.mode.handleMenuRightTurn()

  def handleMenuPress(self):
    self.mode.handleMenuPress()

  def handleVolumeLeftTurn(self):
    self.mode.handleVolumeLeftTurn()

  def handleVolumeRightTurn(self):
    self.mode.handleVolumeRightTurn()

  def handleVolumePress(self):
    self.mode.handleVolumePress()

  def handleShutdown(self):
    self.lcd.printGoodbye()
    sleep(1)
    self.mpc.stop()
    os.system("sudo shutdown -h now")




  

