'''
Jady / Section 30L

Question: Write a function punctuationCounter that consumes a string and returns the number of
          punctuation symbols (comma, period, exclamation, colon, semicolon)

Solution:
'''
def punctuationCounter(arg):
    i = 0
    punctuation = ",.!:;"
    for element in arg:
        if element in vowels:
            i += 1
    return i
'''
Test cases:
punctuationCounter("The quick brown fox jumps over the lazy dog.")
> should return 1
punctuationCounter("9:00 p.m.")
> should return 3
punctuationCounter("Hello")
> should return 0
'''
