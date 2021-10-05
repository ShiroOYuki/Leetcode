using System;

namespace Leetcode_13
{
    public class Solution
    {
        public int RomanToInt(string s)
        {
            char[] c = s.ToCharArray();
            int ans = 0;
            int t = 1;
            for(int i = 0; i < c.Length; i++)
            {
                if(i == c.Length-1)
                {
                    t = 0;
                }
                if(c[i] == 'I')
                {
                    if (c[i + t] == 'V')
                    {
                        ans += 4;
                        i += 1;
                    }
                    else if (c[i + t] == 'X')
                    {
                        ans += 9;
                        i += 1;
                    }
                    else
                    {
                        ans += 1;
                    }
                }
                else if (c[i] == 'V')
                {
                    ans += 5;
                }
                else if (c[i] == 'X')
                {
                    if (c[i + t] == 'L')
                    {
                        ans += 40;
                        i += 1;
                    }
                    else if (c[i + t] == 'C')
                    {
                        ans += 90;
                        i += 1;
                    }
                    else
                    {
                        ans += 10;
                    }
                }
                else if (c[i] == 'L')
                {
                    ans += 50;
                }
                else if (c[i] == 'C')
                {
                    if (c[i + t] == 'D')
                    {
                        ans += 400;
                        i += 1;
                    }
                    else if (c[i + t] == 'M')
                    {
                        ans += 900;
                        i += 1;
                    }
                    else
                    {
                        ans += 100;
                    }
                }
                else if (c[i] == 'D')
                {
                    ans += 500;
                }
                else if (c[i] == 'M')
                {
                    ans += 1000;
                }
            }
            return ans;
        }

        public static void Main(string[] args)
        {
            Solution def = new Solution();
            int ans = def.RomanToInt("DCXXI");
            Console.WriteLine(ans);
        }
    }
}
