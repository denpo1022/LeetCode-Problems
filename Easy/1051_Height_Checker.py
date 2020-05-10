class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        reorder = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != reorder[i]:
                ans += 1
        return ans
