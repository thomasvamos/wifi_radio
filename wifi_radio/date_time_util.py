'''
Date Time Utility
'''

from datetime import datetime

class DateTimeUtil(object):

  def getDate(self):
    date = datetime.now().strftime('%b %d %y')
    return date

  def getTime(self):
    time = datetime.now().strftime('%H:%M:%S')
    return time
