# Method   Single Pass Approach
# Time:  O(n)
# Space: O(1)

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        i=j=len(nums)-1
        while i>0 and nums[i-1]>=nums[i]: # if i==0 nums[i-1]???  # "=" is important because [1,1]
            i-=1
        if i==0: # nums are in descending order
            nums.reverse()
            return
        k=i-1 # find the last "ascending" position
        
        while nums[j]<=nums[k]:
            j-=1
        nums[k],nums[j]=nums[j],nums[k]
        
        # reverse the second part
        l,r=k+1,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

if __name__='main':
	Solution().nextPermutation([1,2,3])