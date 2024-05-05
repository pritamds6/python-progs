#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are 
# not equal to val.
class Solution(object):
    
    def removeElement(self, nums, val):
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
            else:
                nums[i]=0
        nums[k]=0
        return k
        
    
sol=Solution()
nums = [3,2,2,3]
val = 3
r=sol.removeElement(nums,val)
print(r,nums)