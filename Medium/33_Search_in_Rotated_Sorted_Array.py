class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if nums[0] > target:
            if nums[-1] < target:
                return -1
            else:
                if target in nums:
                    return nums.index(target)
                else:
                    return -1
        else:
            if target in nums:
                    return nums.index(target)
            else:
                return -1