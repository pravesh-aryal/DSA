from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #not expected approach
        #set (s) == set(t)

        #cannot be a valid anagram if length differ
        if (len(s) != len(t)): 
            return False

        charCountS = defaultdict(int)
        charCountT = defaultdict(int)

        for letter in s:
            charCountS[letter] += 1
        
        for letter in t:
            charCountT[letter] += 1

        return charCountS == charCountT

        #another ord approach will do that BS later
