"""Demonstrates how to read the ethernet configuration settings from a LabJack.

Relevant Documentation:

LJM Library:
    LJM Library Installer:
        https://labjack.com/support/software/installers/ljm
    LJM Users Guide:
        https://labjack.com/support/software/api/ljm
    Opening and Closing:
        https://labjack.com/support/software/api/ljm/function-reference/opening-and-closing
    eReadNames:
        https://labjack.com/support/software/api/ljm/function-reference/ljmereadnames
    NumberToIP:
        https://labjack.com/support/software/api/ljm/function-reference/utility/ljmnumbertoip

T-Series and I/O:
    Modbus Map:
        https://labjack.com/support/software/api/modbus/modbus-map
    Ethernet:
        https://labjack.com/support/datasheets/t-series/ethernet

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

# Setup and call eReadNames to read ethernet configuration from the LabJack.
names = [
    "ETHERNET_IP",
    "ETHERNET_SUBNET",
    "ETHERNET_GATEWAY",
    "ETHERNET_IP_DEFAULT",
    "ETHERNET_SUBNET_DEFAULT",
    "ETHERNET_GATEWAY_DEFAULT",
    "ETHERNET_DHCP_ENABLE",
    "ETHERNET_DHCP_ENABLE_DEFAULT",
]
numFrames = len(names)
results = ljm.eReadNames(handle, numFrames, names)

print("\nEthernet configuration:")
for i in range(numFrames):
    if names[i].startswith("ETHERNET_DHCP_ENABLE"):
        print(f"    {names[i]} : {results[i]:.0f}")
    else:
        print(
            "    %s : %.0f - %s"
            % (names[i], results[i], ljm.numberToIP(int(results[i])))
        )

# Close handle
ljm.close(handle)
