using System;
using static System.Console;

namespace ch2
{
    class Program
    {
        // This is a single-line comment

        /*  This is an 
            example of a
            multi-line comment 
        */
        static void DemoPrintGreeting(){
            Console.WriteLine("Rise & Shine!");
        }
        static void DemoLocalVariable(){
            var aVariable = "7";
            aVariable = "The name is 007";
            WriteLine(aVariable);
        }

        static string name = "Unknown";
        static void DemoGlobalVariable(){
            name = "Paul";
            WriteLine(name + "y");
        }
        static void Main(string[] args)
        {
            //DemoPrintGreeting();
            //DemoLocalVariable();
            DemoGlobalVariable();WriteLine(name);
        }
    }
}
