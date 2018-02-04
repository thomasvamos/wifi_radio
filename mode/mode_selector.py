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
    self.modes = dict()
    self.initModes()
    self.mode = self.modes[ModeConstants.MODE_PLAYBACK]
  
  def switchMode(self, mode):
    self.mode = self.modes[str(mode)]

  def initModes(self):
    self.modes[ModeConstants.MODE_PLAYBACK] = PlaybackMode(self.lcd, self.mpc, self.switchMode)
    self.modes[ModeConstants.MODE_MENU] = MenuMode(self.lcd, self.mpc, self.switchMode)
    self.modes[ModeConstants.MODE_STATIONS] = StationsMode(self.lcd, self.mpc, self.switchMode)