"""Demonstrates how to use the labjack.ljm.eWriteNames (LJM_eWriteNames) function.

Relevant Documentation:

LJM Library:
    LJM Library Installer:
        https://labjack.com/support/software/installers/ljm
    LJM Users Guide:
        https://labjack.com/support/software/api/ljm
    Opening and Closing:
        https://labjack.com/support/software/api/ljm/function-reference/opening-and-closing
    eWriteNames:
        https://labjack.com/support/software/api/ljm/function-reference/ljmewritenames
    Constants:
        https://labjack.com/support/software/api/ljm/constants

T-Series and I/O:
    Modbus Map:
        https://labjack.com/support/software/api/modbus/modbus-map
    DAC:
        https://labjack.com/support/datasheets/t-series/dac

"""
from labjack import ljm

# Open first found LabJack
handle = ljm.openS("ANY", "ANY", "ANY")  # Any device, Any connection, Any identifier
# handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
# handle = ljm.openS("T4", "ANY", "ANY")  # T4 device, Any connection, Any identifier
# handle = ljm.open(ljm.constants.dtANY, ljm.constants.ctANY, "ANY")  # Any device, Any connection, Any identifier

info = ljm.getHandleInfo(handle)
print(
    "Opened a LabJack with Device type: %i, Connection type: %i,\n"
    "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i"
    % (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5])
)

# Setup and call eWriteNames to write values to the LabJack.
numFrames = 2
names = ["DAC0", "TEST_UINT16"]
aValues = [2.5, 12345]  # [2.5 V, 12345]
ljm.eWriteNames(handle, numFrames, names, aValues)

print("\neWriteNames: ")
for i in range(numFrames):
    print(f"    Name - {names[i]}, value : {aValues[i]:f}")

# Close handle
ljm.close(handle)
