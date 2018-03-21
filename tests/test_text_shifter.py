import unittest

# import the module
from wifi_radio.text_shifter import TextShifter

class TestTextShifter(unittest.TestCase):

  DISPLAY_COLUMNS = 6

  def testSingleShift(self):
    sut = TextShifter(self.DISPLAY_COLUMNS)
    shifted = sut.shiftText('HELLO!')
    self.assertEqual(shifted, 'ELLO!H')

  def testTripleShift(self):
    sut = TextShifter(self.DISPLAY_COLUMNS)
    sut.shiftText('HELLO!')
    sut.shiftText('HELLO!')
    shifted = sut.shiftText('HELLO!')
    self.assertEqual(shifted, 'LO!HEL')

  def testResetShiftIndex(self):
    sut = TextShifter(self.DISPLAY_COLUMNS)
    sut.shiftText('HELLO!')
    sut.shiftText('HELLO!')
    sut.shiftText('HELLO!')
    sut.resetShiftIndex()
    shifted = sut.shiftText('HELLO!')
    self.assertEqual(shifted, 'ELLO!H')

  def testShiftStringLongerThanDisplayColumns(self):
    sut = TextShifter(self.DISPLAY_COLUMNS)
    sut.shiftText('THIS IS A VERY LONG STRING')
    sut.shiftText('THIS IS A VERY LONG STRING')
    shifted = sut.shiftText('THIS IS A VERY LONG STRING')
    self.assertEqual(shifted, 'S IS A')

  if __name__ == '__main__':
    unittest.main()
