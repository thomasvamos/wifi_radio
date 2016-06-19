#!/usr/bin/python

class NextStation:

    def __init__(self, lcdPrintUtil, mpc):
    	self.lcdPrintUtil = lcdPrintUtil
    	self.mpc = mpc        
 
    def __call__(self):
        self.lcdPrintUtil.printNextStation()
        self.mpc.playNextStation()
 
