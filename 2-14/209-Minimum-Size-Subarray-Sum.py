# Method 1 two pointer ( when bi-search better or verse v)
# Time: O(n) Worst case????? O(n^2)
# Space: O(1)


# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 


class Solution1:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        #initialize sum and left pointer is 0, keep track of sum total
        total=left=0
        
        #initialize result 1 length larger than total length of nums list in order to stop when result get last index
        result=len(nums)+1. ### really important!!
        
        
        for right,n in enumerate(nums):
            #total plus each iterative n in nums, right pointer move as total <7
            total+=n
            #stop as current sum (total) smaller than target sum(s)
            while total >=s: # past cases? why equal
                # get minimum size to compare with current two pointers length and last iteration
                result=min(result,right-left+1)
                # substruct left pointer value because left pointer will move
                total -=nums[left]
                #when move left pointer? as the total >=s
                left+=1
        # return 0 when nums list only have one element
        return result if result <=len(nums) else 0

# Method 2 Binary search with Recursion  问题
# Time: O(nlogn) 
# Space: O(nlogn) ???

class Solution:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= s:
                left = self.find_left(left, right, nums, s, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, s, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= s:
                left = mid + 1
            else:
                right = mid
        return left


# Method 3 Binary search without Recursion 
# Time: O(nlogn) 
# Space: O(1)




if __name__ == "__main__":
    print (Solution1().minSubArrayLen((7,[2,3,1,2,4,3]))
    print (Solution1().minSubArrayLen((7,[2])) #output: 0