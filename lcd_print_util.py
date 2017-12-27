#!/usr/bin/python

import threading
from time import sleep
from date_time_util import DateTimeUtil
from threading import Timer
from RPLCD import CharLCD
import RPi.GPIO as GPIO
from wifi_radio_constants import WifiRadioConstants as WRC
from Queue import Queue

class LCDPrintUtil(threading.Thread):

  timeToReturnToCurrentStation = 10.0
  
  #display sizes
  cols = 20
  rows = 4

  # display messages
  lineFrameMsg =        "===================="
  lineEmptyMsg =        "                    "
  lineNoStationName =   "   Unkown Station   "
  welcomeMsg =          ['====================','=   Raspberry PI   =','=    Wifi Radio    =','====================']
  laodingMsg =          ['====================','=      Loading     =','=       ...        =','====================']
  volumeUpMsg =         ['====================','=     Volume       =','=        Up        =','====================']
  volumeDownMsg =       ['====================','=     Volume       =','=       Down       =','====================']
  nextStationMsg =      ['====================','=   > Next     >   =','=   > Station  >   =','====================']
  previousStationMsg =  ['====================','=   < Previous <   =','=   < Station  <   =','====================']
  errorMsg =            ['====================','=       Error      =','=     Occured      =','====================']
  goodbyeMsg =          ['====================','=     Goodbye      =','=       ...        =','====================']
  pauseMsg =            ['====================','=     Paused       =','=     Playback     =','====================']

  def __init__(self, queue):
    
    threading.Thread.__init__(self)
    self.daemon = True
    self.running = True

    self.queue = queue
    self.currentStationName = 'Unkown Station'

    self.displayContent = self.welcomeMsg

    self.lcd = lcd = CharLCD( numbering_mode=GPIO.BCM,
                              cols=LCDPrintUtil.cols,
                              rows=LCDPrintUtil.rows,
                              pin_rs=WRC.LCD_RS,
                              pin_e=WRC.LCD_E,
                              pins_data=[WRC.LCD_D4, WRC.LCD_D5, WRC.LCD_D6, WRC.LCD_D7]
                            )

    self.dateTimeUtil = DateTimeUtil()

  def run(self):
    while self.running:
#      try:
        if not self.queue.empty():
          item = self.queue.get()
          print "Handling incoming message " + str(item)
          self.handleMsg(item)
        else:
          self.printCurrentStation()
        self.printScreen(self.displayContent)
        sleep(0.2)
#      except:
#        print "Unexpected error: ", sys.exc_info()[0]

  def handleMsg(self, item):
    print "Msg Item: " + str(item)
    if item[0] == WRC.MENU_LEFT_TURN_MSG:
      self.currentStationName = item[1]
      self.setCurrentStation(self.currentStationName)
      self.printPreviousStation()
    elif item[0] == WRC.MENU_RIGHT_TURN_MSG:
      self.currentStationName = item[1]
      self.setCurrentStation(self.currentStationName)
      self.printNextStation()
    elif item[0] == WRC.VOLUME_LEFT_TURN_MSG:
      self.printVolume(item[1])
    elif item[0] == WRC.VOLUME_RIGHT_TURN_MSG:
      self.printVolume(item[1])
    elif item[0] == WRC.VOLUME_PRESSED_MSG:
      self.printPause()
    elif item[0] == WRC.SHUTDOWN_MSG:
      self.printGoodbye()
    else:
      print "DEFAULT"
      self.lcdPrintUtil.printCurrentStation()

  def printScreen(self, framebuffer):
    self.lcd.home()
    for row in framebuffer:
      self.lcd.write_string(row.ljust(self.cols)[:self.cols])
      self.lcd.write_string('\r\n')

  def setCurrentStation(self, currentStationName):
    print "Setting current station to: " + currentStationName
    self.currentStationName = " " + currentStationName + " "

  def getCurrentStationNameWithShift(self, shift):
      startIdx = self.shiftIdx % len(self.currentStationName)
      endIdx = (self.shiftIdx + LCDPrintUtil.lineDigits) % len(self.currentStationName)
      if startIdx < endIdx:
        return self.currentStationName[startIdx:endIdx]
      else:
        return self.currentStationName[startIdx:len(self.currentStationName)] + self.currentStationName[0:endIdx]

  def printCurrentStation(self):
    name = self.fitNameToDisplayLine(self.currentStationName)
    dateTime = " " + self.dateTimeUtil.getTime() + " " + self.dateTimeUtil.getDate() + " "
    self.displayContent = [LCDPrintUtil.lineFrameMsg,name,dateTime,LCDPrintUtil.lineFrameMsg]

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

  def printNextStation(self):    
    self.displayContent = LCDPrintUtil.nextStationMsg
    
  def printPreviousStation(self):
    self.displayContent = LCDPrintUtil.previousStationMsg

  def printVolumeUp(self):
    self.displayContent = LCDPrintUtil.volumeUpMsg

  def printVolumeDown(self):   
    self.displayContent = LCDPrintUtil.volumeDownMsg

  def printVolume(self, volume):
    vol = self.centerNameInLine('Volume: ' + str(volume))
    self.displayContent = [LCDPrintUtil.lineFrameMsg,vol,LCDPrintUtil.lineEmptyMsg,LCDPrintUtil.lineFrameMsg]

  def printPause(self):
    self.displayContent = LCDPrintUtil.pauseMsg

  def printLoadingMsg(self):
    self.displayContent = LCDPrintUtil.laodingMsg

  def printErrorMessage(self, error):
    self.displayContent = LCDPrintUtil.errorMsg

  def printGoodbye(self):
    self.displayContent = LCDPrintUtil.goodbyeMsg

if __name__ == '__main__':
  try:
    lcd = LCDPrintUtil()
    lcd.start()
    lcd.join()
  except KeyboardInterrupt:
    print "exit"