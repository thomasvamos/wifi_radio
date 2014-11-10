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

class MusicPlayerControl(object):

  currentStation = 1
  numberOfStations = 0

  def __init__(self, quiet=False):
    self.quiet = quiet

  def clearPlaylist(self):
    self.runCmd(["mpc", "clear"])

  def addStream(self, url):
    self.runCmd(["mpc", "add", url])

  def play(self, entry=1):    
    self.runCmd(["mpc", "play", str(entry)])

  def stop(self):
    self.runCmd(["mpc", "stop"])    

  def toggle(self):
    self.runCmd(["mpc", "toggle"])

  def increaseVolume(self):
    self.runCmd(["mpc", "volume", "+5"])

  def decreaseVolume(self):
    self.runCmd(["mpc", "volume", "-5"])    

  def playNextStation(self):
    if(self.currentStation+1 > self.numberOfStations):
      self.currentStation = 1
    else:
      self.currentStation += 1
    self.play(self.currentStation)

  def playPreviousStation(self):
    if(self.currentStation -1 < 1):
      self.currentStation = self.numberOfStations
    else:
      self.currentStation -=1
    self.play(self.currentStation)

  def getName(self):
    result = self.runCmd(["mpc", "-f", "%name%"])
    new_line_idx = result.index('\n')
    return result[:new_line_idx]

  def stop(self):
    self.runCmd(["mpc", "stop"])

  def runCmd(self, cmd):
    if(self.quiet):
       cmd.insert(1,"-q")

    result = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    out, err = result.communicate()
    if err:
      print "Error: " + err
    return out

  def loadPlaylist(self, path):
    self.numberOfStations = 0
    f = open(path, 'r')
    for line in f:
      self.addStream(line.rstrip())
      self.numberOfStations += 1
    f.close()





