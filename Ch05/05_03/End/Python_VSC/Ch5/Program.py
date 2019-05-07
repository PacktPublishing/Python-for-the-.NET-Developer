# Step 1 - Create abstract base class
class employee():
    def determine_weekly_salary(self, weeklyHours, wage):
        raise NotImplementedError("This abstract method must be implmented by subclass")

# Step 2 - Inherit from base & define calculation for permanent employee
class permanent(employee):
    def determine_weekly_salary(self, weeklyHours, wage):
        salary = 40 * wage
        print("\nThis ANGRY EMPLOYEE worked " + str(weeklyHours) + 
              " hrs. Paid for 40 hrs (no overtime) at $ " + str(wage) +
                        "/hr = $"+ str(salary) + " \n")     

# Step 3 - Inherit from base & define calculation for contractor 
class contractor(employee):
     def determine_weekly_salary(self, weeklyHours, wage):
         salary = weeklyHours * wage
         print("\nThis HAPPY CONTRACTOR worked " + str(weeklyHours) + 
              " hrs. Paid for "+ str(weeklyHours) +" hrs (w/ overtime) at $ " + 
              str(wage) + "/hr = $"+ str(salary) + " \n")

def main():
    pass


if __name__== "__main__":    
    main()   