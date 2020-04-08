class Solution:
    def countElements(self, arr: List[int]) -> int:  
        added = []
        myset = set()
        count = 0
        for x in arr:
            added.append(x+1)
            myset.add(x)
        for x in added:
            if x in myset:
                count += 1
        return count
