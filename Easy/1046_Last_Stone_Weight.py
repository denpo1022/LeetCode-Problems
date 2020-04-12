class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1] > stones[-2]:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()
                
        if len(stones) == 1:
            return stones[0]
        else:
            return 0