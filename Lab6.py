# Omar Ahmad 702444703 / Ryan Fisher 702430872
# Section 12
def my_pow(base, exp):
    '''
    my_pow is a recursive function that raises a number to a power
    Params: (both ints) base (number to be raised), exp (power)
    Returns: the input number raised to the input power
    '''
    if(exp == 0):
        return 1;
    else:
        return base * my_pow(base, exp-1)

def gcd(x,y):
    '''
    gcd is a recursive function that returns the greatest common divisor of two numbers
    Params: two ints, x and y. Order doesn't matter
    Returns: (int) greatest common divisor of x and y
    '''
    if(x % y == 0 and x / y != 0):
        return y
    else:
        return gcd(y, x % y)

def query(dictionary, name):
    '''
    Pulls the birthday of a person in a dictionary, given their name.
    Params: dictionary named dictionary, and the name to look for
    Returns: Birthday of that person, or "I don't know" if that name doesn't exist
    '''
    if(name in dictionary):
        return dictionary[name]
    else:
        return "I don't know"

nick_names = {"John":"Doe","Sarah":"Tiger","Ashley":"Turtle","Bryan":"Bee","Caleb":"Shark"}

def nick_name_list(names, nick_names): # INCOMPLETE
    '''
    Replaces each first name in a list of names with its respective nickname.
    Params: names: list of names, nick_names: dictionary of nicknames.
    Returns: list of names with first names swapped out for nicknames.
    '''
    for i in range(0,len(names)):
        if(names[i].split(" ", 1)[0] in nick_names):
            names[i] = nick_names[names[i].split(" ", 1)[0]] + " " + names[i].split(" ", 1)[1]
        else:
            names[i] = "Walrus " + names[i].split(" ", 1)[1]
    return names

nameList = open("names.txt", "r")
i = 0
for aline in nameList:
    if aline[0] == "M":
        i += 1
print(i)

def word_frequency(fileName):
    '''
    Produces a dictionary that contains the number of occurrences of every word
        in a given text file
    Param: fileName a txt file in the same directory as this py file
    Returns: A dictionary with words as keys and their frequency as definitions
    '''
    wordList = open(fileName, "r" )
    wordFreq = dict()
    for aline in wordList:
        if aline.strip() in wordFreq:
            wordFreq[aline.strip()] += 1
        else:
            wordFreq[aline.strip()] = 1
    return wordFreq

def linear_search(listInt, findNum):
    '''
    Finds the first instance of a given number inside a list of numbers.
    Params: listInt[] a list of numbers, findNum the number to be found.
    Returns: position of that number, -1 if it doesn't exist.
    '''
    for i in range(len(listInt)):
        if listInt[i] == findNum:
            return i + 1
    return -1

def is_sorted(intList):
    '''
    Consumes a list of integers and returns if the list is sorted ascending.
    Param: intList a list of integers.
    Returns: True if the list is in ascending order, False otherwise.
    '''
    for i in range(1,len(intList)):
        if intList[i] < intList[i-1]:
            return False
    return True

def counts(valList):
    '''
    Consumes a list of integers and makes a list of their respective frequency.
    Param: list of integers. Order doesn't matter at this point.
    Returns: list of the frequencies of those integers.
    '''
    freqList = [0]*(max(valList)+1)
    for i in range(max(valList)+1):
        for j in range(len(valList)):
            if valList[j] == i:
                freqList[i] += 1
    return freqList

def values(freqList):
    '''
    Consumes list of integer frequencies (passed by counts()) and returns
        the original list of values, but sorted.
    Param: list of integer frequencies.
    Returns: sorted list of the original values.
    '''
    sortedList = []
    for i in range(len(freqList)):
        for j in range(freqList[i]):
            sortedList.append(i)
    return sortedList
