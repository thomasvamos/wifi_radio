#!/usr/bin/python
from time import sleep
from date_time_util import DateTimeUtil
from lcd_thread import LCDThread
import RPi.GPIO as GPIO
from wifi_radio_constants import WifiRadioConstants as WRC
from Queue import Queue


class LCDPrintUtil(object):

  #display sizes
  cols = 20
  rows = 4

  # display messages
  lineFrameMsg =        '===================='
  lineEmptyMsg =        '                    '
  lineNoStationName =   '   Unkown Station   '
  welcomeMsg =          '=====================   Raspberry PI   ==    Wifi Radio    ====================='
  laodingMsg =          '=====================      Loading     ==       ...        ====================='
  volumeUpMsg =         '=====================     Volume       ==        Up        ====================='
  volumeDownMsg =       '=====================     Volume       ==       Down       ====================='
  nextStationMsg =      '=====================   > Next     >   ==   > Station  >   ====================='
  previousStationMsg =  '=====================   < Previous <   ==   < Station  <   ====================='
  errorMsg =            '=====================       Error      ==     Occured      ====================='
  goodbyeMsg =          '=====================     Goodbye      ==       ...        ====================='
  pauseMsg =            '=====================     Paused       ==     Playback     ====================='

  def __init__(self):
    
    self.currentStationName = 'Unkown Station'
    self.currentStationTitle = 'Unkown Title'
    self.displayContent = self.welcomeMsg
    self.shiftIdx = 0
    self.shift = False
    self.dateTimeUtil = DateTimeUtil()
    self.queue = Queue()
    self.lcdThread = LCDThread(self.queue) 
    self.lcdThread.start()

  def printScreen(self, framebuffer):
    self.queue.put(self.displayContent)
    
  def printCurrentStation(self):
    if self.shift:
      name = self.getShiftedText(self.currentStationName)
      title = self.getShiftedText(self.currentStationTitle)
      self.shiftIdx = self.shiftIdx + 1
    else:
      name = self.fitNameToDisplayLine(self.currentStationName)
      name = self.fitNameToDisplayLine(self.currentStationTitle)

    dateTime = " " + self.dateTimeUtil.getTime() + " " + self.dateTimeUtil.getDate() + " "
    self.displayContent = title + name + LCDPrintUtil.lineEmptyMsg + str(dateTime) 
    self.printScreen(self.displayContent)

  def printNextStation(self):
    self.shiftIdx = 0
    self.displayContent = LCDPrintUtil.nextStationMsg
    self.printScreen(self.displayContent)
    
  def printPreviousStation(self):
    self.shiftIdx = 0
    self.displayContent = LCDPrintUtil.previousStationMsg
    self.printScreen(self.displayContent)

    
  def printRaw(self, content):
    self.displayContent = content
    self.printScreen(self.displayContent)

  def printVolumeUp(self):
    self.displayContent = LCDPrintUtil.volumeUpMsg
    self.printScreen(self.displayContent)

  def printVolumeDown(self):   
    self.displayContent = LCDPrintUtil.volumeDownMsg
    self.printScreen(self.displayContent)

  def printVolume(self, volume):
    vol = self.centerNameInLine('Volume: ' + str(volume))
    self.displayContent = LCDPrintUtil.lineFrameMsg + vol + LCDPrintUtil.lineEmptyMsg + LCDPrintUtil.lineFrameMsg
    self.printScreen(self.displayContent)

  def printPause(self):
    self.displayContent = LCDPrintUtil.pauseMsg
    self.printScreen(self.displayContent)

  def printLoadingMsg(self):
    self.displayContent = LCDPrintUtil.laodingMsg
    self.printScreen(self.displayContent)

  def printErrorMessage(self, error):
    self.displayContent = LCDPrintUtil.errorMsg
    self.printScreen(self.displayContent)

  def printMenu(self):
    menu = self.centerNameInLine('!Menu!')
    self.displayContent = LCDPrintUtil.lineFrameMsg + menu + LCDPrintUtil.lineEmptyMsg + LCDPrintUtil.lineFrameMsg
    self.printScreen(self.displayContent)

  def printGoodbye(self):
    if not self.queue.empty():
      with self.queue.mutex:
        self.queue.queue.clear()
    self.displayContent = LCDPrintUtil.goodbyeMsg
    self.printScreen(self.displayContent)

  def setCurrentStation(self, currentSong):
    if "file" in currentSong:
      if len(currentSong['file']) > LCDPrintUtil.cols:
        self.currentStationName = currentSong['file'] + ' ## '
      else:
        self.currentStationName = currentSong['file']

    if "title" in currentSong:
      if len(currentSong['title']) > LCDPrintUtil.cols:
        self.currentStationTitle = currentSong['title'] + ' ## '
      else:
        self.currentStationTitle = currentSong['title']

    if (len(currentSong['file']) > LCDPrintUtil.cols) or \
    (len(currentSong['title']) > LCDPrintUtil.cols):
      self.shift = True
    else:
      self.shift = False

  def getShiftedText(self, text):
      startIdx = self.shiftIdx % len(text)
      endIdx = (self.shiftIdx + LCDPrintUtil.cols) % len(text)
      if startIdx < endIdx:
        return text[startIdx:endIdx]
      else:
        return text[startIdx:len(text)] + text[0:endIdx]

  def fitNameToDisplayLine(self, name):
    if(len(name) <= 0):
      name = LCDPrintUtil.lineNoStationName
    
    elif(len(name) > LCDPrintUtil.cols):
      name = name[:17] + '...'

    else:
      name = self.centerNameInLine(name)
    return name

  def centerNameInLine(self, name):
    if len(name) % 2 == 0:
      noOfSpaces = (LCDPrintUtil.cols - len(name)) / 2
      return " " * noOfSpaces + name + " " * noOfSpaces
    else:
      noOfSpaces = (LCDPrintUtil.cols - len(name)-1) / 2
      return " " * noOfSpaces + name + " " * (noOfSpaces + 1)

  

if __name__ == '__main__':
  try:
    lcd = LCDPrintUtil()
  except KeyboardInterrupt:
    print "exit"