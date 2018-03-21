'''
Mode for additional menu items
'''
from abstract_mode import AbstractMode
from mode_constants import ModeConstants

class MenuMode(AbstractMode):

  def __init__(self, lcd, mpc, funcSwitchMode):
    super(MenuMode,self).__init__(lcd, mpc, funcSwitchMode) 

  def getName(self):
    return 'MenuMode'

  def tick(self):
    self.lcd.printMenu()

  def handleMenuLeftTurn(self):
    print "MenuMode: Menu left turn"
    pass
  
  def handleMenuRightTurn(self):
    print "MenuMode: Menu right turn"
    pass
  
  def handleMenuPress(self):
    print "MenuMode: Menu press"
    self.switchMode(ModeConstants.MODE_PLAYBACK)

  def handleVolumeLeftTurn(self):
    print "MenuMode: Volume left turn"
    pass

  def handleVolumeRightTurn(self):
    print "MenuMode: Volume right turn"
    pass

  def handleVolumePress(self):
    print "MenuMode: Volume press"
    pass