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
from lockable_mpdclient import LockableMPDClient
import configuration as cfg

class MusicPlayerController(object):

  currentStation = 0
  numberOfStations = 0

  def __init__(self, quiet=False):
    self.quiet = quiet
    self.lastKnownVolume = 0

    self.client = LockableMPDClient(use_unicode=True)
    try:  
      self.client.connect("localhost", 6600)
    except SocketError:
      print "Couldn't connect to mpd."
      exit(1)

    self.clearPlaylist()
    self.loadPlaylist(cfg.playlist_file)
    self.play(0)

  def clearPlaylist(self):
    with self.client:
      self.client.clear()

  def addStream(self, url):
    print 'adding stream...'
    with self.client:
      self.client.add(url)
    print 'finished adding stream.'

  def play(self, entry=0):
    print 'Playing entry: ' + str(entry)
    with self.client:
      self.client.play(entry)
    print 'Set station to entry' + str(entry)

  def stop(self):
    with self.client:
      self.client.stop()   

  def pause(self):
    with self.client:
      self.client.pause()

  def getVolume(self):
    print 'getting volume...'
    with self.client:
      status = self.client.status()
    print 'retrieved volume: ' + str(status['volume'])
    return int(status['volume'])


    # if not status and not status['volume']:
    #   return self.lastKnownVolume

    # self.lastKnownVolume = int(status['volume'])
    # return self.lastKnownVolume

  def increaseVolume(self):
    curVol = self.getVolume()

    if curVol == 100:
      return
    
    with self.client:
      self.client.setvol(curVol + 1)

  def decreaseVolume(self):
    curVol = self.getVolume()

    if curVol == 0:
      return

    with self.client:
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

  def getCurrentSongInfo(self):
    try:
      with self.client:
        result = self.client.currentsong()

      return result
    except ConnectionError:
      print "MPDClient not connected"
      return "Unknown"

  def loadPlaylist(self, path):
    self.numberOfStations = 0
    try:
      f = open(path, 'r')
    except IOError, e:
      print str(e)

    for line in f:
      print "Adding " + line + " as playlist."
      self.addStream(line.rstrip())
      self.numberOfStations += 1
    print "Total number of playlist entries: " + str(self.numberOfStations)
    f.close()





