from abc import ABCMeta, abstractmethod

class AbstractMode:
    __metaclass__ = ABCMeta

  def __init__(self, lcd, mpc):
    this.lcd = lcd
    this.mpc = mpc

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