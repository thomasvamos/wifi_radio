#!/usr/bin/python

class TextShifter(object):

  def __init__(self, columns):
     self.shiftIdx = 0
     self.cols = columns

  def resetShiftIndex(self):
    self.shiftIdx = 0

  def shiftText(self, text):
      self.shiftIdx += 1
      startIdx = self.shiftIdx % len(text)
      endIdx = (self.shiftIdx + self.cols) % len(text)
      if startIdx < endIdx:
        return text[startIdx:endIdx]
      else:
        return text[startIdx:len(text)] + text[0:endIdx]