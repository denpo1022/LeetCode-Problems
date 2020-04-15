class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        for i in nums:
            if i == 0:
                zero_count += 1
                if zero_count > 1:
                    break
            else:
                total *= i
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            ans = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans[i] = total
                    return ans
        else:
            ans = [total] * len(nums)
            for i in range(len(ans)):
                ans[i] = int(ans[i] / nums[i])
            return ans