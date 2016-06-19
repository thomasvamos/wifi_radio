#!/usr/bin/python

from wifi_radio_constants import WifiRadioConstants as WRC
from commands.next_station import NextStation
from commands.previous_station import PreviousStation

class RadioControl(object):


    def __init__(self, mpc):
        self.mpc = mpc

    def handleItem(self, item):
        if item.id == WRC.MENU_MSG_ID:
            self.handleRotaryMenuEvent(item.msg)
        if item.id == WRC.VOLUME_MSG_ID:
            self.handleRotaryVolumeEvent(item.msg)