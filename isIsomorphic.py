''' Time Complexity : O(n) , where n = length of the string s or t
    Space Complexity : O(1) , hashmap will save mapping of max 26 char irrespective of string length, hence constant time.
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Your code here along with comments explaining your approach

   Approach : Using two hashmap, one for mapping s to t, and second for mapping t to s
              Iterating the strings, and checking if the char is previously mapped to some else char if yes, return False

'''
Class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        shash, thash = {}, {}
        for i in range(len(s)):
            schar, tchar = s[i],t[i]
            # s to t mapping
            if schar in shash:
                if shash[schar] != tchar:
                    return False
            else:
                shash[schar] = tchar
                
            # t to s mapping
            if tchar in thash:
                if thash[tchar] != schar:
                    return False
            else:
                thash[tchar] = schar
        return True    