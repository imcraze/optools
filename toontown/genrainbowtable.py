import sys
import os

from .util import *

from colorama import Fore
from ctypes import *

from .decrypt import decryptByte
import json


def __main__():
    print("== rainbow table generator ==")
    info("Generating rainbow table.")

    key = b"\x13\x37\x69\x42\xD3\x4D\xB3\x3F"

    maxDepth = 100 # will need to be larger for compiling larger scripts

    table = []

    for byte in range(255):
        table.append([])
        for depth in range(maxDepth):
            table[byte].append(decryptByte(byte, depth, key))
    
    rtablePath = "rainbowtable.json"
    with open(rtablePath, "w") as f:
        json.dump(table, f)
    success(f"Outputting rainbow table to: {os.path.basename(f.name)}")