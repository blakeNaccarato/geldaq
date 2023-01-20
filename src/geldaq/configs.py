# import os
from pathlib import Path

# Default data directory
# ~ stands for the user folder: C:/Users/username
# .expanduser() ensures that the tilde ~ actually represents the user's home path
DEFAULT_DATA_DIR = Path("~/.geldaq/data").expanduser()

# Now the directory is being created. If it already exists, the parameter
# exist_ok=True is set so that an error isn't raised
# Set parents=True, otherwise will return error since it can't find /geldaq
DEFAULT_DATA_DIR.mkdir(exist_ok=True, parents=True)

CANARY = "yellow"
