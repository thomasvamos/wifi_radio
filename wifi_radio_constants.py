

class WifiRadioConstants(object):

  # GPIO input pins for the menu rotary encoder 
  MENU_ROTARY_PIN_A = 17 #GPIO0
  MENU_ROTARY_PIN_B = 27 #GPIO2
  MENU_ROTARY_PIN_BTN = 4 #GPIO7

  # GPIO input pins for the volume rotary encoder 
  VOLUME_ROTARY_PIN_A = 11 #SCLK
  VOLUME_ROTARY_PIN_B = 9 #MISO
  VOLUME_ROTARY_PIN_BTN = 10 #MOSI

  # GPIO output pins for the LCD mapping
  LCD_RS = 7
  LCD_E  = 8
  LCD_D4 = 25 
  LCD_D5 = 24
  LCD_D6 = 23
  LCD_D7 = 18
  LED_ON = 15

  MENU_MSG_ID = "menu_rotary"
  VOLUME_MSG_ID = "volume_rotary"