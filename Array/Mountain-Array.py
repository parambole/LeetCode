class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:  
        
        
        """
        This wont work because this is a google question and you have not thought of all the possible cases. SO ALWAYS THINK THINK OF ALL THE CASES BEFORE WRITTING THE SOLUTION
        
        """
        
        N = len(arr)
        i = 0
        
        while i < N - 1 and arr[i] < arr[i+1]:
            i += 1
            
        if i == 0 or i == N - 1:
            return False
        
        while i < N - 1and arr[i] > arr[i+1]:
            i += 1
            
        return i == N - 1
        
#         n = len(arr)
#         if n <= 2:
#             return False
        
#         numPeaks = 0
#         for i in range(1, n - 1):
#             if arr[i] == arr[i + 1]:
#                 return False
            
#             if arr[i] > arr[i - 1] and arr[i + 1] < arr[i]:
#                 numPeaks += 1
                
#             if numPeaks > 1:
#                 return False
#         return True if numPeaks == 1 else False
        
        
        
            
