class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        local_max = global_max = -10000000000
        for n in nums:
            local_max = max(n, local_max + n)
            global_max = max(local_max, global_max)
        return global_max