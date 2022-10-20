import os
from datetime import datetime
from .utils import *
from base64 import b64encode, b64decode
import ecdsa

# Returns an relativ save private Key 
# arg1 is format
def getPrivKey(format=hex):
    r = os.urandom(32)
    token = b64encode(r).decode('utf-8')
    decoded = int.from_bytes(b64decode(token), 'big')
    return format(decoded)

    
    # TODO
def getPublicKey(privKey):
    pass  