"""
Demonstrates reading a single analog input (AIN) from a LabJack.

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
    Analog Inputs:
        https://labjack.com/support/datasheets/t-series/ain

"""


import sys
import time

import keyboard

# sys and time are part of Python's built-in library - did not include in requirements.txt
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

# Setup and call eReadName to read from AIN0 on the LabJack.
name = "AIN0"

# while loop to continously read voltage, delay can be adjusted (in seconds)
# Will write function for this in future, set the delay as a parameter (Convert to ms)
# for use as a function parameter ex. delay = 150

delay = 0.01

while True:
    result = ljm.eReadName(handle, name)
    # Time delay between readings
    time.sleep(delay)
    print(f"\n{name} reading : {result:f} V")

    # This section handles whether the data needs to be saved or not
    try:
        if keyboard.is_pressed("Esc"):

            # If the user does not want to save data, exit the program
            print("Data has not been saved. Exiting....")
            sys.exit(0)

            # If user presses 's' on keyboard, data aquisition stops and file is saved
            # Does not matter if lower case or upper case 's' is pressed.
        if keyboard.is_pressed("s"):
            print("File saved.")
            break
    except Exception:
        break


# Close handle
ljm.close(handle)
