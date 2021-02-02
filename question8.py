# Author: Wanjiru Wang'ondu
#
# DSA Implementation Exercises
# W2Q8 Instructions
# Input a list of lists and return a single list with each element occurring exactly once
from typing import List

listA = [1, 2, 2, 3, 4, 5, 6]
listB = ["a", "b", "c", "d", "e", " f", "g"]
listC = ["zebra", "giraffe", "octopus", "gorilla", "zebra"]
listD = ["apple", "banana", "grape", "banana", "apple"]

# this is the list with all the lists the way they are, with duplicates
listOfLists = [listA, listB, listC, listD]

# print(listA[0::])

# this is the new list with the duplicates removed
# this was done by making the lists into sets
newListOfLists = [set(listA), set(listB), set(listC), set(listD)]
print(newListOfLists)



# other trials
# for i in listOfLists:
#     elementList = [i]
#     print(elementList)

# dictOfLists = {"1": listA.copy().__getitem__(1), "2": listB, "3": listC, "4": listD}
# dictOfLists = {"1": listA.copy().__getitem__(1), "2": listB, "3": listC, "4": listD}
# print(dictOfLists)

# if the list elements are put into a set, the duplicates could be removed
# this is because of the sets unordered property

# def converting_lists_to_sets(ListX):
#     newListX = set(ListX)
#     print(newListX)
#
#
# setA = converting_lists_to_sets(listA)
# converting_lists_to_sets(listB),
# converting_lists_to_sets(listC)
# converting_lists_to_sets(listD)
#
# print(dictOfLists)