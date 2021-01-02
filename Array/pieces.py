class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {}
        
        for piece in pieces:
            dic[piece[0]] = piece
            
        i = 0
        
        while i < len(arr):
            
            if arr[i] not in dic:
                return False
            
            target_piece = dic[arr[i]]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1
                
        return True
                
