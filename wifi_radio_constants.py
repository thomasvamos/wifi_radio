#!/usr/bin/python

class WifiRadioConstants(object):

  # GPIO input pins for rotary encoders
  VOLUME_ROTARY_LEFT_TURN_PIN = 22 #GPIO_3
  VOLUME_ROTARY_RIGHT_TURN_PIN = 27 #GPIO_2
  VOLUME_ROTARY_BUTTON_PIN = 3 #SCL

  # Input Pin to tell the radio to init shutdown
  SHUTDOWN_INPUT = 10 #MOSI

  # GPIO output pins for the LCD mapping
  LCD_RS = 7
  LCD_E  = 8
  LCD_D4 = 25 
  LCD_D5 = 24
  LCD_D6 = 23
  LCD_D7 = 18
  # LED_ON = 15 # hard wired, always on

  # Rotary encoder messages for multihtread communication
  MENU_LEFT_TURN_MSG = 0
  MENU_RIGHT_TURN_MSG = 1
  MENU_PRESSED_MSG = 2

  VOLUME_LEFT_TURN_MSG = 3
  VOLUME_RIGHT_TURN_MSG = 4
  VOLUME_PRESSED_MSG = 5
  
  TICK = 6
  SHUTDOWN_MSG = 7
  