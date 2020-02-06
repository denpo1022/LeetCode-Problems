class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k <= 1):
            return 0
        else:
            ans = 0
            left_bound, production = (0, 1)
            for right_bound in range(len(nums)):
                production *= nums[right_bound]
                while(production >= k):
                    production /= nums[left_bound]
                    left_bound += 1
                ans += right_bound - left_bound + 1
            return ans
