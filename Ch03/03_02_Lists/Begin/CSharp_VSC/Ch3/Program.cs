using System;
using static System.Console;

namespace ch3
{
    class Program
    {
        static void DemoIf() {
            int testGrade = 95;

            // Ex: if
            if (testGrade>85)
            {
               WriteLine("You did good!"); 
            }else{
                WriteLine("You did not work hard!");
            }

            // Ex: else if
            if (testGrade > 94)
            {
                WriteLine("You did awesome!");
            }
            else if (testGrade > 85)
            {
                WriteLine("You did good!");
            }
            else
            {
                WriteLine("You did not work hard!");
            }
            // Ex: multiple operators
            if ((testGrade >= 90) && (testGrade <= 95))
            {
                WriteLine("You almost reached excellence!");
            }
        }
        static void Main(string[] args)
        {
          DemoIf();
        }
    }
}
