from abstract_mode import AbstractMode
from mode_constants import ModeConstants

class PlaybackMode(AbstractMode):

  def __init__(self, lcd, mpc, funcSwitchMode):
    super(PlaybackMode,self).__init__(lcd, mpc,funcSwitchMode)
    self.lcd.setCurrentStation(self.mpc.getCurrentSongInfo())
    self.lcd.printCurrentStation()
    
  def tick(self):
    self.lcd.setCurrentStation(self.mpc.getCurrentSongInfo())
    self.lcd.printCurrentStation()

  def handleMenuLeftTurn(self):
    self.mpc.playPreviousStation()
    name = self.mpc.getCurrentSongInfo()
    self.lcd.setCurrentStation(name)
    self.lcd.printPreviousStation()
    self.lcd.printCurrentStation()
  
  def handleMenuRightTurn(self):
    self.mpc.playNextStation()
    name = self.mpc.getCurrentSongInfo()
    self.lcd.setCurrentStation(name)
    self.lcd.printNextStation()
    self.lcd.printCurrentStation()
  
  def handleVolumeLeftTurn(self):
    self.mpc.decreaseVolume()
    vol = self.mpc.getVolume()
    self.lcd.printVolume(vol)

  def handleVolumeRightTurn(self):
    self.mpc.increaseVolume()
    vol = self.mpc.getVolume()
    self.lcd.printVolume(vol)

  def handleVolumePress(self):
    self.mpc.pause()
    self.lcd.printPause()

  def handleMenuPress(self):
    self.switchMode(ModeConstants.MODE_STATIONS)