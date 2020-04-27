class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        elif nums[0] == 0:
            return False
        else:
            max_index = 0
            for cur_index, element in enumerate(nums):
                if cur_index > max_index:
                    return False
                max_index = max(max_index, element + cur_index)
            return True