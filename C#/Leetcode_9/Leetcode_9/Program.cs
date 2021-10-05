using System;

namespace Leetcode_9
{
    public class Solution
    {
        public bool IsPalindrome(int x)
        {
            char[] c;
            c = x.ToString().ToCharArray();
            string s1, s2;
            s1 = new string(c);
            Array.Reverse(c);
            s2 = new string(c);
            if(s1==s2)
            {
                return true;
            }
            return false;
        }
        static void Main(string[] args)
        {
            Solution def = new Solution();
            Console.WriteLine(def.IsPalindrome(123));
        }
    }
}
