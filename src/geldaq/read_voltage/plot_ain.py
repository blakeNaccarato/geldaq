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


import datetime
from pathlib import Path
import sys
import time

import keyboard
from labjack import ljm
import pandas as pd

from geldaq.read_voltage.configs import DEFAULT_DATA_DIR

# sys and time are part of Python's built-in library - did not include in requirements.txt


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

delay = 0.025

# This is the initial start time in UTC
TimeStart = time.time()
print("Reference String")

# Create the initial dataframe "data" before the readings are recorded in the
# loop by the LabJack

# Before putting together dfdata, each column will be stored as a list.
# This dataframe will be populated after the loop finishes and the data is saved
# by the user. There are three lists total for each column.

# List 1 / Column 1: Relative Time
RunTimeList = []
# List 2 / Column 2: Voltage Output
Volt = []
# List 3 / Column 3: Real Time in PST
RealTime = []


while True:

    # Relative time measured with reference to start time in UTC
    RunTime = time.time() - TimeStart

    # Voltage reading
    reading = ljm.eReadName(handle, name)

    # Time delay between voltage and relative time readings
    time.sleep(delay)

    # Populate RunTimList list
    RunTimeList.append(RunTime)
    # Populate RealTime list in PST
    RealTime.append(datetime.datetime.now())
    # Populate Voltage list
    Volt.append(reading)

    print(f"\n{name} reading : {reading:f} V")
    print(RunTime)

    # This section handles whether the data needs to be saved
    # https://stackoverflow.com/questions/50733662/how-to-continue-or-exit-the-program-by-pressing-keys
    try:
        # Test conditional statement if voltage reaches a certain threshold

        if reading < 0:
            print("Negative")

        if keyboard.is_pressed("Esc"):

            # If the user does not want to save data, exit the program
            print("Data has not been saved. Exiting...")

            sys.exit(0)

            # If user presses 'Shift' on keyboard, data aquisition stops and file is saved
            # If using alphabetic keys, does not matter if lower case or upper case is pressed

        if keyboard.is_pressed("Shift"):
            # Populate dataFrame with created lists using dictionary
            # Dictionary uses key:value pairs, ex. color:red, year:2012
            # https://favtutor.com/blogs/list-to-dataframe-python

            DictSortData = {
                "Time": RunTimeList,
                "Response": Volt,
                "Local Time": RealTime,
            }
            dfdata = pd.DataFrame(DictSortData)
            print(dfdata)

            # Reference the default directory from the file in which it was created
            # (configs.py)

            # Create directory in case user hasn't run configs.py
            DEFAULT_DATA_DIR.mkdir(exist_ok=True, parents=True)
            print("\nFile saved.")
            # filename = input()
            print(DEFAULT_DATA_DIR)
            dfdata.to_csv(DEFAULT_DATA_DIR / Path("new.csv"))

            break
    except Exception:
        break


# Close handle
ljm.close(handle)
