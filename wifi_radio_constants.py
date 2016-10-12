

class WifiRadioConstants(object):

  # GPIO input pins for rotary encoders
  MENU_ROTARY_LEFT_TURN_PIN =17 #GPIO_0 
  MENU_ROTARY_RIGHT_TURN_PIN = 4 #GPIO_7
  MENU_ROTARY_BUTTON_PIN = 2 # SDA

  VOLUME_ROTARY_LEFT_TURN_PIN = 27 #GPIO_2
  VOLUME_ROTARY_RIGHT_TURN_PIN = 22 #GPIO_3
  VOLUME_ROTARY_BUTTON_PIN = 3 #SCL

  # GPIO output pins for the LCD mapping
  LCD_RS = 7
  LCD_E  = 8
  LCD_D4 = 25 
  LCD_D5 = 24
  LCD_D6 = 23
  LCD_D7 = 18
  LED_ON = 15

  # Rotary encoder messages for multihtread communication
  MENU_LEFT_TURN_MSG = 0
  MENU_RIGHT_TURN_MSG = 1

  VOLUME_LEFT_TURN_MSG = 2
  VOLUME_RIGHT_TURN_MSG = 3
  TICK = 4
  