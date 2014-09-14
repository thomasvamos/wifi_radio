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
from subprocess import call

class MusicPlayerControl(object):

  currentStation = 1
  numberOfStations = 0

  def clearPlaylist(self):
    print "Clear playlist"
    self.runCmd("mpc clear")

  def addStream(self, url):
    print "Add stream: " + url
    self.runCmd("mpc add " + url)

  def play(self, entry=1):    
    print "Play entry " + str(entry)
    self.runCmd("mpc play " + str(entry))

  def playNextStation(self):
    print "Play next station"
    if(self.currentStation+1 > self.numberOfStations):
      self.currentStation = 1
    else:
      self.currentStation += 1
    self.play(self.currentStation)

  def playPreviousStation(self):
    print "Play previous station"
    if(self.currentStation -1 < 1):
      self.currentStation = self.numberOfStations
    else:
      self.currentStation -=1
    self.play(self.currentStation)

  def stop(self):
    print "Stop"
    self.runCmd("mpc stop")

  def runCmd(self, cmd):
    returncode = call(cmd, shell=True)

    if(returncode != 0):
        print "error on command"

  def loadPlaylist(self, path):
    print "Load playlist"
    self.numberOfStations = 0
    f = open(path, 'r')
    for line in f:
      self.addStream(line)
      self.numberOfStations += 1
    f.close()





