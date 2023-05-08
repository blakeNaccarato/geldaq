import sys

import sd_util
from labjack import ljm


def usage():
    print(f"Usage: {sys.argv[0]}")
    sys.exit()


if len(sys.argv) != 1:
    print("No arguments are allowed")
    usage()

handle = sd_util.openDevice()
sd_util.printDiskInfo(handle)
ljm.close(handle)
