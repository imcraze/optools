import json
import sys
import os
from xmlrpc.client import INVALID_XMLRPC
import dis

from .util import *

ttrOpmap = []
ttrCodeBytes = []
matchCnt = []
pyOps=[]

def t2():

    ttrFileName = sys.argv[2]
    pyFileName = sys.argv[3]
    pyOffset = sys.argv[4]

    i = 0
    for num in range(255):
        pyOps.append([])

    with open(ttrFileName, "rb") as ttrFile:
        ttrFile.seek(0x1A)
        ttrCodeSize = int.from_bytes(ttrFile.read(4), "little")
        ttrFile.seek(0x1e)
        ttrCode = ttrFile.read(ttrCodeSize)
        #for byte in ttrCode:

    with open(pyFileName, "rb") as pyFile:
        pyFile.seek(int(pyOffset, 16))
        depth = 0
        for byte in pyFile.read(ttrCodeSize):
            pyOps[byte].append(depth)
            depth +=1
    
    print(pyOps)

    matchCnt = []
    matches = []
    for num in range(255):
        matchCnt.append([])

    depth = 0
    for byte in ttrCode:
        if depth % 2 == 1:
            continue
        opNum = 0
        for op in pyOps:
            try:
                if op[0] == depth:
                    matches.append((opNum, depth))
            except:
                print("", end="")
            opNum += 1
        depth += 1
    
    for match in matches:
        print(match)
                
    

def thing():
    print("== file differ ==")

    ttrFileName = sys.argv[2]
    pyFileName = sys.argv[3]
    pyOffset = sys.argv[4]

    with open(ttrFileName, "rb") as ttrFile:
        ttrFile.seek(0x1A)
        ttrCodeSize = int.from_bytes(ttrFile.read(4), "little")
        ttrFile.seek(0x1e)
        ttrCode = ttrFile.read(ttrCodeSize)
        #for byte in ttrCode:
            #if type(ttrOpmap[byte]) != list:
             #   ttrOpmap[byte] = []
            #ttrCodeBytes[ttrFile.tell()].append(byte)
            #ttrOpmap[byte].append(ttrFile.tell())
    
    #print(ttrCode)

    codeBytearray = bytearray(ttrCode)
#24fb
    with open(pyFileName, "rb") as pyFile:
        pyFile.seek(int(pyOffset, 16))
        pyCode = pyFile.read(ttrCodeSize)
        """pyFile.seek(0, os.SEEK_END)
        size = pyFile.tell()

        while pyFile.tell() < size - ttrCodeSize:
            ba = bytearray(pyFile.read(ttrCodeSize))
            print(ba)
            loc = pyFile.tell()
            matches = 0
            byteOff = 0
            for byte in ba:
                print(byte)
                if byte == codeBytearray[byteOff]:
                    matches += 1
                byteOff += 1
            matchCnt.append([loc, matches])
        
        highestMatchIdx = 0
        idx = 0
        highestMatch = 0
        for match in matchCnt:
            print(match[1])
            if(match[1] > highestMatch):
                highestMatchIdx = idx
            idx += 1"""
    
    i = 0
    firstLoc = 0
    secondLoc = 0
    firstByte = None
    for byte in pyCode:
        #if i % 2:
            #continue
        if firstByte == None:
            firstByte = byte
            firstLoc = i
        elif byte == firstByte and i != 0:
            #print(f"{hex(byte)} : {str(i)}", end=" ")
            secondLoc = i
            break
        i+=1

    ttrFirstByte = None
    ttrFirstLoc = 0
    ttrSecondLoc = 0
    i = 0

    for byte in ttrCode:
        #if i % 2:
        #    continue
        if ttrFirstByte == None:
            ttrFirstByte = byte
            ttrFirstLoc = i
        elif byte == ttrFirstByte and i != ttrFirstLoc:
            #print(f"{hex(byte)} : {str(i)}", end=" ")
            ttrSecondLoc = i
            break
        i += 1
    
    if ttrSecondLoc == secondLoc:
        info(f"{dis.opname[firstByte]} : {hex(ttrFirstByte)}")
        
        




def __main__():
    ttrFileName = sys.argv[2]
    pyFileName = sys.argv[3]

    with open(ttrFileName, "rb") as ttrFile:
        with open(pyFileName, "rb") as pyFile:
            ttrFile.seek(0x1A)
            ttrCodeSize = int.from_bytes(ttrFile.read(4), "little")
            ttrFile.seek(0x1e)
            ttrCode = ttrFile.read(ttrCodeSize)

            ttrFile.seek(0x1e)
            ttrCodeStart = ttrFile.read(15)
            ttrArgList = bytearray([])
            num = 0
            for byte in ttrCodeStart:
                if num % 2:
                    ttrArgList.append(byte)
                    print(hex(byte))
                num += 1
            
            pyFile.seek(0, os.SEEK_END)
            pyFileSize = pyFile.tell()
            pyFile.seek(0)

            pyFileDiffStart = None
            print(ttrArgList)

            
            while pyFile.tell() < pyFileSize - 9:
                num = 0
                pyArgList = bytearray([])
                for byte in pyFile.read(15):
                    if num % 2:
                        pyArgList.append(byte)
                    if num == 0 and byte == ttrArgList[0]:
                        print(pyArgList)
                    num += 1
                #print(pyArgList)
                if bytes(pyArgList) == bytes(ttrArgList):
                    pyFileDiffStart = pyFile.tell() - 15

            if pyFileDiffStart != None:
                info("found py file diff start!")