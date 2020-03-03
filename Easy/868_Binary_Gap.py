class Solution:
    def binaryGap(self, N: int) -> int:
        N = str(bin(N))
        ans, left_point = 0, 0
        for index, i in enumerate(N[2:]):
            if(int(i) == 1):
                if(index - left_point > ans):
                    ans = index - left_point
                left_point = index
        return(ans)