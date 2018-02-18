# Omar Ahmad / Ryan Fisher
# Lab group 22L
def sumNxN(nestedList, intSample):
    '''
    calculates the sum of all elements in a nested list.
    Parameters: nested list of size N x N, integer value representing N
    Returns: sum of all elements
    '''
    xCounter = 0
    yCounter = 0
    currentSum = 0
    while(xCounter < intSample):
        yCounter = 0
        while(yCounter < intSample):
            currentSum += nestedList[xCounter][yCounter]
            yCounter += 1
        xCounter += 1
    return currentSum

def countEvensNxN(nestedList):
        '''
        Calculates the number of even numbers in a nested list of integers.
        Parameter: one nested list containing integers
        Returns: number of occurrences even numbers make in that list
        '''
        xCounter = 0
        yCounter = 0
        currentSum = 0
        while(xCounter < len(nestedList)):
            yCounter = 0
            while(yCounter < len(nestedList[xCounter])):
                if(nestedList[xCounter][yCounter] % 2 == 0):
                    currentSum +=1
                yCounter += 1
            xCounter += 1
        return currentSum

def aboveThreshold(matrix, threshold):
    '''
    Calculates the sum of floats in a matrix of floats that are greater than a given value.
    Parameters: input matrix, and threshold number
    Returns: sum of instances in which a number in the matrix is above the threshold.
    '''
    xCounter = 0
    yCounter = 0
    currentSum = 0
    while(xCounter < len(matrix)):
        yCounter = 0
        while(yCounter < len(matrix[xCounter])):
            if(matrix[xCounter][yCounter] > threshold):
                currentSum += matrix[xCounter][yCounter]
            yCounter += 1
        xCounter += 1
    return currentSum

def diagonal_diff(matrix):
    '''
    Takes in a square matrix of numbers and calculates the difference between
    the sums of its diagonals.
    Parameter: input matrix to be evaluated
    Return: The difference between the sums of the diagonals
    '''
    Counter = 0
    sum = 0
    while (Counter < len(matrix)):
        sum += matrix[Counter][Counter]
        sum -= matrix[Counter][len(matrix)-1-Counter]
        Counter += 1
    return abs(sum)

def flatten(stringList):
    '''
    Converts a list of strings to a list of characters.
    Parameter: a list of strings
    Return: a list of characters, derived from the parameter.
    '''
    counter = 0
    subcounter = 0
    returnList = []
    while(counter < len(stringList)):
        while(subcounter < len(stringList[counter])):
            returnList.append(stringList[counter][subcounter])
            subcounter += 1
        subcounter = 0
        counter += 1
    return returnList

def mask_encode(boolList, someString):
    '''
    Uses a list of booleans to encode a string.
    Parameters: list of booleans, string (length <= length of boolean list)
    Return: encoded string
    '''
    counter = 0
    returnString = ""
    while(counter < len(someString)):
        if(boolList[counter] == True):
            returnString += someString[counter]
        counter += 1
    return returnString

def count_strange_caps(inString):
    '''
    Counts the number of strange caps in a string.
    Parameter: a string
    Returns: (int) number of strange caps in that string
    '''
    counter = 1
    charsFound = 0
    currentChar = ""
    while (counter < len(inString)):
        if (inString[counter].isupper()):
            charsFound += 1
            counter += 1
        else:
            counter += 1
    return charsFound

def total_strange_caps(inStringList):
    '''
    counts the number of strange caps in a list of strings.
    Dependencies: count_strange_caps()
    Parameter: a list of strings
    Returns: (int) number of strange caps in that list.
    '''
    i = 0
    capsFound = 0
    while (i < len(inStringList)):
        capsFound += (count_strange_caps(inStringList[i]))
        i += 1
    return capsFound

def move(location, speed):
    '''
    Returns a tuple of an objects new location.
    Parameters: (int tuples of 2) location and speed
    Returns: location after 1 time unit has passed.
    '''
    return(location[0] + speed[0], location[1] + speed[1])

def total_money(studentList):
    '''
    Returns the total money of a list of students
    Parameter: List of students, each element is a tuple containing name and money
    Returns: total sum of their money.
    '''
    counter = 0
    moneySum = 0
    while(counter < len(studentList)):
        moneySum += studentList[counter][1]
        counter += 1
    return moneySum

def matrix_find_k(m,k):
    '''
    Locates int value k in int matrix m
    Parameters: int k, int[][] m
    Returns: int(,) position of the first occurrence of k in m, or None if not found.
    '''
    yCounter = 0
    xCounter = 0
    while (yCounter < len(m)):
        while (xCounter < len(m[yCounter])):
            if (m[yCounter][xCounter] == k):
                return (yCounter, xCounter)
            xCounter += 1
        xCounter = 0
        yCounter += 1

    return None
