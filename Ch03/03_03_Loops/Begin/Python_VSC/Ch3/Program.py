
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

def demo_lists():
    #Create, print entire list & just first friend
    print('Create, print entire list & just first friend')
    print('---------------------------------------------')
    friend_list = ['Sky', 'Marcel', 'Robin', 
                  'Khaleel', 'Connie']
    print('All Friends =', friend_list)
    print('First Friend =', friend_list[0])

    #Change value
    friend_list[0] = "Taylor"
    print('First Friend with name change =', friend_list[0])

    #Print partial list
    print('Partial list of friends =' + str(friend_list[2:5]))

    #List within lists
    family_list = ['Mom', 'Dad', 'Cousin']
    people_list = [friend_list,family_list]
    print('\nWrite out people_list:')
    print('-----------------------')
    print(people_list)
    print('\nWrite 3rd element from 2nd list:')
    print('-----------------------------------')
    print('Third person in 2nd list is:' + (people_list[1][2]))

    

def main():
    #demo_if()  
    demo_lists() 

if __name__ =="__main__":
    main()