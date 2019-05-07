using System;
using static System.Console;

namespace ch5
{
    // Step 1 - Create abstract base class
    public abstract class Employee{
        public abstract void DetermineWeeklySalary(int weeklyHours, int wage);
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
