from abc import ABCMeta, abstractmethod
from mpc import MusicPlayerController
from lcd_print_util import LCDPrintUtil
import os
from time import sleep

class AbstractMode:
  __metaclass__ = ABCMeta

  def __init__(self, lcd, mpc, funcSwitchMode):
    self.lcd = lcd
    self.mpc = mpc
    self.switchMode = funcSwitchMode

  def switchMode(mode):
    self.switchMode(mode)

  @abstractmethod
  def tick(self):
    pass

  @abstractmethod
  def handleMenuLeftTurn(self):
    pass
  
  @abstractmethod
  def handleMenuRightTurn(self):
    pass
  
  @abstractmethod
  def handleMenuPress(self):
    pass

  @abstractmethod
  def handleVolumeLeftTurn(self):
    pass

  @abstractmethod
  def handleVolumeRightTurn(self):
    pass

  @abstractmethod
  def handleVolumePress(self):
    pass

  def handleShutdown(self):
    self.lcd.printGoodbye()
    sleep(1)
    self.mpc.stop()
    os.system("sudo shutdown -h now")