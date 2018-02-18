from cisc106 import *
def courseGrade(score):
    '''
    Determines letter grade from number grade
    Input: (int) number grade 0-100
    Output: (string) letter grade A-F
    '''
    score = int(score)
    if  (score <= 10):
        return "F"
    elif(score <= 20):
        return "D"
    elif(score <= 30):
        return "C"
    elif(score <= 50):
        return "B"
    else:
        return "A"

def main():
    '''
    The main function in courseGrade
    no parameters, runs in the shell.
    Prints letter grade after prompting number grade.
    '''
    score = input("Enter your course grade: ")
    print(courseGrade(score))

assertEqual(courseGrade(7), "F")
assertEqual(courseGrade(30), "C")
assertEqual(courseGrade(45), "B")
assertEqual(courseGrade(75), "A")
