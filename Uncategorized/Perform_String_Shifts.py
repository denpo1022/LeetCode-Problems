class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for i in shift:
            if i[0] == 1:
                total_shift -= i[1]
            else:
                total_shift += i[1]
        total_shift %= len(s)
        return s[total_shift:] + s[:total_shift]