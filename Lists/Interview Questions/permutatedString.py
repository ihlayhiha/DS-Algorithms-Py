# Given 2 strings, check whether one of them is just a permutated string of the other

def isPermutatedString(str1, str2):

    # Using set method
    # dummy1 = set(str1)
    # dummy2 = set(str2)
    # if dummy1 == dummy2:
    #     return True
    # return False

    # Using sort method
    # if len(str1) != len(str2):
    #     return False
    # dummy1 = list(str1)
    # dummy1.sort()
    # dummy2 = list(str2)
    # dummy2.sort()
    # if dummy1 == dummy2:
    #     return True
    # return False

    # linear search
    if len(str1) != len(str2):
        return False
    for char in str1:
        if char not in str2:
            return False
    return True


print(isPermutatedString('abcd', 'accc'))
