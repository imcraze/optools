import sys
import os

from .util import *

from colorama import Fore
from ctypes import *



def __main__():
    #genRainbowTable()
    if len(sys.argv) < 3:
        print(f"{Fore.RED}ERROR{Fore.RESET}: Syntax: {sys.argv[0]} decrypt file [key]")
        sys.exit()
    
    farg = sys.argv[2]
    key = None

    if len(sys.argv) > 3:
        key = sys.argv[3]
    else:
        key = farg + ".key"

    with open(farg, "rb") as f:
        if key != None:
            with open(key, "rb") as k:
                decryptMarshalDump(f, k)
        else:
            decryptMarshalDump(f, key)
    
    sys.exit()

def genRainbowTable():
    key = b"\x13\x37\x69\x42\xD3\x4D\xB3\x3F"

    maxDepth = 100 # will need to be larger for compiling larger scripts

    table = []

    for byte in range(255):
        table.append([])
        for depth in range(maxDepth):
            table[byte].append(decryptByte(byte, depth, key))
    
    print(table)


def decryptMarshalDump(f, key): 
    print("== marshal dump decrypter ==")

    if(key.read(4) != b"\x6b\x73\x69\x67"):
        error(f"Key file is corrupted!")

    k = key.read()
    key.close()

    f.seek(0x1A)
    codeSize = int.from_bytes(f.read(4), "little")
    f.seek(0x1E)
    code = f.read(codeSize)
    
    decryptedBytes = []
    info(f"Decrypting {os.path.basename(f.name)}...")
    info(f"Code size: {codeSize} bytes.")
    
    depth = 0
    i = 0
    xruns = 0
    for byte in code:
        if xruns > 0:
            xruns -= 1
            continue
         #toonpp.decryptByte(byte, depth, int.from_bytes(k, "little"))
        decByte = decryptByte(byte, depth, k).to_bytes(1, "little")
        """if decByte == b"\xAC":
            depth += 1
            xruns = 1
            oparg = decryptByte(code[i + 1], depth, k).to_bytes(1, "little")
            depth += 1
            #depth += 2
            decByte = decryptByte(int.from_bytes(decByte, "little"), depth, k)
            depth += 1
            oparg = decryptByte(int.from_bytes(oparg, "little"), depth, k)
            decryptedBytes.append(decByte)
            decryptedBytes.append(oparg)
            depth += 1
            i += 2
            continue"""

        depth += 1

        decryptedBytes.append(decByte)
        i += 1
    
    f.seek(0)
    marshalHeader = f.read(0x1E)
    f.seek(0x1E + codeSize)
    restOfMarshal = f.read()

    decName = f.name + ".dec"
    success(f"Finished decrypting {os.path.basename(f.name)}, outputting to {decName}.")

    with open(f.name + ".dec", "wb") as decFile:
        decFile.write(marshalHeader)
        for byte in decryptedBytes:
            if type(byte) == int:
                #print(hex(byte))
                decFile.write(byte.to_bytes(1, "little"))
                continue
            decFile.write(byte)
        decFile.write(restOfMarshal)


def decryptByte(byte, depth, key): # thank you Nat for fixing my shitty python code
    

    keyNum = int.from_bytes(key, "little")
    
    r1 = rol1(byte, 5) 
    r2 = rol1((((depth >> 6) | 1) * (r1 ^ ((keyNum >> (r1 & 0x38)) ))) & 0xFF, 5) 
    r3 = rol1((((2 * depth) | 1) * (((keyNum >> (r2 & 0x38))) ^ r2)) & 0xFF , 5) 

    ret = (((keyNum >> (r3 & 0x38))) ^ r3) & 0xFF

    if depth % 2:
        ret = (0x89 * ret - 1) & 0xff

    return ret