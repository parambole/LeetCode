class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {}
        
        for i, num in enumerate(nums):
            if num != 0:
                self.dic[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        A = self.dic
        B = vec.dic
        
        res = 0
        if len(A) < len(B):
            
            A, B = self.dic, vec.dic
        else:
            A, B = vec.dic, self.dic
            
        for key, val in A.items():
            res += val * B.get(key, 0)
            
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
