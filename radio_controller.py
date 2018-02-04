#!/usr/bin/python

from mode.mode_selector import ModeSelector

class RadioController(object):

  def __init__(self):
    self.modeSelector = ModeSelector()

  def tick(self):
    self.modeSelector.mode.tick()

  def handleMenuLeftTurn(self):
    self.modeSelector.mode.handleMenuLeftTurn()

  def handleMenuRightTurn(self):
    self.modeSelector.mode.handleMenuRightTurn()

  def handleMenuPress(self):
    self.modeSelector.mode.handleMenuPress()

  def handleVolumeLeftTurn(self):
    self.modeSelector.mode.handleVolumeLeftTurn()

  def handleVolumeRightTurn(self):
    self.modeSelector.mode.handleVolumeRightTurn()

  def handleVolumePress(self):
    self.modeSelector.mode.handleVolumePress()

  def handleShutdown(self):
    self.modeSelector.mode.handleShutdown()




  

