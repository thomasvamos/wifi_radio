#!/usr/bin/python

import threading
import time
from wifi_radio_constants import WifiRadioConstants


class Init(threading.Thread):

  def __init__(self, mpc):
    threading.Thread.__init__(self)
    self.mpc = mpc

  def run(self):
    self.mpc.stop()
    self.mpc.clearPlaylist()
    self.mpc.loadPlaylist("playlist.m3u")
    self.mpc.play()
