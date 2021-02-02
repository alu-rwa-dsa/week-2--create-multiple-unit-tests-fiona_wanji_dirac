

def count_letters(str_input):
    """count the number of letters"""
    if type(str_input) is not str:
        #raise type error when the input is not a string
        raise TypeError

    new_dic = {}
    str_input = str_input.lower()       #make all letters to lower case
    for letter in str_input:
        if letter == " ": #skip spaces
            continue
        if letter in list(new_dic.keys()):  #increment the existing key
            new_dic[letter] += 1
        else:
            new_dic[letter] = 1     #add new key and initialize to 1
    return new_dic

# # ===== test case 0 =============
# print("=========== Test case 0 ============\n")
# print(count_letters("my first name is dirac"))

# # ===== test case 1 =============
# print("\n=========== Test case 1 ============\n")
# print(count_letters("       my           first      name        is        dirac       "))

# # ===== test case 2 =============
# print("=========== Test case 2 ============\n")
# print(count_letters("MMMMmmmmmy first name is Dirac. I am a congolese born in Kinshasa."))