class Solution:
    def groupAnagrams(strs):
        # Create dictionary by default
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # 
                count[ord(c) - ord('a')] += 1
            # Tuple is like an array. But key is taken
            ans[tuple(count)].append(s)
        return ans.values()
