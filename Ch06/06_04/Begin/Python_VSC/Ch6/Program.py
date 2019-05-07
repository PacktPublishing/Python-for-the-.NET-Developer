
 
# Create the class
class Employee:
    def __init__(self):
        print("Employee created") 
    def DetermineWeeklySalary(self):
        print("ready to calculate")

class Permanent(Employee):
    def __init__(self):
        Employee.__init__(self)
        print("permanent created")
    def DetermineWeeklySalary(self):
        print("ready to calculate for perm emp.")

class Contractor(Employee):
    def __init__(self):
        Employee.__init__(self)
        print("contractor created")
    def DetermineWeeklySalary(self):
        print("ready to calculate for contr. emp.")

def main():
   #anEmployee = Employee()
   aPermanent = Permanent()
   aPermanent.DetermineWeeklySalary()
   aContractor = Contractor()
   aContractor.DetermineWeeklySalary()

if __name__== "__main__":    
    main()   