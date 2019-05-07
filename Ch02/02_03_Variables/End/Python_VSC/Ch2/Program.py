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

def main():
    #demo_print_greeting()
    #demo_local_variable()
    demo_global_variable(); print(name)

if __name__ =="__main__":
    main()