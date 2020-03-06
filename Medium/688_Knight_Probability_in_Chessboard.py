class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        import functools
        @functools.lru_cache(None)
        def get_probability(r, c, k):
            if (r < 0 or r >= N or c < 0 or c >= N):
                return 0
            elif(k == 0):
                return 1
            else:
                return (get_probability(r + 2, c + 1, k - 1) +
                        get_probability(r + 1, c + 2, k - 1) +
                        get_probability(r - 1, c + 2, k - 1) +
                        get_probability(r - 2, c + 1, k - 1) +
                        get_probability(r - 2, c - 1, k - 1) +
                        get_probability(r - 1, c - 2, k - 1) +
                        get_probability(r + 1, c - 2, k - 1) +
                        get_probability(r + 2, c - 1, k - 1)) / 8   
        
        return get_probability(r, c, K)
        