from numpy import uint8
from numpy import uint16
from colorama import Fore

"""def rol1(value, count):
    nbits = 1 * 8
    if count > 0:
        count %= nbits
        high = value >> (nbits - count)
        value <<= count
        value |= high
    return uint8(value)

def rol2(value, count):
    nbits = 1 * 8
    if count > 0:
        count %= nbits
        value = uint8(value)
        high = uint8(value >> uint8(nbits - count))
        value <<= count
        value |= high
    return value"""

def rol1(value, count):
    nbits = 1 * 8
    if count > 0:
        count %= nbits
        high = value >> (nbits - count)
        value <<= count
        value |= high
    return value

def info(str):
    print(f"[{Fore.BLUE}INFO{Fore.RESET}]: {str}")

def warn(str):
    print(f"[{Fore.YELLOW}WARN{Fore.RESET}]: {str}")

def error(str):
    print(f"[{Fore.RED}ERROR{Fore.RESET}]: {str}")
    exit()

def success(str):
    print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}]: {str}")