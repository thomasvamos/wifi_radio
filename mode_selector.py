#!/usr/bin/python

from playback_mode import PlaybackMode
from menu_mode import MenuMode
from stations_mode import StationsMode

from mode_constants import ModeConstants
from mpc import MusicPlayerController
from lcd_print_util import LCDPrintUtil
import os
from time import sleep

class ModeSelector(object):

  def __init__(self):
    self.lcd = LCDPrintUtil()
    self.mpc = MusicPlayerController()
    self.mode = PlaybackMode(self.lcd, self.mpc, self.switchMode)
  
  def switchMode(self, mode):
    if mode == ModeConstants.MODE_STATIONS:
      self.mode =  StationsMode(self.lcd, self.mpc, self.switchMode)
    elif mode == ModeConstants.MODE_MENU:
      self.mode = MenuMode(self.lcd, self.mpc, self.switchMode)
    elif mode == ModeConstants.MODE_PLAYBACK:
      self.mode = PlaybackMode(self.lcd, self.mpc, self.switchMode)
    else:
      print "unkown mode, returning to playback."
      self.mode = PlaybackMode(self.lcd, self.mpc, self.switchMode)