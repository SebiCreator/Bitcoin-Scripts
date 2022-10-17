from utils import *


def decodeTransaction(transaction):
    out = {}
    pointer = 0
    if type(transaction) == int:
        transaction = str(hex(transaction))[2:]
    
    out["versionNr"] = swapEndian(transaction[pointer:4*2])
    pointer += 8
    print(transaction[8:])
    out["inputCount"] = decodeVarInt(transaction[8])


    return out
