
 
# Create the class
class Employee:
    def __init__(self):
        None
        
    def DetermineWeeklySalary(self, weeklyHours, wage):
        print("ready to calculate" )

class Permanent(Employee):
    def __init__(self):
        Employee.__init__(self)
    def DetermineWeeklySalary(self, weeklyHours, wage):
        salary = 40 * wage
        print("\nThis ANGRY EMPLOYEE worked " + str(weeklyHours) + 
              " hrs. Paid for 40 hrs (no overtime) at $ " + str(wage) +
                        "/hr = $"+ str(salary) + " \n")
class Contractor(Employee):
    def __init__(self):
        Employee.__init__(self)
    def DetermineWeeklySalary(self, weeklyHours, wage):
        salary = weeklyHours * wage
        print("\nThis HAPPY CONTRACTOR worked " + str(weeklyHours) + 
              " hrs. Paid for "+ str(weeklyHours) +" hrs (w/ overtime) at $ " + str(wage) +
                        "/hr = $"+ str(salary) + " \n")
def GetEmployees():
    somePermanentEmployee = Permanent()
    someContractor = Contractor()
    everyone = [somePermanentEmployee, someContractor]
    return everyone

def main():
    hours = 50
    wage = 70
    employees = GetEmployees()
    
    for e in employees:
        e.DetermineWeeklySalary(hours,wage)

if __name__== "__main__":    
    main()   