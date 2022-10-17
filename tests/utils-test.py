from testmanager import *
import os
import sys
import inspect

# For importing the parent dir
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from src import *


handleAssessment(
    real=hexstrToInt("0102030405"),
    should=0x0102030405,
    name="hexstrToInt"
)



# Swap Endian
handleAssessment(
    real=swapEndian("0102030405"),
    should="0504030201",
    name="swapEndian"
)

handleAssessment(
    real=swapEndian("102030405"),
    should=-1,
    name="swapEndian"
)

#handleAssessment(
    #real=swapEndian(0x0102030405),
    #should="0504030201",
    #name="swapEndian"
#)
