class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        
        
        while(low < high):
            mid = (low + high) // 2
            
            if (nums[mid - 1] != nums[mid]) and (nums[mid + 1] != nums[mid]):
                print("I Am here")

                return nums[mid]
            elif nums[mid] == nums[mid + 1]:
                
                #print("I Am here 1 ")

                left = mid - low
                right = high - mid - 1
                
                if left % 2 != 0:
                    high = mid - 1
                elif right % 2 != 0:
                    low = mid + 2
                    
            elif nums[mid] == nums[ mid - 1]:
                
                
                #print("I Am here 2")
                

                
                left = mid - low - 1
                right = high - mid
                
                #print(low, high, left, right)

                
                if left % 2 != 0:
                    high = mid - 2
                elif right % 2 != 0:
                    low = mid + 1
                    
        return nums[low]
                
                    
