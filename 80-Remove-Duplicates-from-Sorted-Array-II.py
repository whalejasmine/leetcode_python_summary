## Method 1

# Time:  O(n)
# Space: O(1)
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array A = [1,1,1,2,2,3],
# 
# Your function should return length = 5, and A is now [1,1,2,2,3].
#

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        
        last,i,same =0,1,False
        while i<len(nums):
            if nums[last]!=nums[i] or not same:
                same=nums[last]==nums[i]
                last+=1
                nums[last]=nums[i]
            i+=1
        return last+1
if __name__=="__main__":
	print (Solution().removeDuplicates([1,1,1,2,2,3]))
	print (Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))


## Method 2

# Time:  O(n)
# Space: O(1)

class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail=0
        for num in nums:
            if tail<2 or num !=nums[tail-1] or num!=nums[tail-2]:
                nums[tail]=num
                tail+=1
        return tail
if __name__=="__main__":
	print (Solution2().removeDuplicates([1,1,1,2,2,3]))
	print (Solution2().removeDuplicates([0,0,1,1,1,1,2,3,3]))