#!/usr/bin/python

from time import sleep
from date_time_util import DateTimeUtil

class LCDPrintUtil(object):

  def __init__(self, lcd, mpc, nameShiftEnabled=False):
    self.lcd = lcd
    self.mpc = mpc
    self.dateTimeUtil = DateTimeUtil()
    self.currentStationName = ""
    self.nameShiftEnabled = nameShiftEnabled
    self.shiftRequired = False
    self.shiftIdx = 0

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

    self.lcd.writeMessageToLine(name,2,2)
    dateTime = self.dateTimeUtil.getTime() + " " + self.dateTimeUtil.getDate()
    self.lcd.writeMessageToLine(dateTime,3,2)

  def printNextStation(self):    
    self.lcd.clear()
    self.lcd.writeMessageToLine(">> Next station >>",2,2)
    sleep(0.5)
    self.lcd.writeMessageToLine(self.mpc.getName(),2,2)
    dateTime = self.dateTimeUtil.getTime() + " " + self.dateTimeUtil.getDate()
    self.lcd.writeMessageToLine(dateTime,3,2)

  def printPreviousStation(self):
    self.lcd.clear()
    self.lcd.writeMessageToLine("<< Prev. station <<",2,2)
    sleep(0.5)
    self.lcd.writeMessageToLine(self.mpc.getName(),2,2)
    dateTime = self.dateTimeUtil.getTime() + " " + self.dateTimeUtil.getDate()
    self.lcd.writeMessageToLine(dateTime , 3, 2)

  def printWelcomeScreen(self):
    self.lcd.clear()
    self.lcd.writeMessageToLine("====================",1,2)
    self.lcd.writeMessageToLine("=   Raspberry PI   =",2,2)
    self.lcd.writeMessageToLine("=    Wifi Radio    =",3,2)
    self.lcd.writeMessageToLine("====================",4,2)

  def printErrorMessage(self, error):
    self.lcd.clear()
    self.lcd.writeMessageToLine("An error occured.",2,2)
    self.lcd.writeMessageToLine(error,3,2)