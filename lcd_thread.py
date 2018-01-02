import threading
from time import sleep
from wifi_radio_constants import WifiRadioConstants as WRC
from lcd import CharLCD
import Queue

class LCDThread(threading.Thread):

  def __init__(self, queue):

    threading.Thread.__init__(self)
    self.daemon = True
    self.running = True
    self.queue = queue

    self.lcd = CharLCD( pin_rs = WRC.LCD_RS,
            pin_e  = WRC.LCD_E,
            pin_d4 = WRC.LCD_D4,
            pin_d5 = WRC.LCD_D5,
            pin_d6 = WRC.LCD_D6,
            pin_d7 = WRC.LCD_D7)

  def run(self):
    while self.isDaemon():
      if not self.queue.empty():
        content = self.queue.get()
        with self.queue.mutex:
          self.queue.queue.clear()
        self.lcd.writeMessage(content)
      sleep(0.1)


if __name__ == '__main__':
  try:
    queue = Queue.LifoQueue()
    
    lcdthread = LCDThread(queue)
    lcdthread.start()

    queue.put("Hello!")
    sleep(2)
    queue.put("not printed")
    queue.put("New content!")
    input("Press any key to exit...")

  except KeyboardInterrupt:
    print "exit"

