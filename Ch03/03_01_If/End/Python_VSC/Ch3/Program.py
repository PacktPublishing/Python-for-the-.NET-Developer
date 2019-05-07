
def demo_if():
    testGrade = 95

    # Ex: if
    if testGrade>85:
        print("You did good!") 
    else:
        print("You did not work hard!")
    
    # Ex: elif
    if testGrade > 94:
        print("You did awesome!")
    elif testGrade > 85:
        print("You did good!")
    else:
        print("You did not work hard!")

    # Ex: multiple operators
    if ((testGrade >= 90) and (testGrade <= 95)):
        print("You almost reached excellence!")

def main():
    demo_if()   

if __name__ =="__main__":
    main()