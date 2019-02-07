# Mehod 1 Gauss
# Time:  O(n)
# Space: O(1) 
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.
# 
# For example,
# Given [[3,0,1]]
# return 2.
#

class Solution1:

    def missingNumber(self, nums) :
        return len(nums)*(len(nums)+1)//2 -sum(nums)





# Mehod 2 brute force hashset
# Time:  O(n)
# Space: O(n) 
#. ??why not use nums instead of num_set


class Solution2:

    def missingNumber(self, nums) :
            num_set=set(nums)
            n=len(nums)+1
            for num in range(n):
                if num not in num_set:
                    return num

# Mehod 3 sort
# Time:  O(nlogn)
# Space: O(n) 
#


class Solution3:
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num


# Mehod 4 Bit Manipulation 
# Time:  O(n)
# Space: O(1) 
#


class Solution4:
    def missingNumber(self, nums):
        missing=len(nums)
        for i,num in enumerate(nums):
            missing^=i^num
            return missing
if __name__ == "__main__":
    print (Solution1().missingNumber([3,0,1])
    print (Solution2().missingNumber([3,0,1])
