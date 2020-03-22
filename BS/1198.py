class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # The main point that I was missing was the smallest of one element will always be before other elmenets of each row ( as in the given row )
        for element in mat[0]:
            flag = True
            for row in mat[1:]:
                if not self.bs(row, element):
                    flag = False
                    break
            if flag == True: return element
        return -1
    
    def bs(self, arr: List[int], element) -> bool:
        
        # These are some good base conditions to have in a binary search
        
        if arr and arr[0] > element: return False
        if arr and arr[-1] < element: return False
        
        i = 0
        j = len(arr) - 1
        
        while i <= j:
            mid = (i + j) // 2
            if arr[mid] == element: 
                return True
            elif arr[mid] < element: 
                i = mid + 1
            else:
                j = mid - 1
        return False
            
                

