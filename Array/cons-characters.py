class Solution:
    def maxPower(self, s: str) -> int:
        maxCount = 1
        n = len(s)
        dic = collections.defaultdict(int)
        i, j = 0, 0
        while i < n and j < n:
            dic[s[j]] += 1
            if len(dic) > 1:
                dic[s[i]] -= 1
                if dic[s[i]] == 0:
                    del dic[s[i]]
                i += 1
            maxCount = max(maxCount, j-i+1)
            j += 1

        return maxCount
