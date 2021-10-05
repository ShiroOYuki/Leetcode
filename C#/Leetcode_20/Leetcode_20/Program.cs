using System;
using System.Collections;

namespace Leetcode_20
{
    public class Solution
    {
        public bool IsValid(string s)
        {
            Stack t = new Stack();
            if(s.Length %2 != 0)
            {
                return false;
            }
            t.Push(s[0]);
            for(int i=1;i<s.Length;i++)
            {
                if(t.Count != 0)
                {
                    if ((t.Peek()).ToString() == "{" && s[i] == '}')
                    {
                        t.Pop();
                    }
                    else if ((t.Peek()).ToString() == "[" && s[i] == ']')
                    {
                        t.Pop();
                    }
                    else if ((t.Peek()).ToString() == "(" && s[i] == ')')
                    {
                        t.Pop();
                    }
                    else
                    {
                        t.Push(s[i]);
                    }
                }
                else
                {
                    t.Push(s[i]);
                }
            }
            if(t.Count == 0)
            {
                return true;
            }
            return false;
        }

        static void Main()
        {
            Solution def = new Solution();
            bool ans = def.IsValid("{}()][");
            Console.WriteLine(ans);
        }
    }
}
