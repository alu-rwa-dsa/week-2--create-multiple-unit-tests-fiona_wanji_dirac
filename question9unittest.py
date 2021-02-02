from question9 import *


def check_conversion_to_set(setX, listX):
    print(" ")

    print("This is the set " + str(setX) + " and this is the list " + str(listX))
    if setX == listX:
        print("The set and the list are the same, meaning the duplicates weren't removed. Unsuccessful")

    else:
        print("The set and the list aren't equal, meaning the duplicates were removed when"
              "\nit was converted to a set! Successful")


check_conversion_to_set(setA, listA)


def check_set_difference_function(setX, setY):
    if setX.difference(setY) in setY:
        print("Difference function does not work")

    else:
        print("Difference function works!")


W = {1, 2, 3, 4}
V = {1, 2, 3}
check_set_difference_function(W, V)
