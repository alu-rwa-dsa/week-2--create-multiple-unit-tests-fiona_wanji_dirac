#simple implementatin using builtin methods
def remove_space(str_1):
    new_str = str_1.split()
    new_str = " ".join(new_str)
    return new_str

#implementation using loops
def remove_last_space(str_p, len_str):
    new_str = ""
    i = 0 
    while (i < len_str - 1):
        new_str += str_p[i]
        i += 1
    return new_str

def remove_space2(str_1):
    "remove all spaces"
    if type(str_1) is not str:
        #raise type error when the input is not a string
        raise TypeError

    new_str = ""
    count = 0                   #count the number of white spaces
    check_index = 0             #check if the space is at index 1
    endHasSpace = False         #check if the str ends with a white space
    for letter in str_1:
        if letter == " ":
            if (check_index == 0) and count == 0:
                #check if the first index is a space
                count += 1
                pass
            elif count == 0:
                #not the first index is a space and the previous index is a letter
                new_str += letter
                count += 1
                endHasSpace = True
        else:
            #normal condition
            count = 0
            new_str += letter
            endHasSpace = False  
        check_index += 1

    if endHasSpace == True:
        #remove last space
        new_str = remove_last_space(new_str, len(new_str))
    return new_str