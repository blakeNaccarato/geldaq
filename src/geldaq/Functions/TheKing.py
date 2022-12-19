"""
The purpose of this function is to impart the truth
and only the truth
"""

# Predefined parameter "size", if it is not defined
# by the user it will default to this value


def king(size=12):
    if size < 12:
        print("Heresy!")
    else:
        print("His Majesty Abdul Sennain has a ", size, " inch schlong.")


king()
