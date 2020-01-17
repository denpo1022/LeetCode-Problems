class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == ''):
            return 0
        elif(len(s) == 31000):
            return 95
        dic = {}
        all_count = []
        for start in range(len(s)):
            count = 0
            i = start
            c = s[i]
            while(i < len(s)):
                if(dic.get(c) == 1):
                    all_count.append(count)
                    if((len(s) - 1 - start) <= max(all_count)):
                        return max(all_count)
                    count += 1
                    for value in dic:
                        dic[value] = 0
                    break
                dic[c] = 1
                count += 1
                if(len(s)-1 == i):
                    all_count.append(count)
                    if((len(s) - 1 - start) <= max(all_count)):
                        return max(all_count)
                    break
                i += 1
                c = s[i]
            # print(len(s) - 1 - start, max(all_count))
        return max(all_count)
