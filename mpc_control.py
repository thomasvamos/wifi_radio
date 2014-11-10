#!/usr/bin/python

import threading
import time
from wifi_radio_constants import WifiRadioConstants


class MPCControl(threading.Thread):

  def __init__(self, mpc, queue):
    threading.Thread.__init__(self)
    self.daemon = True
    self.mpc = mpc
    self.queue = queue
    self.running = True

    self.mpc.stop()
    self.mpc.clearPlaylist()
    self.mpc.loadPlaylist("playlist.m3u")
    self.mpc.play()

  def run(self):
    self.running = True
    while self.running:
      if not self.queue.empty():
        item = self.queue.get()
        if item.id == WifiRadioConstants.MENU_MSG_ID:
          self.handleRotaryMenuEvent(item.msg)
        if item.id == WifiRadioConstants.VOLUME_MSG_ID:
          self.handleRotaryVolumeEvent(item.msg)


    print "Stopped mpd control thread"

  def handleRotaryMenuEvent(self, msg):
    if msg == "clockwise":
      print "mpc menu clockwise"
      self.mpc.playNextStation()
    elif msg == "counterclockwise":
      print "mpc menu counterclockwise"
      self.mpc.playPreviousStation()
    elif msg == "button":
      print "mpc menu button"
      self.mpc.toggle()
    else:
      print "mpc menu undefined"

  def handleRotaryVolumeEvent(self, msg):
    if msg == "clockwise":
      print "mpc volume clockwise"
      self.mpc.increaseVolume()
    elif msg == "counterclockwise":
      print "mpc volume counterclockwise"
      self.mpc.decreaseVolume()
    elif msg == "button":
      print "mpc volume button"
      self.mpc.toggle()
    else:
      print "mpc volume undefined"




  

