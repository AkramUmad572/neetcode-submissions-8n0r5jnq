class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0
        def substrings_expansion(l,r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        for i in range(len(s)):
            substrings += substrings_expansion(i,i)
            substrings += substrings_expansion(i, i + 1)
        return substrings