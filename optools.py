from colorama import Fore;
import colorama;
import argparse
import sys

import toontown.decrypt
import toontown.diff

colorama.init()
print(f"{Fore.YELLOW}optools by harold{Fore.RESET}")

if sys.argv[1] == "decrypt":
    toontown.decrypt.__main__()

# dead
elif sys.argv[1] == "diff": # automatically get opcodes by comparing a toontown dump and vanilla python dump
    toontown.diff.t2()

# TODO: rainbow table generator for encrypting opcodes
