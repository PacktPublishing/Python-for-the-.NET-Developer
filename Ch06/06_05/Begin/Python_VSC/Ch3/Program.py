
# Chapter 3

def printRiseAndShine():
    day = "Wednesday"
    print("\nRise & Shine on this " + day + "\n")    

def demoArithmetic():
    print(demoAddition(5,2))
    print("5 - 2 =", 5-2)
    print("5 * 2 =", 5*2)
    print("5 / 2 =", 5/2)
    print("5 % 2 =", 5%2)
    print("5 ** 2 =", 5**2)
    print("5 // 2 =", 5//2)

def demOrderOfOperations():
    print("1+2-3*2 =", 1+2-3*2)
    print("1+(2-3)*2 =", 1+(2-3)*2)

def demoAddition(numberA, numberB):
    sumStatement = "5 + 2 ==" + str(numberA+ numberB)
    return sumStatement

def demoBooleanNon():
    authorIsReynald = True
    authorIsJames = False 

    print (int(authorIsReynald))
    print (int(authorIsJames)) 
    
    myVal = None
    if myVal == None:
        print("The variable myVal doesn't have a value")

    if authorIsReynald:
        print("Reynald is the official author of this course. ")
    else: 
        print("Reynald isn't the author.")

def demoIf():
    #Traditional if/else
    age = 35
    if age !=35:
        print("A value was given ")
        
    name = "Reynald"
    if not name:
        print("The 'if' condition evaluated to true")
    else:
        print("The 'if' condition evaluated to false")

    #Ternerary operator
    isAgeGreaterThan25 = True if age > 24 else False
    print("isAgeGreaterThan25=" + str(isAgeGreaterThan25))

def main():
    #printRiseAndShine()
    #demoArithmetic()
    #demOrderOfOperations()
    demoBooleanNon() 

if __name__== "__main__":
    main()
    