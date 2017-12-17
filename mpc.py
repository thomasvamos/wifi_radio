#!/usr/bin/python
#
# MPD Utility Class
# 
# Author : Thomas Pieronczyk
# Site   : http://www.impierium.de
# 
# Date   : 14.09.2014
#
# Based on code from the following resources:
import subprocess
import mpd
from mpd import ConnectionError

class MusicPlayerController(object):

  currentStation = 0
  numberOfStations = 0
  currentVolume = 0

  def __init__(self, quiet=False):
    self.quiet = quiet    

    self.client = mpd.MPDClient(use_unicode=True)
    try:
      self.client.connect("localhost", 6600)
    except SocketError:
      print "Couldn't connect to mpd."
      exit(1)

    self.clearPlaylist()
    self.loadPlaylist("playlist.m3u")
    self.play(0)

  def clearPlaylist(self):
    self.client.clear()

  def addStream(self, url):
    self.client.add(url)

  def play(self, entry=0):    
    self.client.play(entry)

  def stop(self):
    self.client.stop()   

  def pause(self):
    self.client.pause()

  def getVolume(self):
    status = self.client.status()
    return int(status['volume'])

  def increaseVolume(self):
    curVol = self.getVolume()
    if curVol == 100:
      return
    self.client.setvol(curVol + 1)

  def decreaseVolume(self):
    curVol = self.getVolume()
    if curVol == 0:
      return
    self.client.setvol(curVol - 1)

  def playNextStation(self):
    if(self.currentStation+1 >= self.numberOfStations):
      self.currentStation = 0
    else:
      self.currentStation += 1
    self.play(self.currentStation)

  def playPreviousStation(self):
    if(self.currentStation -1 < 0):
      self.currentStation = self.numberOfStations-1
    else:
      self.currentStation -=1
    self.play(self.currentStation)

  def getName(self):
    try:
      result = self.client.currentsong()
      return result["file"]
    except ConnectionError:
      print "MPDClient not connected"
      return "Unknown"

  def loadPlaylist(self, path):
    self.numberOfStations = 0
    f = open(path, 'r')
    for line in f:
      print "Adding " + line + " as playlist."
      self.addStream(line.rstrip())
      self.numberOfStations += 1
    print "Total number of playlist entries: " + str(self.numberOfStations)
    f.close()





