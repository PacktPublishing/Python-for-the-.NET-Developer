using System;
using static System.Console;
using System.Collections.Generic;

namespace ch3
{
    class Program
    {
        static void DemoLists() {
            // Create, print entire list of friends & first first friend
            WriteLine("Create, print entire list & just first friend:");
            WriteLine("---------------------------------------------");
            List<string> friend_list = new List<string> { "Sky", "Marcel",
                                                "Robin", "Khaleel", "Connie" };
            WriteLine($"All friends = '{friend_list[0]}','{friend_list[1]}'," +
                                    $"'{friend_list[2]}','{friend_list[3]}'," +
                                    $"'{friend_list[4]}'");

            WriteLine($"First Friend = '{friend_list[0]}'");

            // Change value
            friend_list[0] = "Taylor";
            WriteLine($"First Friend with name change = {friend_list[0]}");

            //Print partial list
            WriteLine($"Partial list of friends = '{friend_list[2]}','{friend_list[3]}','{friend_list[4]}'");

            // List within lists aka mulitdimensional array
            List<string> family_list = new List<string> { "Mom", "Dad", "Cousin" };
            List<List<string>> people_list = new List<List<string>>();
            people_list.Add(friend_list);
            people_list.Add(family_list);

            WriteLine("\nWrite out people_list:");
            WriteLine("-------------------------");
            people_list[0].ForEach(WriteLine);
            people_list[1].ForEach(WriteLine);
            WriteLine("\nWrite 3rd element from 2nd list:");
            WriteLine("-----------------------------------");
            WriteLine($"Third person in 2nd list is: {people_list[1][2]}");
        }

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
          //DemoIf();
          DemoLists();
        }
    }
}
