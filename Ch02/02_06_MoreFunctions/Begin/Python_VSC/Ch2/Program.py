import math
# This is a single-line comment

'''  This is an 
     example of a
     multi-line comment 
'''
def demo_print_greeting():
    print("Rise & Shine!!") 

def demo_local_variable():
    a_variable = 7
    a_variable ="The name is 007"
    print(a_variable)

name = "Unknown"
def demo_global_variable():
    global name
    name = "Paul"
    print(name + "y")

def demo_arithmetic():
    print("\nDemo Arithmetic\n")
    print("7 + 2 =", 7+2)
    print("7 - 2 =", 7-2)
    print("7 * 2 =", 7*2)
    print("7 / 2 =", 7/2)
    print("7 % 2 =", 7%2)
    print("7 ** 2 =", 7**2) #Power
    print("7 // 2 =", 7//2) #Floor
    
    print("math.floor(7/2) =", math.floor(7/2))
    print("math.ceil(7/2) =", math.ceil(7/2))

def demo_order_of_operations():
    print("\nDemo Order of Operations\n")
    print("5+7-3*2 =", 5+7-3*2)
    print("5+(7-3)*2 =", 5+(7-3)*2)

def main():
    #demo_print_greeting()
    #demo_local_variable()
    #demo_global_variable(); print(name)
    demo_arithmetic()
    demo_order_of_operations()

if __name__ =="__main__":
    main()