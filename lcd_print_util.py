#!/usr/bin/python

import threading
from time import sleep
from date_time_util import DateTimeUtil
from threading import Timer

class LCDPrintUtil(threading.Thread):

  timeToReturnToCurrentStation = 10.0
  
  # display messages
  
  lineFrameMsg =        "===================="
  lineEmptyMsg =        "                    "
  welcomeMsg =          "=====================   Raspberry PI   ==    Wifi Radio    ====================="
  laodingMsg =          "=====================      Loading     ==       ...        ====================="
  volumeUpMsg =         "=====================     Volume       ==        Up        ====================="
  volumeDownMsg =       "=====================     Volume       ==       Down       ====================="
  nextStationMsg =      "=====================   > Next     >   ==   > Station  >   ====================="
  previousStationMsg =  "=====================   < Previous <   ==   > Station  >   ====================="
  errorMsg =            "=====================       Error      ==     Occured      ====================="

  def __init__(self, lcd, mpc, nameShiftEnabled=False):
    
    threading.Thread.__init__(self)
    self.daemon = True
    self.running = True

    self.lcd = lcd
    self.mpc = mpc
    self.dateTimeUtil = DateTimeUtil()
    self.currentStationName = ""
    self.nameShiftEnabled = nameShiftEnabled
    self.shiftRequired = False
    self.shiftIdx = 0
    self.currentStationEnabled = True
    self.displayContent = LCDPrintUtil.welcomeMsg
    self.screenResetCtr = 10
    self.awaitingScreenReset = False
    self.setAwaitingScreenReset()

  def run(self):
    while self.running:
      if self.awaitingScreenReset and self.screenResetCtr > 0:
        self.screenResetCtr -= 1

      if self.awaitingScreenReset and self.screenResetCtr == 0:
        self.printCurrentStation()
        self.awaitingScreenReset = False

      if not self.awaitingScreenReset:
        self.printCurrentStation()

      self.printScreen()
      sleep(0.1)    

  def printScreen(self):
    self.lcd.writeMessage(self.displayContent)

  def setAwaitingScreenReset(self):
    self.awaitingScreenReset = True
    self.screenResetCtr = 10

  def setCurrentStation(self, currentStationName):
    self.currentStationName = currentStationName
    if(len(currentStationName) >= 20):
      self.shiftRequired = True
    else:
      self.shiftRequired = False

  def getCurrentStationNameWithShift(self, shift):
      startIdx = self.shiftIdx % len(self.currentStationName)
      endIdx = (self.shiftIdx + 20) % len(self.currentStationName)
      if startIdx < endIdx:
        return self.currentStationName[startIdx:endIdx]
      else:
        return self.currentStationName[startIdx:len(self.currentStationName)] + self.currentStationName[0:endIdx]

  def printCurrentStation(self):
    name = self.currentStationName

    if(self.shiftRequired):
      name = self.getCurrentStationNameWithShift(self.shiftIdx)
      self.shiftIdx +=1
      if self.shiftIdx >= len(self.currentStationName):
        self.shiftIdx = 0

    if(len(name) > 20):
      name = name[:17] + '...'

    if(len(name) == 0):
      name = LCDPrintUtil.lineEmptyMsg

    dateTime = " " + self.dateTimeUtil.getTime() + " " + self.dateTimeUtil.getDate() + " "
    self.displayContent = LCDPrintUtil.lineFrameMsg + name + dateTime + LCDPrintUtil.lineFrameMsg

  def printNextStation(self):    
    self.displayContent = LCDPrintUtil.nextStationMsg
    self.setAwaitingScreenReset()
    

  def printPreviousStation(self):
    self.displayContent = LCDPrintUtil.previousStationMsg
    self.setAwaitingScreenReset()

  def printVolumeUp(self):
    self.displayContent = LCDPrintUtil.volumeUpMsg
    self.setAwaitingScreenReset()

  def printVolumeDown(self):   
    self.displayContent = LCDPrintUtil.volumeDownMsg
    self.setAwaitingScreenReset()

  def printLoadingMsg(self):
    self.displayContent = LCDPrintUtil.laodingMsg
    self.setAwaitingScreenReset()

  def printErrorMessage(self, error):
    self.displayContent = LCDPrintUtil.errorMsg
    self.setAwaitingScreenReset()