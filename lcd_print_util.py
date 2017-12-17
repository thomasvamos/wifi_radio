#!/usr/bin/python

import threading
from time import sleep
from date_time_util import DateTimeUtil
from threading import Timer

class LCDPrintUtil(threading.Thread):

  timeToReturnToCurrentStation = 10.0
  
  #display sizes
  lineDigits = 20

  # display messages
  lineFrameMsg =        "===================="
  lineEmptyMsg =        "                    "
  lineNoStationName =   "   Unkown Station   "
  welcomeMsg =          "=====================   Raspberry PI   ==    Wifi Radio    ====================="
  laodingMsg =          "=====================      Loading     ==       ...        ====================="
  volumeUpMsg =         "=====================     Volume       ==        Up        ====================="
  volumeDownMsg =       "=====================     Volume       ==       Down       ====================="
  nextStationMsg =      "=====================   > Next     >   ==   > Station  >   ====================="
  previousStationMsg =  "=====================   < Previous <   ==   < Station  <   ====================="
  errorMsg =            "=====================       Error      ==     Occured      ====================="
  goodbyeMsg =          "=====================     Goodbye      ==       ...        ====================="
  pauseMsg =            "=====================     Paused       ==     Playback     ====================="

  def __init__(self, lcd, nameShiftEnabled=False):
    
    threading.Thread.__init__(self)
    self.daemon = True
    self.running = True

    self.lcd = lcd
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
      sleep(0.5)    

  def printScreen(self):
    self.lcd.writeMessage(self.displayContent)

  def setAwaitingScreenReset(self):
    self.awaitingScreenReset = True
    self.screenResetCtr = 10

  def setCurrentStation(self, currentStationName):
    print "Setting current station to: " + currentStationName
    self.currentStationName = " " + currentStationName + " "
    if(len(currentStationName) >= LCDPrintUtil.lineDigits):
      self.shiftRequired = True
    else:
      self.shiftRequired = False

  def getCurrentStationNameWithShift(self, shift):
      startIdx = self.shiftIdx % len(self.currentStationName)
      endIdx = (self.shiftIdx + LCDPrintUtil.lineDigits) % len(self.currentStationName)
      if startIdx < endIdx:
        return self.currentStationName[startIdx:endIdx]
      else:
        return self.currentStationName[startIdx:len(self.currentStationName)] + self.currentStationName[0:endIdx]

  def printCurrentStation(self):
    name = self.fitNameToDisplayLine(self.currentStationName)

    if(self.shiftRequired):
      name = self.getCurrentStationNameWithShift(self.shiftIdx)
      self.shiftIdx +=1
      if self.shiftIdx >= len(self.currentStationName):
        self.shiftIdx = 0

    dateTime = " " + self.dateTimeUtil.getTime() + " " + self.dateTimeUtil.getDate() + " "
    self.displayContent = LCDPrintUtil.lineFrameMsg + name + dateTime + LCDPrintUtil.lineFrameMsg

  def fitNameToDisplayLine(self, name):
    if(len(name) <= 0):
      name = LCDPrintUtil.lineNoStationName
    
    elif(len(name) > LCDPrintUtil.lineDigits):
      name = name[:17] + '...'

    else:
      name = self.centerNameInLine(name)
    return name

  def centerNameInLine(self, name):
    if len(name) % 2 == 0:
      noOfSpaces = (LCDPrintUtil.lineDigits - len(name)) / 2
      return " " * noOfSpaces + name + " " * noOfSpaces
    else:
      noOfSpaces = (LCDPrintUtil.lineDigits - len(name)-1) / 2
      return " " * noOfSpaces + name + " " * (noOfSpaces + 1)

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

  def printPause(self):
    self.displayContent = LCDPrintUtil.pauseMsg
    self.setAwaitingScreenReset()

  def printLoadingMsg(self):
    self.displayContent = LCDPrintUtil.laodingMsg
    self.setAwaitingScreenReset()

  def printErrorMessage(self, error):
    self.displayContent = LCDPrintUtil.errorMsg
    self.setAwaitingScreenReset()

  def printGoodbye(self):
    self.displayContent = LCDPrintUtil.goodbyeMsg
    self.setAwaitingScreenReset()