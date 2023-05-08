import sys

import sd_util
from labjack import ljm


def usage():
    print(f"Usage: {sys.argv[0]} [directory]")
    sys.exit()


listCwd = None
if len(sys.argv) == 1:
    listCwd = True
elif len(sys.argv) == 2:
    listCwd = False
else:
    usage()

handle = sd_util.openDevice()

dirToRead = sd_util.getCWD(handle) if listCwd else sys.argv[1]

sd_util.listDirContents(handle, dirToRead)
ljm.close(handle)
