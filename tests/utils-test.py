from black import out
from testmanager import *
import os
import sys
import inspect

# For importing the parent dir
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from src import *



# Hex String to Int
handleAssessment(
    func=hexstrToInt,
    input="0102030405",
    output=0x0102030405
)

handleAssessment(
    func=hexstrToInt,
    input="0000000",
    output=0x0
)

handleAssessment(
    func=hexstrToInt,
    input="fffffff",
    output=0xfffffff
)

# If Hex Integer than to String else return input

handleAssessment(
    func=ifHexintToStr,
    input="01020304",
    output="01020304"
)

handleAssessment(
    func=ifHexintToStr,
    input=0x12345,
    output="12345"
)

handleAssessment(
    func=ifHexintToStr,
    input=0x00012345,
    output="12345"
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

handleAssessment(
    func=swapEndian,
    input=0x0102030405,
    output=-1
)


# Decode Var Int

handleAssessment(
    func=decodeVarInt,
    input="01",
    output=("01",1)
)

handleAssessment(
    func=decodeVarInt,
    input="fdabcd",
    output=("abcd",2)
)

handleAssessment(
    func=decodeVarInt,
    input=0xff12345678,
    output=("12345678",8)
)


# Decode Locktime

handleAssessment(
    func=decodeLocktime,
    input=0x0000,
    output=('NoLock',-1)
)

handleAssessment(
    func=decodeLocktime,
    input=251019,
    output=('Blockheight',251019)
)


handleAssessment(
    func=decodeLocktime,
    input=1666277491,
    output=('Blocktime',"2022-10-20 14:51:1666270291")
)


# Sat <-> BTC Converter

handleAssessment(
    func=btcToSat,
    input=1,
    output=100000000
)

handleAssessment(
    func=btcToSat,
    input=0.1,
    output=10000000
)

handleAssessment(
    func=SatToBtc,
    input=100000000,
    output=1
)

handleAssessment(
    func=SatToBtc,
    input=10000000,
    output=0.1
)