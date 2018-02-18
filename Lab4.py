# Omar Ahmad / Ryan Fisher
# Lab group 22L

def yesOrNo():
    '''
    Returns True or False if user inputs "yes" or "no."
    No parameters
    Returns: boolean
    '''
    isComplete = False
    while (isComplete == False):
        inputAnswer = input(("please say yes or no"))
        if inputAnswer == "yes":
            isComplete = True
            return True
        elif inputAnswer == "no":
            isComplete = True
            return False

def numberAdder():
    '''
    User inputs integers one at a time until typing "done"
    No parameters or returns
    '''
    isComplete = False
    sumInput = 0
    userInput = "B"
    while isComplete == False:
        userInput = input("Input an integer or 'done' ")
        if userInput == "done":
            isComplete = True
            print(sumInput)
        else:
            sumInput += int(userInput)

def is_prime(n):
    """
    determines if the input is a prime number or not
    """
    if n < 0:
        print("positive numbers only!")
        return
    for i in range(2,n):
        if n % i == 0:
            return False
    return n != 1

def main():
    n = int(input())
    increment = 1
    currentFound = 0
    while currentFound < n:
        if is_prime(increment) == True:
            print(increment)
            increment += 1
            currentFound += 1
        else:
            increment += 1

main()

acc = 0
x = 1
sqr = 1
while x**2 <= num:
    sqr = x**2
    acc += sqr
    x +=1

def fib(n):
    '''
    returns the n'th Fibonacci number
    '''
    fn = 2
    fn_1 = 1
    fn_2 = 1
    loop_num = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 3:
        return 1
    if n == 4:
        return 1
    else:
        while loop_num <= n-3:
            fn += fn_1
            fn_2 = fn_1
            fn_1 = fn - fn_1
            loop_num += 1
        return fn

def countW(in_string):
    """
    Returns the number of "W"'s in the parameter string
    """
    list(in_string)
    loop_count = 0
    w_count = 0
    while loop_count < len(in_string):
        if in_string[loop_count] == "W":
            w_count += 1
            loop_count += 1
        else:
            loop_count += 1
    return w_count

def count_vowels(arg):
    '''
    Returns the number of vowels (both cases) in the parameter string.
    '''
    counter = 0
    vowels = "aAeEiIoOuU"
    for letter in arg:
        if letter in vowels:
            counter += 1
    return counter

def largest_digit(arg):
    '''
    Returns the largest digit in parameter string as an int (or None if no ints were found)
    '''
    countDigit = 9
    isComplete = False
    while isComplete == False:
        if(countDigit < 0):
            isComplete = True
            return None
        elif arg.find(str(countDigit)) != -1:
            isComplete = True
            return countDigit
        else:
            countDigit -= 1

def interleave(a,b):
    """
    interleaves two parameter strings
    Parameters: two strings
    Returns: those strings, interleaved into one
    """
    returnString = ""
    length_a = len(a)
    length_b = len(b)
    if length_a > length_b:
        for i in range(length_a):
            returnString += a[i]
            if i < length_b:
                returnString += b[i]
    elif length_b > length_a:
        for i in range(length_b):
            if i < length_a:
                returnString += a[i]
            if i <= length_b:
                returnString += b[i]
    else:
        for i in range(length_a):
            returnString += a[i]
            if i <= length_b:
                returnString += b[i]
    return returnString

num0 = theLst[0]
theLst.remove(num0)
theLst.insert(0,num0 + "hi")

def print_histogram(lst):
    """
    Takes an parameter list of ints and prints a histogram with asterisks.
    """
    loop_num = 1
    lst_num = 0
    while loop_num <= len(lst):
        lst_value = int(lst[lst_num])
        print('*'*lst_value)
        loop_num += 1
        lst_num += 1

def sum_between(lst,a,b):
    """
    Returns the sum of numbers between a and b in a given list
    Parameters: list, integer a, integer b
    """

    loop_num = 0
    lst_sum = 0
    while loop_num < len(lst):
        if lst[loop_num] >= a and lst[loop_num] <= b:
            lst_sum += lst[loop_num]
            loop_num += 1
        else:
            loop_num += 1
    return lst_sum

def total_numbers(number_list, weights):
    """
    Returns the sum of numbers, weighted
    Parameters: a list of numbers, a list of the weights of those numbers
    """
    loop_num = 0
    total_sum = 0
    for num in number_list:
        total_sum += num * weights[loop_num]
        loop_num += 1
    return total_sum
