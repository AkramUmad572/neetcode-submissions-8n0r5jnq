class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0
        def expansion_feature(l,r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        for i in range(len(s)):
           substrings += expansion_feature(i, i)
           substrings += expansion_feature(i, i + 1)
        return substrings