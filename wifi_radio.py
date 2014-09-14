#!/usr/bin/python
#
# Raspberry Pi Wifi Radio
# 
# Author : Thomas Pieronczyk
# Site   : impierium.de
# 
# Date   : 14.09.2014
#
# Based on code from the following resources:
# Matt Hawkins: http://www.raspberrypi-spy.co.uk/2012/08/20x4-lcd-module-control-using-python/
# http://usualpanic.com/2013/05/raspberry-pi-internet-radio/
#

import RPi.GPIO as GPIO
import time

class WifiRadio(object):

  # GPIO input pins for the back and forth buttons 
  BUTTON_BACK = 17
  BUTTON_FORTH = 27

  # GPIO output pins for the LCD mapping
  LCD_RS = 7
  LCD_E  = 8
  LCD_D4 = 25 
  LCD_D5 = 24
  LCD_D6 = 23
  LCD_D7 = 18
  LED_ON = 15

  def __init__(self):
    lcd = CharLCD()

  def main():

  init()

  # main loop
  while True:
    btn_input = readButtonInputs()
        
  
def init():
  gpio_init()
  lcd_init()

def gpio_init():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)

  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7

  #set GPIO 0 as input
  GPIO.setup(GPIO0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  #set GPIO 2 as input
  GPIO.setup(GPIO2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD)
  lcd_byte(0x32,LCD_CMD)
  lcd_byte(0x28,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD)  
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x01,LCD_CMD)  

def lcd_string(message,style):
  # Send string to display
  # style=1 Left justified
  # style=2 Centred
  # style=3 Right justified

  if style==1:
    message = message.ljust(LCD_WIDTH," ")  
  elif style==2:
    message = message.center(LCD_WIDTH," ")
  elif style==3:
    message = message.rjust(LCD_WIDTH," ")

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY)      

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY)   

def readButtonInputs():  
  
  # Initialize  
  got_prev = False  
  got_next = False  

  # Read switches  
  sw1_prev = not GPIO.input(GPIO0)  
  sw2_next = not GPIO.input(GPIO2)  

  # Debounce switches and look for two-button combo  
  while(sw1_prev or sw2_next):  

    if(sw1_prev):  
      got_prev = True  

    if(sw2_next):  
      got_next = True  

    time.sleep(0.001)
    sw1_prev = not GPIO.input(GPIO0)  
    sw2_next = not GPIO.input(GPIO2)  

  if(got_prev and got_next):  
    print "both buttons pressed"
    return 3  
  if(got_next):
    print "next button pressed"  
    return 2  
  if(got_prev):  
    print "prev button pressed"
    return 1  
  return 0  

if __name__ == '__main__':
  main()