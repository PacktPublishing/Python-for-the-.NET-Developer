using System;

namespace ch4
{
    class Employee{
        private string _name;
        
        // Constructor
        public Employee(string name){
            _name = name;
        }
    }

    class Program
    {
        static void DemoClass(){
           // Create employee object
           Employee e = new Employee("James");  

        }
        static void Main(string[] args)
        {
            // TODO
        }
    }
}
