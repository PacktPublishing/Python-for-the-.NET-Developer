import random
import sys
import os 

# Chapter 5 - Creating & working w/ Classes
# Create the class
class Employee:
    __name = ""     # an attribute

    # Constructor
    def __init__(self, name):
        self.__name = name    #When values are passed in, define them.   
    
    # Getter & Setter  
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name.upper()  

    #  Write employee name
    def getIntro(self):
        return "Name of employee is {}. ".format(self.get_name())


def main():
    #Create employee object
    anEmployee = Employee('james')

    # Execute code
    print(anEmployee.getIntro())

if __name__== "__main__":
    main()
    