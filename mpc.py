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
  storedPlaylistName = 'wifi_radio_playlist'

  def __init__(self, quiet=False):
    self.quiet = quiet
    self.lastKnownVolume = 0

    self.client = LockableMPDClient(use_unicode=True)
    try:  
      self.client.connect("localhost", 6600)
    except SocketError:
      print "Couldn't connect to mpd."
      exit(1)

    self.updateStationList()
    self.play(0)

  
  '''
  Playback
  '''
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

  '''
  Playlist management
  '''

  def updateStationList(self):
    self.clearCurrentPlaylist()

    playlists = self.getStoredPlaylists()
    if any(item['playlist'] == self.storedPlaylistName for item in playlists):
      self.deleteStoredPlaylist(self.storedPlaylistName)
      
    self.loadPlaylist(cfg.playlist_file)
    self.savePlaylist(self.storedPlaylistName)

  def getStoredPlaylists(self):
    with self.client:
      return self.client.listplaylists()

  def deleteStoredPlaylist(self, name):
    with self.client:
      self.client.rm(name)

  def savePlaylist(self, name):
    with self.client:
      self.client.save(name)

  def clearCurrentPlaylist(self):
    with self.client:
      self.client.clear()

  def addStream(self, url):
    print 'adding stream...'
    with self.client:
      self.client.add(url)
    print 'finished adding stream.'

  def loadPlaylist(self, path):
    self.numberOfStations = 0
    try:
      f = open(path, 'r')
      for line in f:
        print "Adding " + line + " to playlist " + self.storedPlaylistName
        self.addStream(line.rstrip())
        self.numberOfStations += 1
      print "Total number of playlist entries: " + str(self.numberOfStations)
      f.close()
    except IOError, e:
      print str(e)

    





