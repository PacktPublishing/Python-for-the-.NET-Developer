using System;
using System.Collections.Generic;
namespace ch6
{
    // Step 0
    public abstract class Employee
    {
        //public abstract void work();
        public abstract void DetermineWeeklySalary(int weeklyHours, int wage);
    }
    // Step 1
    public class Permanent : Employee
    {
        public override void DetermineWeeklySalary(int weeklyHours, int wage)
        {
            var salary = 40 * wage;
            Console.WriteLine("\nThis ANGRY EMPLOYEE worked {0} hrs. " + 
                              "Paid for 40 hrs (no overtime) at $ {1}" +
                        "/hr = ${2} \n", weeklyHours, wage, salary);
            Console.WriteLine("---------------------------------------------\n");
        }
    }
    // Step 2
    public class Contractor : Employee
    {
        public override void DetermineWeeklySalary(int weeklyHours, int wage)
        {
            var salary = weeklyHours * wage;
            Console.WriteLine("\nThis HAPPY CONTRACTOR worked {0} hrs. " + 
                              "Paid for {0} hrs (w/ overtime) at $ {1}" +
                              "/hr = ${2} ", weeklyHours, wage, salary);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Step 3
            const int hours = 50;
            const int wage = 70;
            List<Employee> employees = GetEmployees();

            foreach (var e in employees)
            {
                e.DetermineWeeklySalary(hours, wage);
            }
        }

        // Step 4
        private static List<Employee> GetEmployees()
        {
            var somePermanentEmployee = new Permanent();
            var someContractor = new Contractor();
            var everyone = new List<Employee> { somePermanentEmployee, someContractor };
            return everyone;
        }
    }

}
