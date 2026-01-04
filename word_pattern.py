''' Time Complexity : O(n) , where n = length of the string s or pattern
    Space Complexity : O(1) , hashmap will save mapping of max 26 char irrespective of string length, hence constant time.
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Your code here along with comments explaining your approach

   Approach : Using two hashmap, one for mapping pattern to s, and second for vice verca
              Iterating the strings, and checking if the char is previously mapped to some else word if yes, return False

'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        # for pattern to s mapping

        phashmap = {}
        for i in range(len(pattern)):
            c = pattern[i]
            if c in phashmap:
                if phashmap[c] != s[i]:
                    return False
            else:
                phashmap[c] = s[i]

        # for s to pattern mapping
        shashmap = {}
        for i in range(len(s)):
            word = s[i]
            if word in shashmap:
                if shashmap[word] != pattern[i]:
                    return False
            else:
                shashmap[word] = pattern[i]
        return True


        