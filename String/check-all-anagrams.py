class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        result = []
        # When comparing alpahets in anagram it's actually co
        dicP = collections.defaultdict(int)
        dicS = collections.defaultdict(int)
        for c in p:
            dicP[c] = dicP[c] + 1
        counter = 0
        for i, c in enumerate(s):
            dicS[c] = dicS[c] + 1
            counter += 1
            if counter == m:
                idx = i- counter + 1
                if dicS == dicP:
                    result.append(idx)
                dicS[s[idx]] = dicS[s[idx]] - 1
                if dicS[s[idx]] == 0:
                    del dicS[s[idx]]
                counter -= 1
        return result
