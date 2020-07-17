class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.defaultdict(int)
        result = []
        for i in nums:
            dic[i] += 1
            
        heap = []
        
        for key, value in dic.items():
            heap.append((-1 * value,key))
            
        heapify(heap)
        
        print(heap)
                
        for i in range(k):
            result.append(heappop(heap)[1])
            
        return result
