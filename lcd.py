#!/usr/bin/python
#
# Raspberry Pi Wifi Radio
# 
# Author : Thomas Pieronczyk
# Site   : http://www.impierium.de
# 
# Date   : 14.09.2014
#
# Based on code from the following resources:
# Matt Hawkins: http://www.raspberrypi-spy.co.uk/2012/07/16x2-lcd-module-control-using-python/
# Adafruit: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_CharLCD/Adafruit_CharLCD.py
#

# LCD Pin functions
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

#import
import RPi.GPIO as GPIO
from time import sleep

class CharLCD(object):

  LCD_WIDTH = 20    # Maximum characters per line
  LCD_CHR = True
  LCD_CMD = False

  LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
  LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
  LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
  LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line 

  # commands
  LCD_CLEARDISPLAY = 0x01

  # Timing constants
  E_PULSE = 0.00005
  E_DELAY = 0.00005

  def __init__(self, pin_rs=7, pin_e=8, pin_d4=25, pin_d5=24, pin_d6=23, pin_d7=18):
    self.pin_rs = pin_rs
    self.pin_e = pin_e
    self.pin_d4 = pin_d4
    self.pin_d5 = pin_d5
    self.pin_d6 = pin_d6
    self.pin_d7 = pin_d7

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pin_rs, GPIO.OUT) # RS
    GPIO.setup(self.pin_e, GPIO.OUT)  # E
    
    GPIO.setup(self.pin_d4, GPIO.OUT) # DB4
    GPIO.setup(self.pin_d5, GPIO.OUT) # DB5
    GPIO.setup(self.pin_d6, GPIO.OUT) # DB6
    GPIO.setup(self.pin_d7, GPIO.OUT) # DB7

    # Initialise display
    self.writeByte(0x33,self.LCD_CMD)
    self.writeByte(0x32,self.LCD_CMD)
    self.writeByte(0x28,self.LCD_CMD) # 4 line 5x7 matrix
    self.writeByte(0x0C,self.LCD_CMD) # turn cursor off 0x0E to enable cursor 
    self.writeByte(0x06,self.LCD_CMD) # shift cursor right
    self.writeByte(0x01,self.LCD_CMD)  


  def clear(self):
    self.writeByte(self.LCD_CLEARDISPLAY)  # command to clear display
    self.delayMicroseconds(3000)  # 3000 microsecond sleep, clearing the display takes a long time

  def delayMicroseconds(self, microseconds):
    seconds = microseconds / float(1000000)  # divide microseconds by 1 million for seconds
    sleep(seconds)

  def writeMessage(self, text, style=1):
    # trim text if it is bigger than the screen
    if(len(text) > 80):
      text = text[:77] + '...'

    for i in range(4):
      self.writeMessageToLine(text[i*20 :i*20+20], i+1, style)

  def writeMessageToLine(self, text, line=1, style=1):
    line_address = self.getLineAddress(line)
    self.writeByte(line_address, self.LCD_CMD)
    self.writeString(text[:20],style)

  def getLineAddress(self, line):
    if line == 2:
      return self.LCD_LINE_2
    elif line == 3:
      return self.LCD_LINE_3
    elif line == 4:
      return self.LCD_LINE_4
    else:
      return self.LCD_LINE_1

  def writeString(self, message, style):
    # Send string to display
    # style=1 Left justified
    # style=2 Centred
    # style=3 Right justified

    if style==1:
      message = message.ljust(self.LCD_WIDTH," ")  
    elif style==2:
      message = message.center(self.LCD_WIDTH," ")
    elif style==3:
      message = message.rjust(self.LCD_WIDTH," ")

    for i in range(self.LCD_WIDTH):
      self.writeByte(ord(message[i]),self.LCD_CHR)

  def writeByte(self, bits, mode=False):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command

    GPIO.output(self.pin_rs, mode) # RS

    # High bits
    GPIO.output(self.pin_d4, False)
    GPIO.output(self.pin_d5, False)
    GPIO.output(self.pin_d6, False)
    GPIO.output(self.pin_d7, False)
    if bits&0x10==0x10:
      GPIO.output(self.pin_d4, True)
    if bits&0x20==0x20:
      GPIO.output(self.pin_d5, True)
    if bits&0x40==0x40:
      GPIO.output(self.pin_d6, True)
    if bits&0x80==0x80:
      GPIO.output(self.pin_d7, True)

    # Toggle 'Enable' pin
    sleep(self.E_DELAY)    
    GPIO.output(self.pin_e, True)  
    sleep(self.E_PULSE)
    GPIO.output(self.pin_e, False)  
    sleep(self.E_DELAY)      

    # Low bits
    GPIO.output(self.pin_d4, False)
    GPIO.output(self.pin_d5, False)
    GPIO.output(self.pin_d6, False)
    GPIO.output(self.pin_d7, False)
    if bits&0x01==0x01:
      GPIO.output(self.pin_d4, True)
    if bits&0x02==0x02:
      GPIO.output(self.pin_d5, True)
    if bits&0x04==0x04:
      GPIO.output(self.pin_d6, True)
    if bits&0x08==0x08:
      GPIO.output(self.pin_d7, True)

    # Toggle 'Enable' pin
    sleep(self.E_DELAY)    
    GPIO.output(self.pin_e, True)  
    sleep(self.E_PULSE)
    GPIO.output(self.pin_e, False)  
    sleep(self.E_DELAY)   

if __name__ == '__main__':
  lcd = CharLCD()
  lcd.writeMessage("This is a short message")  
  sleep(3)  
  lcd.clear()
  sleep(3)  
  lcd.writeMessage("This is a very long message which should spread across the lines eflkjeh fkj ewfjkl weflkhew f khlewfhjklwef jkl")  
  sleep(3)  
  lcd.clear()
  sleep(3)  
  lcd.writeMessageToLine("====================")
  lcd.writeMessageToLine("Textline",2,2)
  lcd.writeMessageToLine("test",3,2)
  lcd.writeMessageToLine("====================",4)


