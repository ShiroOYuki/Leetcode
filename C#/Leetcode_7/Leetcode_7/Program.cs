using System;

namespace Leetcode_7
{
    public class Solution
    {
        public int Reverse(int x)
        {
            char[] c;
            int temp = 1;
            if (x < 0)
            {
                x *= -1;
                temp = -1;
            }
            c = x.ToString().ToCharArray();
            Array.Reverse(c);
            string s = new string(c);
            try
            {
                x = int.Parse(s) * temp;
            }
            catch
            {
                return 0;
            }
            return x;
        }

        public static void Main(string[] args)
        {
            Solution def = new Solution();
            int x = def.Reverse(1534236469);
            Console.WriteLine(x);
        }
    }
}
