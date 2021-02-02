# Author: Wanjiru Wang'ondu

# W2Q9 instructions
# Input 2 lists - listA with n elements and listB which has all elements of listA except
# one (but the rest are in the same order). Outputs the missing element. E.g.
# f([8,1,2,3],[8,1,3]) outputs 2


listA = ["apple", "banana", "grape", 3, 5, 77, 12]
listB = ["apple", "banana", "grape", 3, 5, 77, 12, 44444]

# to find the element that list b has that is unique, we use the difference method used on sets
# to do this, we have to first convert the two lists to sets
setA = set(listA)
setB = set(listB)

# then, we use the difference operator to find the difference and print to see the element that is in setB but not setA
# the set which has an element the other doesn't have comes first
# I printed the unique element out as a list item

print(list(setB.difference(setA)))





