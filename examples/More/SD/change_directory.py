import sys

import sd_util
from labjack import ljm


def usage():
    print(f"Usage: {sys.argv[0]} directory")
    sys.exit()


if len(sys.argv) != 2:
    usage()

handle = sd_util.openDevice()
sd_util.goToPath(handle, sys.argv[1])
ljm.close(handle)
