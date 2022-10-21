import base58
import hashlib
from .utils import *
from .keys import *

resolve = {
    "76" : "OP_DUP",
    "a9" : "OP_HASH160",
    "88" : "OP_EQUALVERIFY",
    "ac" : "OP_CHECKSIG"
}





# 
def parseScript(hexscript):
    for idx in range(0,len(hexscript),2):
        mode = ""
        asm = []
        byte = hexscript[idx] + hexscript[idx+1]
        if idx == 0 and byte == "76":
            mode = "P2PKH"

        if mode == "P2PKH":
           asm.append("OP_DUP") 
           asm.append("OP_HASH160")
           pubKeyHash = hexscript[6:-4]
           asm.append(getBtcAddr(pubKeyHash=pubKeyHash))
           asm.append("OP_EQUALVERIFY")
           asm.append("OP_CHECKSIG")

        return {"mode": mode,
                "asm" : asm,
                "hex" : hexscript}

