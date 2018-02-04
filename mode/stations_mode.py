from abstract_mode import AbstractMode
from mode_constants import ModeConstants

class StationsMode(AbstractMode):

  def __init__(self, lcd, mpc, funcSwitchMode):
    super(StationsMode,self).__init__(lcd, mpc, funcSwitchMode) 

  def getName(self):
    return 'StationsMode'

  def tick(self):
    self.lcd.printMenu()

  def handleMenuLeftTurn(self):
    print "StationsMode: Menu left turn"
    pass
  
  def handleMenuRightTurn(self):
    print "StationsMode: Menu right turn"
    pass
  
  def handleMenuPress(self):
    print "StationsMode: Menu press"
    self.switchMode(ModeConstants.MODE_PLAYBACK)

  def handleVolumeLeftTurn(self):
    print "StationsMode: Volume left turn"
    pass

  def handleVolumeRightTurn(self):
    print "StationsMode: Volume right turn"
    pass

  def handleVolumePress(self):
    print "StationsMode: Volume press"
    pass