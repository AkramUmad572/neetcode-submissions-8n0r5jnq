class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = {}, {}

        for i in s:
            if i in s1:
                s1[i] += 1
            else:
                s1[i] = 1
        
        for n in t:
            if n in s2:
                s2[n] += 1
            else:
                s2[n] = 1
        
        if s1 == s2:
            return True
        else:
            return False