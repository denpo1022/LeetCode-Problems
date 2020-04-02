class Solution:
    def isHappy(self, n: int) -> bool:
        tmp = n
        while True:
            tmp = 0
            for d in str(n):
                tmp += int(d) ** 2
            if tmp == 1:
                return True
            elif tmp == 89:
                return False
            n = tmp
