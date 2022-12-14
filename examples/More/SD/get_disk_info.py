import sys

from labjack import ljm
import sd_util


def usage():
    print("Usage: %s" % (sys.argv[0]))
    exit()


if len(sys.argv) != 1:
    print("No arguments are allowed")
    usage()

handle = sd_util.openDevice()
sd_util.printDiskInfo(handle)
ljm.close(handle)
