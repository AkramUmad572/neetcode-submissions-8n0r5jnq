class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = 0, 0
        
        for i in range(len(s)):
            currlen = 1
            #odd lenght strings
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currlen = r - l + 1
                if currlen > resLen:
                    res = l
                    resLen = currlen
                l -= 1
                r += 1
            #even lenght loops
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currlen = r - l + 1
                if currlen > resLen:
                    res = l
                    resLen = currlen
                r += 1
                l -= 1

        return s[res: res + resLen]



