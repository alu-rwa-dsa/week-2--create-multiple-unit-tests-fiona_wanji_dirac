from question8 import *


def check_conversion_to_set(setX, listX):
    print(" ")

    print("This is the set " + str(setX) + " and this is the list " + str(listX))
    if setX == listX:
        print("The set and the list are the same, meaning the duplicates weren't removed. Unsuccessful")

    else:
        print("The set and the list aren't equal, meaning the duplicates were removed when"
              "\nit was converted to a set! Successful")


check_conversion_to_set(set(listB), listB)
