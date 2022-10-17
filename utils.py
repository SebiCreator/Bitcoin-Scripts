
# stream is a byte stream in hex or string format
# start is the start of the byte stream
def decodeVarInt(stream,start=0):
    if type(stream) == int:
        data = hex(stream)[2*start+2:]
    elif type(stream) == str:
        data = stream[2*start:]
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
    if type(stream) == int:
        stream = str(hex(stream))[2:]
    for i in range(0,len(stream),2):
        tmp = "%s%s" % (stream[i],stream[i+1])
        out.append(tmp)
    out.reverse()
    return ''.join(out)

