class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) == 1 or s == ''):
            return s
        elif(len(s) == 2):
            if(s[0] == s[1]):
                return s
            else:
                return s[0]
        
        def searchPalindrome(entry1, entry2):
            while(entry1 > 0 and entry2 < len(s)-1):
                entry1 -= 1
                entry2 += 1
                if(s[entry1] != s[entry2]):
                    return s[entry1+1:entry2]
            return s[entry1:entry2+1]
        
        ans = ''
        for i in range(len(s)-2):
            if(s[i] == s[i+2]):
                if(len(ans) < len(searchPalindrome(i, i+2))):
                    ans = searchPalindrome(i, i+2)
        for i in range(len(s)-1):
            if(s[i] == s[i+1]):
                if(len(ans) < len(searchPalindrome(i, i+1))):
                    ans = searchPalindrome(i, i+1)
                    
        if(ans == ''):
            return s[0]
        else:
            return ans