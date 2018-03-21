#!/usr/bin/env python

'''
LCD Utility class with pre defined LCD message layouts for the station selector menu
'''


from text_shifter import TextShifter

class LcdMenuUtil(object):

  U_ARROW = '>'
  currentTopItem = 0
  currentSelectedItem = 0

  displayContent = ""

  def __init__(self, cols, rows, entries):
    self.cols = cols
    self.rows = rows
    self.textShifter = TextShifter(self.cols)
    self.menu_entries = entries


  def printToConsole(self, content):
    for x in range(0, self.rows):
      print content[x*self.cols:(x+1)*self.cols]


  def getMenuAsString(self):
    content = ""

    for x in range(self.currentTopItem, self.currentTopItem+self.rows):
      content = content + self.getMenuItemString(self.menu_entries[x]['file'], x == self.currentSelectedItem)
    return content


  def up(self):
    self.textShifter.resetShiftIndex()

    if self.currentSelectedItem == 0:
      return
    elif self.currentSelectedItem > self.currentTopItem:
      self.currentSelectedItem -= 1
    else:
      self.currentSelectedItem -= 1
      self.currentTopItem -= 1


  def down(self):
    self.textShifter.resetShiftIndex()

    if self.currentSelectedItem + 1 == len(self.menu_entries):
      return
    elif self.currentSelectedItem < self.currentTopItem + self.rows-1:
      self.currentSelectedItem += 1
    else: 
      self.currentSelectedItem += 1
      self.currentTopItem += 1


  def getSelectedIndex(self):
    return self.currentSelectedItem


  def getMenuItemString(self, item, selected):
    prefix = self.U_ARROW if selected else ' '

    if(len(item) > self.cols):
      if selected:
        item = self.textShifter.shiftText(item)
      item = prefix + item[:19]

    if(len(item) < self.cols):
      item = (prefix + item).ljust(self.cols)

    return item

if __name__ == '__main__':

  menu_entries = [  'FM4',
                    'Antenne Bayern',
                    'Radio 7',
                    'THIS Is a very, very, very Long Menu Item',
                    'LAUT.FM',
                    'Alternative FM',
                    'Ego FM',
                    'SWR 4',
                    'Raegge Sound',
                    'Rock FM',
                    'Antenne Vorarlberg']

  ms = LcdMenuUtil(menu_entries)

  print "CurrentTopItem: " + str(ms.currentTopItem)
  print "CurrentSelectedItem: " + str(ms.currentSelectedItem)
  print '\n'

  menu = ms.getMenuAsString()
  ms.printToConsole(menu)

  while True:
    char = raw_input("Up or down? ")
    if str(char) == 'u':
      ms.up()

      print "CurrentTopItem: " + str(ms.currentTopItem)
      print "CurrentSelectedItem: " + str(ms.currentSelectedItem)
      print '\n'

      menu = ms.getMenuAsString()
      ms.printToConsole(menu)
      print '\n'

    elif str(char) == 'd':
      ms.down()

      print "CurrentTopItem: " + str(ms.currentTopItem)
      print "CurrentSelectedItem: " + str(ms.currentSelectedItem)
      print '\n'

      menu = ms.getMenuAsString()
      ms.printToConsole(menu)
      print '\n'
