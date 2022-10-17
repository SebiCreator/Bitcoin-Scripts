from datetime import datetime

# stream is a byte stream in hex or string format
def decodeVarInt(stream):
    print(stream)
    if type(stream) == int:
        data = hex(stream)[2:]
    data = ifHexintToStr(stream)
    print(data)
    head = int("0x"+data[:2],base=16)
    if head < 0xfd:
        return data[:2]
    elif head == 0xfd:
        return data[2:6]
    elif head == 0xfe:
        return data[2:10]
    elif head == 0xff:
        return data[2:18]


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

# Converts a hexnumber in string format to an normal integer
def hexstrToInt(hexstr: str):
    return int("0x%s" % hexstr,base=16)

# Converts integer in hex format to string in hex format
def ifHexintToStr(hexInput):
    if type(hexInput) == str:
        return hexInput
    elif type(hexInput) == int:
        return str(hex(hexInput))[2:0]
    else:
        print("Unknown Format: %s\n" % type(hexInput))
        exit(1)

# decodes Bitcoin locktime Field
def decodeLocktime(locktime):
    if type(locktime) == str:
        locktime =  hexstrToInt(locktime)
    
    if locktime == 0:
        return ('NoLock',-1)
    elif locktime < (5 * 10e7):
        return ('Blockheight',locktime)
    else:
        formated = datetime.utcfromtimestamp(locktime).strftime('%Y-%m-%d %H:%M:%s')
        return ('Blocktime',formated)


