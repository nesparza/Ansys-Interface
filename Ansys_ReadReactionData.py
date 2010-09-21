# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:50:34 2010
Ansys Reaction Force data reader
@author: Noe
"""

# importing function section
import numpy as np			#this loads the numpy module as np
from os.path import splitext
import matplotlib.pyplot as mp 

import Tkinter
from tkFileDialog import askopenfilename

#from fnmatch import fnmatch

# Begin some function definitions
def orgData(dataArray, headerInfo):
    keys = ['TIME','UX','UY','UZ','FX','FY','FZ']
    dataSet = {}
    for key in keys:
        for i,str in enumerate(headerInfo):
            if not (str.find(key) < 0):
                dataSet[key] = dataArray[:,i]
    
    return dataSet
    
    
def plotForceDisp(data):
    mp.figure()
    mp.plot(data['UX'],data['FX'],'r-',label = 'shear')
    mp.plot(data['UY'],-1*data['FY'],'b-',label = 'normal')
    mp.title('Force Displacement Curves')
    mp.legend()
    print 'plot force displacement'

def plotForceSpace(data):
    mp.figure()
    mp.plot(data['FX'],-1*data['FY'],'r-')
    mp.title('Force Space for loading')
    print 'plot force space data'
    
def plotTimeForce(data):
    mp.figure()
    mp.plot(data['TIME'],data['FX'],'r-',label = 'shear')
    mp.plot(data['TIME'],-1*data['FY'],'b-',label = 'normal')
    mp.title('Force Displacement Curves')
    mp.legend()
    print 'plot time history'    

def parseFile(inTxt,ext):
    """Parse a text or CSV into data and header info.
    
    This method takes in text read from a data file and its extenstion.
    If the data comes from a text or CSV file, the method attempts to extract
    the data and header info (if present)
    
    """
    print 'starting parse'
    # Check extension to determine splitter
    dlmtr = None
    if ext == '.csv': dlmtr = ','
    elif ext == '.txt': dlmtr = None
    else: 
        print 'unrecognized extension' 
        return (0,0)
        
    # Go through and parse the individual line    
    numArray = np.zeros(1)
    for l in inTxt:
        
        try:
            # Capture the numerical data
            tempArr = np.array(l.split(dlmtr),dtype = np.float64)
            if numArray.size == 1:
                numArray = tempArr
            else:
                numArray = np.vstack((numArray,tempArr))
        except ValueError:
            # This except tries to catch header str info
            try:
                tempHead = np.array(l.split(dlmtr),dtype = str)
                headerStr = tempHead
                print 'Header Info Found'
            except ValueError:
                print 'Something is really wrong'
    return (headerStr,numArray)

	
	
# This portion asks the user for a file to parse
root = Tkinter.Tk()	# initiliases the window system
root.withdraw()
filename = askopenfilename(filetypes=[('text','*.txt'),('csv','*.csv')],
title='Select data file to process',parent = root)

root.destroy()	# window cleanup

# Load file and read in lines
try:
    fHandle = open(filename)
    rawTxt = fHandle.readlines()
    ext = splitext(filename)[-1]
    colStr,dataArray = parseFile(rawTxt,ext)
    data = orgData(dataArray,colStr)
    plotForceDisp(data)
    plotForceSpace(data)
    plotTimeForce(data)
    mp.show()
    
except:
    print 'No File Provided'