class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if(not g or not s):
            return 0
        ans, cookie_index = 0, 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        for child in g:
            if(child <= s[cookie_index]):
                ans += 1
                cookie_index += 1
            if(cookie_index == len(s)):
                return ans
        return ans