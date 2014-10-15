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
# http://rollcode.com/get-raspberry-pi-time-date-using-python/

from datetime import datetime

class DateTimeUtil(object):

  def getDate(self):
    date = datetime.now().strftime('%b %d %y')
    return date

  def getTime(self):
    time = datetime.now().strftime('%H:%M:%S')
    return time
