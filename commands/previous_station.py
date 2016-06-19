#!/usr/bin/python

class PreviousStation:

    def __init__(self, lcdPrintUtil, mpc):
    	self.lcdPrintUtil = lcdPrintUtil
    	self.mpc = mpc        
 
    def __call__(self):
        self.lcdPrintUtil.printPreviousStation()
        self.mpc.playPreviousStation()
 
