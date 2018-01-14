from abstract_mode import AbstractMode

class MenuMode(AbstractMode):

  def __init__(self, lcd, mpc, funcSwitchMode):
    super(MenuMode,self).__init__(lcd, mpc, funcSwitchMode)

  def getName(self):
    return 'MenuMode'

  def tick(self):
    self.lcd.printMenu()

  def handleMenuLeftTurn(self):
    pass
  
  def handleMenuRightTurn(self):
    pass
  
  def handleMenuPress(self):
    pass
    # self.switchMode(PlaybackMode.__name__)

  def handleVolumeLeftTurn(self):
    pass

  def handleVolumeRightTurn(self):
    pass

  def handleVolumePress(self):
    pass