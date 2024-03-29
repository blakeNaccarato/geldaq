"""Demonstrates how to read the WiFi RSSI from a LabJack.

Relevant Documentation:

LJM Library:
    LJM Library Installer:
        https://labjack.com/support/software/installers/ljm
    LJM Users Guide:
        https://labjack.com/support/software/api/ljm
    Opening and Closing:
        https://labjack.com/support/software/api/ljm/function-reference/opening-and-closing
    eReadName:
        https://labjack.com/support/software/api/ljm/function-reference/ljmereadname

T-Series and I/O:
    Modbus Map:
        https://labjack.com/support/software/api/modbus/modbus-map
    WiFi:
        https://labjack.com/support/datasheets/t-series/wifi

"""
import sys

from labjack import ljm

# Open first found LabJack
handle = ljm.openS("ANY", "ANY", "ANY")  # Any device, Any connection, Any identifier
# handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
# handle = ljm.open(ljm.constants.dtANY, ljm.constants.ctANY, "ANY")  # Any device, Any connection, Any identifier

info = ljm.getHandleInfo(handle)
print(
    "Opened a LabJack with Device type: %i, Connection type: %i,\n"
    "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i"
    % (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5])
)

if info[0] == ljm.constants.dtT4:
    print("\nThe LabJack T4 does not support WiFi.")
    sys.exit()

# Setup and call eReadName to read the WiFi RSSI from the LabJack.
name = "WIFI_RSSI"
result = ljm.eReadName(handle, name)
print(f"\n{name} : {result:f}")

# Close handle
ljm.close(handle)
