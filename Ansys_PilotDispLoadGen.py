# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 13:59:13 2010
Ansys Loading Scripts. This python script will create a set of displacment 
loading condition files to input into Ansys.
@author: Noe
"""
# Import Section
from math import tan,radians
# End Import Section

baseFileName = "pilotLoading_%03dum_Depth_%02dAngle.txt"
commandSyntax = "D,pilot,ux,%f\nD,pilot,uy,%f"
depth = 40e-6
angle = (45,30,20,10)

for gamma in angle:
    myFileName = baseFileName % (depth*1e6, gamma)
    xDist = depth/tan(radians(gamma))
    myCommands = commandSyntax % (xDist,-1*depth)
    
    fileH = open(myFileName, 'w')
    newTitle = "/title, T15P60 %03dum Depth %02dLoad Angle\n" % (depth*1e6,gamma)
    fileH.write(newTitle)
    fileH.write(myCommands)
    fileH.close()
    
    print "Completed: %s" % (myFileName,)