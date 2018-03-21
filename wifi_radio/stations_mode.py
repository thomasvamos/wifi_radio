'''
Mode to select a radio station
'''

from abstract_mode import AbstractMode
from mode_constants import ModeConstants
from lcd_menu_util import LcdMenuUtil

class StationsMode(AbstractMode):

  def __init__(self, lcd, mpc, funcSwitchMode):
    super(StationsMode,self).__init__(lcd, mpc, funcSwitchMode)
    self.stations = self.mpc.getSongsInCurrentPlaylist()
    self.lcdMenuUtil = LcdMenuUtil(lcd.cols, lcd.rows, self.stations)


  def tick(self):
    menu = self.lcdMenuUtil.getMenuAsString()
    self.lcd.printRaw(menu)

  def handleMenuLeftTurn(self):
    self.lcdMenuUtil.up()
  
  def handleMenuRightTurn(self):
    self.lcdMenuUtil.down()
  
  def handleMenuPress(self):
    idx = self.lcdMenuUtil.getSelectedIndex()
    self.mpc.play(int(self.stations[idx]['pos']))
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