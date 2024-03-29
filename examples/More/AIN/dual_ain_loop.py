"""Demonstrates reading 2 analog inputs (AINs) in a loop from a LabJack.

Relevant Documentation:

LJM Library:
    LJM Library Installer:
        https://labjack.com/support/software/installers/ljm
    LJM Users Guide:
        https://labjack.com/support/software/api/ljm
    Opening and Closing:
        https://labjack.com/support/software/api/ljm/function-reference/opening-and-closing
    Multiple Value Functions(such as eWriteNames):
        https://labjack.com/support/software/api/ljm/function-reference/multiple-value-functions
    Timing Functions(such as StartInterval):
        https://labjack.com/support/software/api/ljm/function-reference/timing-functions

T-Series and I/O:
    Modbus Map:
        https://labjack.com/support/software/api/modbus/modbus-map
    Analog Inputs:
        https://labjack.com/support/datasheets/t-series/ain

"""

import sys

from labjack import ljm

loopMessage = ""
if len(sys.argv) > 1:
    # An argument was passed. The first argument specifies how many times to
    # loop.
    try:
        loopAmount = int(sys.argv[1])
    except:
        raise Exception(
            f'Invalid first argument "{str(sys.argv[1])}". This specifies how many times to loop and needs to be a number.'
        )
else:
    # An argument was not passed. Loop an infinite amount of times.
    loopAmount = "infinite"
    loopMessage = " Press Ctrl+C to stop."

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

deviceType = info[0]

# Setup and call eWriteNames to configure AIN0 and AIN1 on the LabJack.
if deviceType == ljm.constants.dtT4:
    # LabJack T4 configuration

    # AIN0 and AIN1:
    #   Range: +/-10.0 V (10.0). Only AIN0-AIN3 support the +/-10 V range.
    #   Resolution index = Default (0)
    #   Settling, in microseconds = Auto (0)
    names = [
        "AIN0_RANGE",
        "AIN0_RESOLUTION_INDEX",
        "AIN0_SETTLING_US",
        "AIN1_RANGE",
        "AIN1_RESOLUTION_INDEX",
        "AIN1_SETTLING_US",
    ]
    aValues = [10.0, 0, 0, 10.0, 0, 0]
else:
    # LabJack T7 and other devices configuration

    # AIN0 and AIN1:
    #   Negative channel = single ended (199)
    #   Range: +/-10.0 V (10.0)
    #   Resolution index = Default (0)
    #   Settling, in microseconds = Auto (0)
    names = [
        "AIN0_NEGATIVE_CH",
        "AIN0_RANGE",
        "AIN0_RESOLUTION_INDEX",
        "AIN0_SETTLING_US",
        "AIN1_NEGATIVE_CH",
        "AIN1_RANGE",
        "AIN1_RESOLUTION_INDEX",
        "AIN1_SETTLING_US",
    ]
    aValues = [199, 10.0, 0, 0, 199, 10.0, 0, 0]
numFrames = len(names)
ljm.eWriteNames(handle, numFrames, names, aValues)

print("\nSet configuration:")
for i in range(numFrames):
    print(f"    {names[i]} : {aValues[i]:f}")

names = ["AIN0", "AIN1"]

print(f"\nStarting {str(loopAmount)} read loops.{loopMessage}\n")
intervalHandle = 1
ljm.startInterval(intervalHandle, 1000000)  # Delay between readings (in microseconds)
i = 0
numFrames = 2
while True:
    try:
        results = ljm.eReadNames(handle, numFrames, names)
        print(f"AIN0 : {results[0]:f} V, AIN1 : {results[1]:f} V")
        ljm.waitForNextInterval(intervalHandle)
        if loopAmount != "infinite":
            i = i + 1
            if i >= loopAmount:
                break
    except KeyboardInterrupt:
        break
    except Exception:
        print(sys.exc_info()[1])
        break

# Close handles
ljm.cleanInterval(intervalHandle)
ljm.close(handle)
