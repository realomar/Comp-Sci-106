def testFunction(nameList):
    newList = open(nameList, "r")
    i = 0
    for aline in newList:
        if aline[0] == "M": 
            i += 1
    print(i)
testFunction("names.txt")