using System;
using static System.Console;

namespace Ch3
{
    #region "test"

    class Program
    {
        static void printRiseAndShine()
        {
            var day = "Wednesday";
            WriteLine("\nRise & Shine on this " + day + "\n");
        }
        static void demoArithmetic()
        {
            Console.WriteLine(demoAddition(5, 2));
            Console.WriteLine("5 - 2 = {0}", 5 - 2);
            Console.WriteLine("5 * 2 = {0}", 5 * 2);
            Console.WriteLine("5 / 2 = {0}", (decimal)5 / (decimal)2);
            Console.WriteLine("5 % 2 = {0}", 5 % 2);
            Console.WriteLine("5 ** 2 = {0}", Math.Pow(5, 2));
            Console.WriteLine("5 // 2 = {0}", Math.Floor(decimal.Divide(5, 2)));
        }
        static void demOrderOfOperations()
        {
            // Order of operations demo
            Console.WriteLine("1+2-3*2 = {0}", 1 + 2 - 3 * 2);
            Console.WriteLine("1+(2-3)*2 = {0}", 1 + (2 - 3) * 2);
        }
        static string demoAddition(int numberA, int numberB)
        {
            string sumStatement = String.Format("5 + 2 = {0}", numberA + numberB);
            return sumStatement;
        }

        static void demoBooleanNull()
        {
            bool authorIsReynald = true;
            bool authorIsJames = false;

            Console.WriteLine(Convert.ToInt32(authorIsReynald));
            Console.WriteLine(Convert.ToInt32(authorIsJames));

            string myVal = null;
            if (myVal == null)
                Console.WriteLine("The variable myVal doesn't have a value");

            if (authorIsReynald)
            {
                Console.WriteLine("Reynald is the official author of this course. ");
            }
            else
            {
                Console.WriteLine("Reynald isn't the author.");
            }

        }


        static void Main()
        {
            //printRiseAndShine();
            //demoArithmetic();
            //demOrderOfOperations();
            demoBooleanNull(); 
        }
    }
    #endregion
}
