import random
import sys
import os 

# Chapter 4
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

    #Ternary operator
    isAgeGreaterThan25 = True if age > 24 else False
    print("isAgeGreaterThan25=" + str(isAgeGreaterThan25))

def demoLists():
    #Create, print entire list & just first friend
    friend_list = ['Sky', 'Marcel', 'Robin', 
                  'Khaleel', 'Connie']
    print('All Friends =', friend_list)
    print('First Friend =', friend_list[0])
    
    #Change value
    friend_list[0] = "Taylor"
    print('First Friend with name change =', friend_list[0])

    #Print partial list
    print('Partial list of friends =' + str(friend_list[2:5]))
     
    #list within lists
    family_list = ['Mom', 'Dad', 'Cousin']
    people_list = [friend_list,family_list]
    print(people_list)
    print('Third person in 2nd list is: ' + str((people_list[1][2])))

def demoForLoops():
    #Print from 0 to 4
    print("\n*Print from 0 to 4")
    for i in range(0,5):
        print(i, ' ', end="")

    #Print list using 'for'
    print("\n*Print list using 'for'")
    friend_list = ['Sky', 'Marcel', 'Robin','Khaleel', 'Connie']
    for list in friend_list:
        print(list)
        
    #List within list aka 2-dimensional array
    print("\n*Printing nested loop")
    arrayOfPeople = [["Robin", "Khaleel", "Connie"],["Mom","Dad","Sister"]]
    for x in range(0,2):
        for y in range(0,3):
            print(arrayOfPeople[x][y])

def demoWhileLoops():
    print("\n*While loop demo")
    x=0
    while x < 5:
        print("Today, I've got time, son.")
        x = x + 1
def demoDictionary():
    favorite_movie = {'Reynald' : 'Titanic',
                        'Marcel' : 'Enter the Dragon',
                        'Khaleel' : 'The Notebook',
                        'Connie' : 'Superman'}

    print("No shame, Reynald's fav movie is " + favorite_movie['Reynald'])

    print(favorite_movie)                       #print entire dictionary
    del favorite_movie['Connie']                #delete value
    favorite_movie['Khaleel'] = "Star Wars"     #replace value
    
    print("\nReprinting dictionary after modifications")
    print(favorite_movie)                       #reprint entire dictionary

def main():
    #demoIf()
    #demoLists()
    #demoForLoops()
    #demoWhileLoops()
    demoDictionary()

if __name__== "__main__":
    main()
    