# Predefined parameter "size", if it is not defined
# by the user it will default to this value


def king(size=12):

    # Doc-strings are used at the beginning of
    # modules, functions, classes, etc. and provides details about what the code does

    """
    The purpose of this function is to impart the truth
    and only the truth
    """
    if size < 12:
        print("Heresy!")
    else:
        print("His Majesty Abdul Sennain has a ", size, " inch schlong.")


king()
# ^ Because there is a docstring associated with the king() function, it will appear
#       when you hover over it. This is convenient when you quickly
#       need to know what the function does, information about its parameters, etc.

print(king.__doc__)
# ^ You can actually print the docstring using func.__doc__ (two underscores).
# Perhaps this may be useful if the information is really long.
# This will be very useful when creating graphing functions with multiple parameters
#   to keep track of.
