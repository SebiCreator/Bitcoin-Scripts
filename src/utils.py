from datetime import datetime
import time
import json

# Converts a hexnumber in string format to an normal integer
def hexstrToInt(hexstr: str):
    return int("0x%s" % hexstr,base=16)


# Converts integer in hex format to string in hex format
def ifHexintToStr(hexInput):
    if type(hexInput) == str:
        return hexInput
    elif type(hexInput) == int:
        return str(hex(hexInput))[2:]
    else:
        print("Unknown Format: %s\n" % type(hexInput))
        return -1


# stream is a byte stream in hex or string format
# convert to NetworkByteOrder or backwards
def swapEndian(stream):
    out = []
    stream = ifHexintToStr(stream)
    if not not len(stream) % 2:
        return -1 
    for i in range(0,len(stream),2):
        tmp = "%s%s" % (stream[i],stream[i+1])
        out.append(tmp)
    out.reverse()
    return ''.join(out)


# stream is a byte stream in hex or string format
# returns 2-Tuple (Value of VarInt,Bytes)
def decodeVarInt(stream):
    if type(stream) == int:
        data = hex(stream)[2:]
    data = ifHexintToStr(stream)
    head = int("0x"+data[:2],base=16)
    if head < 0xfd:
        return (data[:2],1)
    elif head == 0xfd:
        return (data[2:6],2)
    elif head == 0xfe:
        return (data[2:10],4)
    elif head == 0xff:
        return (data[2:18],8)





# decodes Bitcoin locktime Field
def decodeLocktime(locktime):
    if type(locktime) == str:
        locktime =  hexstrToInt(locktime)
    
    if locktime == 0:
        return ['NoLock',-1]
    elif locktime < (5 * 10e7):
        return ['Blockheight',locktime]
    else:
        formated = datetime.utcfromtimestamp(locktime).strftime('%Y-%m-%d %H:%M:%s')
        return ['Blocktime',formated]

def btcToSat(btc):
   return btc * 10e7 

def SatToBtc(sat):
    return sat *10e-9

    
def getUnixTime():
   return time.time() 

def printDictNice(dict):
   print(json.dumps(dict,indent=4,sort_keys=True)) 