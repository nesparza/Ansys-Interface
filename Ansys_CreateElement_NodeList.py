# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:15:23 2010
Creating a script to write direct element formulation in Ansys
I am assuming that the file of nodes has the nodes in ascending (x direction)
order and that the I wish to skip the midside node of the element when making my
new tension elements
@author: Noe
"""
# import modules

from numpy import *			#this loads the numpy module
import sys
from os.path import dirname,join
# these modules assist creation of graphical user file dialog
import Tkinter
from tkFileDialog import askopenfilename

# Declare Functions

def importTxtData(inTxt):	
    for l in inTxt:
        try:
            l.split()
            yield array(l.split()[0], dtype = int)
        except:
            print 'Unexpected Split error'
            pass

# BEGIN MAIN CODE/SCRIPT

# initialize GUI dialog box
root = Tkinter.Tk()	# initiliases the window system
root.withdraw()
# This portion asks the user for a file to parse
filename = askopenfilename(filetypes=[('Text File','*.txt')],
title='Node Listing Text File',parent = root)
root.destroy()	# window cleanup

debug = 0

# Load file and read in lines
try:
    fHandle = open(filename)
    rawTxt = fHandle.readlines()
    nodeList = vstack(importTxtData(rawTxt))
    if debug:
        print nodeList
    fHandle.close()    
    
except:
    print 'No File Provided ', sys.exc_info()[0]


# Lets do some crazy stuff
print 'Crazy Stuff'
newElemNodes = nodeList[0::2] #subselect everyother node

# open file to output commands
newFile = join(dirname(filename),'BottomElementCreation.txt')
fHandle = open(newFile,'w')
# Then loop through and pair the nodes 
i = 0
myLine = ''
while i < (len(newElemNodes)-1):
    # Define the Element using node pair
    myLine = 'E,%d,%d\n' % (newElemNodes[i],newElemNodes[i+1])
    i=i+1
    # write out file with commands to create elements from node pairs
    fHandle.write(myLine)
fHandle.close() # File clean up