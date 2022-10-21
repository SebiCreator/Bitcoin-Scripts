import codecs
import os
from datetime import datetime

import base58
from .utils import *
from base64 import b64encode, b64decode
import ecdsa
import hashlib

# Returns an relativ save private Key 
# arg1 is format
def getPrivKey(format=ifHexintToStr):
    r = os.urandom(32)
    token = b64encode(r).decode('utf-8')
    decoded = int.from_bytes(b64decode(token), 'big')
    return format(decoded)

# Compress Public Key (only X-Coordinate of Point) from PublicKey
def compressPubKey(pubKey):
    if (ord(bytearray.fromhex(pubKey[-2:])) % 2 == 0):
        # Even Number
        compressed = "02"
    else:
        # Odd Number
        compressed = "03"
    return (compressed + pubKey[2:66])

    
# Extracts Public Key from Private Key
def getPublicKey(privKey):
    # Get private key from String to Byte Format
    byte_format = codecs.decode(privKey,'hex')
    # Apply ECDSA 
    pk_raw = ecdsa.SigningKey.from_string(byte_format,curve=ecdsa.SECP256k1).verifying_key
    pk_bytes = pk_raw.to_string()
    # Encode back to hex
    pk_hex = codecs.encode(pk_bytes,'hex')
    # Add version 0x04 for public Key -> decode to string format and compress
    return compressPubKey((b'04' + pk_hex).decode('utf-8'))

    

# Extracts Public Key Hash (P2PKH)
def getPublicKeyHash(pubKey):
    # Transform to hex format
    hex_ = bytearray.fromhex(pubKey)
    # Create first SHA256-Hash
    sha = hashlib.sha256()
    sha.update(hex_)
    # From SHA256 create RIPEMD160 Hash
    rip = hashlib.new('ripemd160')
    rip.update(sha.digest())
    # Return the double Hashed Digest
    return rip.hexdigest()


# Extracts Btc-Address from pubKeyHash
def getBtcAddr(pubKeyHash):
    # Add version Byte 0x00 for Mainnet Id
    mod_hash = "00" + pubKeyHash
    # Create checksum with double Hash -> SHA256(SHA256(mod_hash))
    sha = hashlib.sha256()
    hex_ = bytearray.fromhex(mod_hash)
    sha.update(hex_)
    sha_2 = hashlib.sha256()
    sha_2.update(sha.digest())
    # Extract first 4 bytes of checksum
    checksum = sha_2.hexdigest()[:8]
    # Append checksum to pubkeyHash -> Btc Raw Addr
    addr = mod_hash + checksum
    # Encode Addr to Base58  Encoding for better readability
    b58_encode = base58.b58encode(bytes(bytearray.fromhex(addr))).decode('utf-8')
    return b58_encode

# Checks if Bitcoin Address is valid or not 
def checkValidAddr(addr):
    addr = base58.b58decode(addr)
    addr = str(hex(int.from_bytes(addr,'big')))
    # Extract Data sperately
    data = addr[:-8]
    checksum_should = addr[-8:]
    # CreateChecksum of data
    sha = hashlib.sha256()
    hex_ = bytearray.fromhex(data[2:])
    sha.update(hex_)
    sha2 = hashlib.sha256()
    sha2.update(sha.digest())
    checksum_is = sha2.hexdigest()[:8]
    print(checksum_should)
    print(checksum_is)



# Public Key -> Bitcoin Address
def pubKeyToAddr(pubKey):
    return getBtcAddr(
        getPublicKeyHash(
            pubKey=pubKey
        )
    )

# Private Key -> Bitcoin Address
def privKeyToAddr(privKey):
   pubKeyToAddr(
       getPublicKey(privKey=privKey)
   ) 
    
# Create Dict with 
# {privateKey,publicKey,publicKeyHash,Bitcoin-Address}
def createNewPair():
    priv = getPrivKey()
    pub = getPublicKey(priv)
    pubHash = getPublicKeyHash(pub)
    addr = getBtcAddr(pubHash)
    return {
        "privateKey": priv,
        "publicKey" : pub,
        "publicKeyHash" : pubHash,
        "Adress" : addr
    }