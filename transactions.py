from utils import *


def decodeTransaction(transaction):
    out = {}
    if type(transaction) == int:
        transaction = str(hex(transaction))[2:]
    
    out["versionNr"] = swapEndian(transaction[0:4*2])
    out["inputCount"] = decodeVarInt(transaction,4)

    return out
