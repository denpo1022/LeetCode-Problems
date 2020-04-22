class Solution:
    def countElements(self, arr: List[int]) -> int:
        from collections import Counter

        arr = sorted(arr)
        cnt = Counter()
        for num in arr:
            cnt[num] += 1
        keys = list(cnt.keys())
        values = list(cnt.values())
        ans = 0
        for i in range(len(keys) - 1):
            if keys[i] + 1 == keys[i + 1]:
                ans += values[i]
        return ans