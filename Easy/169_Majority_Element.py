class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import collections

        elements = collections.Counter([num for num in nums])
        return max(elements, key=lambda x: (elements[x], x))
