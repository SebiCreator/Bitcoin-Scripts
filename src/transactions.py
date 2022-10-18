from .utils import *
import pprint


def decodeTransaction(transaction):
    out = {}
    pointer = 0
    if type(transaction) == int:
        transaction = str(hex(transaction))[2:]
    

    # Version-Bits
    out["versionNr"] = hexstrToInt(swapEndian(transaction[pointer:pointer+4*2])) # 4 Byte
    pointer += 4 * 2  

    # Input Counter
    value,byteOffset = decodeVarInt(transaction[pointer:])
    out["inputCount"] = hexstrToInt(value) # 1 - 8 Byte
    pointer += byteOffset * 2


    out["vin"] = []

    # VIN - LOOP
    for idx in range(0,out["inputCount"]):
        out["vin"].append({})
        # TXID
        out["vin"][idx]["txid"] = swapEndian(transaction[pointer:pointer+32*2]) # 32 Byte
        pointer += 32 * 2

        #VOUT
        out["vin"][idx]["vout"] = hexstrToInt(swapEndian(transaction[pointer:pointer+(4*2)])) # 4 Byte
        pointer += 4*2

        
        # SCRIPT-SIG (easy for now)
        scriptSigSize,byteOffset = decodeVarInt(transaction[pointer:])
        pointer += byteOffset * 2
        scriptSigSize = hexstrToInt(scriptSigSize)
        print(scriptSigSize)
        out["vin"][idx]["ScriptSig"] = transaction[pointer:pointer+(scriptSigSize*2)]
        pointer += scriptSigSize*2


        # SEQUENCE-NUM
        out["vin"][idx]["sequence"] = hexstrToInt(transaction[pointer:pointer+(4*2)]) # 4 Byte
        pointer += 4*2

    
    # Output Counter
    value,byteOffset = decodeVarInt(transaction[pointer:])
    out["outputCount"] = hexstrToInt(value)
    pointer += byteOffset * 2

    out["vout"] = []
    # VOUT - LOOP
    for idx in range(0,out["outputCount"]):
        # Bitcoin Amount
        out["vout"].append({})
        out["vout"][idx]["value"] = hexstrToInt(swapEndian(transaction[pointer:pointer+(8*2)])) / 10e7 # 8 byte
        pointer += 8*2



    # TODO: !!!!
        value,byteOffset = decodeVarInt(transaction[pointer:])
        lockScriptSize = hexstrToInt(value)
        pointer += byteOffset
        out["vout"][idx]["scriptPubKey"] = transaction[pointer:pointer+(lockScriptSize*2)]
        pointer += lockScriptSize*2
    


    
        

         
    pprint.pprint(out)

