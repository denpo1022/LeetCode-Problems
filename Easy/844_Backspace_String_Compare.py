class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = list(S)
        T = list(T)
        i = 0
        while i < len(S):
            if S[i] == '#' and i > 0:
                S.pop(i)
                S.pop(i - 1)
                i -= 1
            elif S[i] == '#' and i == 0:
                S.pop(i)
            else:
                i += 1
        i = 0
        while i < len(T):
            if T[i] == '#' and i > 0:
                T.pop(i)
                T.pop(i - 1)
                i -= 1
            elif T[i] == '#' and i == 0:
                T.pop(i)
            else:
                i += 1
        if S == T:
            return True
        else:
            return False