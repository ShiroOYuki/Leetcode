using System;

namespace Leetcode_14
{
    public class Solution
    {
        public string LongestCommonPrefix(string[] strs)
        {
            if(strs.Length == 0)
            {
                return "";
            }
            string t = "";
            string ans = "";
            bool IsLink = false;
            bool Isinstr = false;
            for(int i = 0; i < strs[0].Length; i++)
            {
                for(int j = 0; j < strs.Length; j++)
                {
                    try
                    {
                        if (strs[j][i]==strs[0][i])
                        {
                            Isinstr = true;
                        }
                        else
                        {
                            Isinstr = false;
                            return ans;
                        }
                    }
                    catch
                    {
                        Isinstr = false;
                        break;
                    }
                }
                if(Isinstr && IsLink)
                {
                    t += strs[0][i];
                }
                else if (Isinstr)
                {
                    t = strs[0][i].ToString();
                    IsLink = true;
                }
                else
                {
                    if (t.Length>ans.Length)
                    {
                        ans = t;
                    }
                    t = "";
                    IsLink = false;
                }
                if (t.Length > ans.Length)
                {
                    ans = t;
                }
            }
            return ans;
        }

        public static void Main(string[] args)
        {
            Solution def = new Solution();
            string[] str = { "reflower","flow","flight" };
            string t = def.LongestCommonPrefix(str);
            Console.WriteLine(t);
        }
    }
}
