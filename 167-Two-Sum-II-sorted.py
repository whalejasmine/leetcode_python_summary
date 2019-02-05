
#pseudo code
'''
// assume 0 is the first index in array
// and n is the total number of elements in array
left = 0
right = n - 1
while left is less than right
    sum = array[left] + array[right]
    if sum == val return true
    if sum is less than val
        // sum is smaller than value
        // means pair can only exist to the
        // right of left element, so left element
        // should be moved one step next
        left = left + 1
    else
        // sum is greater than value
        // means pair can only exist to the
        // left of right element, so right element
        // should be moved one step previous
        right = right - 1
'''

# Time:  O(n) when array sorted; O(nlogn) as array not sorted but has to be sorted
# Space: O(1)
#
# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that 
# they add up to the target, where index1 must be less than index2. 
# Please note that your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution.
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#

class Solution:
    def twoSum(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start != end:
            sum = nums[start] + nums[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]

if __name__ == "__main__":
    print (Solution().twoSum([2, 7, 11, 15], 9))
    print (Solution().twoSum([1,2, 7,8, 11, 15], 9))