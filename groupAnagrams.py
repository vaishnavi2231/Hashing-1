# -------- Solution 1 : By sorting the strings------
''' Time Complexity : O(nklogk) : where n = no of strings in the input
                                        k = maximum/average length of the string
                                        O(n) = to process all strings in input, O(klogk) = to sort individual string
    Space Complexity : O(nk) : 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Your code here along with comments explaining your approach

   Approach : 1. Sort each string in the input 
             2. create the index of sorted string and Check if it is already mapped in hashmap,
             3. append the input string to sorted string index
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            hashmap[ss].append(s)
        result=[]
        for v in hashmap.values():
            result.append(v)
        return result


# -------- Solution 2 : By hashing using Prime numbers------
''' Time Complexity : O(nk) : where n = no of strings in the input
                                        k = maximum/average length of the string
    Space Complexity : O(nk) : 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Your code here along with comments explaining your approach

   Approach : 1.Create a unique key by multiplying prime nos assigned to each char
             2. Append the s which has unique keys
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101 ]

        for s in strs:
            key = 1
            for c in s:
                key *= primes[ord(c) - ord('a')]
            hashmap[key].append(s)
        return list(hashmap.values())   
