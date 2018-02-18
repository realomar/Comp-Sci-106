# Omar Ahmad / Ryan Fisher
from cisc106 import *
from courseGrade import courseGrade

def accelerate():
    global CAR_SPEED
    CAR_SPEED += 1

def mySum(givenNum):
    count = 0
    totalSum = 0
    while (count < givenNum):
        count += 1
        totalSum += count
    return totalSum

def bmiRisk(bmi, age):
    '''
    bmiRisk calculates risk of heart disease based on age and bmi

    Inputs:
        bmi, given as its own unit
        age, given in years

    Output:
        Risk, given as low, medium, or high.
    '''
    if(bmi < 22):
        if(age < 45):
           return "Low"
        else:
            return "Medium"
    else:
        if(age < 45):
            return "Medium"
        else:
            return "High"

assertEqual(bmiRisk(10, 10), "Low")
assertEqual(bmiRisk(25, 45), "High")
assertEqual(bmiRisk(22, 45), "High")
assertEqual(bmiRisk(10, 45), "Medium")

def blackJack(int1, int2):
    if (int1 > 21):
        if (int2 > 21):
            return 0
        else:
            return int2
    elif (int2 > 21):
        if (int1 > 21):
            return 0
        else:
            return int1
    elif (21-int1 <= 21-int2):
        return int1
    else:
        return int2

def factorial(posInt):
    '''
    Calculates the factorial of a given positive integer
    Input: (int) any positive integer
    Output: (int) its factorial or (string) "none" if input is negative
    '''
    posInt = int(posInt)
    if(posInt < 0):
        return "None"
    elif(posInt == 0):
        return 1
    else:
        counter = posInt
        while(counter > 1):
            counter -= 1
            posInt *= counter
        return posInt

assertEqual(factorial(0), 1)
assertEqual(factorial(1), 1)
assertEqual(factorial(2), 2)
assertEqual(factorial(3), 6)

BASE_RATE=80.00
def bill_small(gigabytes):
    global BASE_RATE
    return BASE_RATE

def bill_medium(gigabytes):
    global BASE_RATE
    amount = (1.15 * BASE_RATE) + (.07 * (gigabytes - 100))
    return amount

def bill_large(gigabytes):
    global BASE_RATE
    amount = BASE_RATE * 2
    return amount

def bill_amount(gigabytes):
    '''
    Calculates the price of the internet bill.
    Input: gigabytes used (int or float)
    Output: bill cost (float)
    '''
    if (gigabytes <= 100):
        return bill_small(gigabytes)
    elif (gigabytes <= 1000):
        return bill_medium(gigabytes)
    else:
        return bill_large(gigabytes)

assertEqual(bill_small(90), 80.00, 2)
assertEqual(bill_medium(110), 92.70, 2)
assertEqual(bill_large(1110), 160.00, 2)

assertEqual(courseGrade(7), "F")
assertEqual(courseGrade(30), "C")
assertEqual(courseGrade(45), "B")
assertEqual(courseGrade(75), "A")

def f(x):
    return x**2 - 3

def g(x, y):
    return x - f(f(y))

def h(x, y, z):
    return g(x, y) + z

# question 14
'''
daysGone = input("how many days have passed since the celebration?")
daysGone = int(daysGone) % 7
if(daysGone < 1):
    print ("Tuesday")
elif(daysGone < 2):
    print ("Wednesday")
elif(daysGone < 3):
    print ("Thursday")
elif(daysGone < 4):
    print ("Friday")
elif(daysGone < 5):
    print ("Saturday")
elif(daysGone < 6):
    print ("Sunday")
else:
    print ("Monday")
'''

string15 = "The three numbers are {:.2f}, {:.2f}, and {:.2f}."
