# Time:  O(n)
# Space: O(1)
#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# For example,
# Given input array A = [1,1,2],
# 
# Your function should return length = 2, and A is now [1,2].
#

class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums)==0:
            return 0
        
        last, i =0,1
        
        while i<len(nums):
            if nums[last]!=nums[i]:
                #count non duplicate
                last+=1
                #keep record last iteration value of i in order to compare with next iteration
                nums[last]=nums[i]                
            i+=1
        return last +1

class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums)==0 :return 0
        left=0
        for i, num in enumerate(nums[1:]):# slow????
            if nums[left]!=num:
                left+=1
                nums[left]=num
        return left+1

if __name__ == "__main__":
    print Solution().removeDuplicates([1, 1, 2])