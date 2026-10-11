class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = {}, {}

        def anagram(string, seen):
            for n in string:
                if n in seen:
                    seen[n] += 1
                else:
                    seen[n] = 1
        anagram(s, s1)
        anagram(t, s2)
        
        
        return s1 == s2