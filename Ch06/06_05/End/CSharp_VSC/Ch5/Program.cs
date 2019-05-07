using System;

namespace ch5
{
    class Employee {
        private string _name;

        // Getter & Setter
        public string Name
        {
            get { return _name.ToUpper(); }
            set { _name = value; }
        }
        // Constructor
        public Employee(string name)
        {
            _name = name;
        }
        // Write employee name
        public string getIntro() {
            return String.Format("Name of employee is {0}.", Name);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            // Create employee object
            Employee anEmployee = new Employee("James");

            // Execute code
            Console.WriteLine(anEmployee.getIntro());
        }
    }
}
