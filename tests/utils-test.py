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
    func=hexstrToInt,
    input="0102030405",
    output=0x0102030405
)



# Swap Endian
handleAssessment(
    func=swapEndian,
    input="0102030405",
    output="0504030201"
)

handleAssessment(
    func=swapEndian,
    input="102030405",
    output=-1
)

#handleAssessment(
    #func=swapEndian,
    #input=0x0102030405,
    #output="0504030201"
#)
