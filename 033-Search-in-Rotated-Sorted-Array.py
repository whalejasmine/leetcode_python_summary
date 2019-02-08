# Method 1 Binary search
# Time:  O(logn)
# Space: O(1)
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.

class Solution1:
	# @param nums, a list of integers
	# @param target: an integer to be searched
	# @return an interger
	def search (self,nums,target):
		low, high = 0,len(nums)-1
		while low<=high:
			mid=low+(high-low)//2
			if nums[mid]==target:
				return mid
			if nums[low]<=nums[mid]:
				if nums[low]<=target and target <nums[mid]:
					high = mid-1
				else:
					low = mid+1
			else:
				# if unsorted half first check target in sorted part or not
				if nums[mid]<target and target<nums[high]:
					low = mid+1
				else:
					high=mid-1

		return -1

if __name__=="__main__":
	print(Solution1().search([4, 5, 6, 7, 0, 1, 2], 5))
	print(Solution1().search([1],1))
	print(Solution1().search([4, 5, 6, 7,8, 0, 1, 2,3],1))

# Method 1 Recursion #####more digging######
# Time:  O(logn)
# Space: O(logn)
class Solution2:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer}
	def search(self, nums, target):
	    if not nums:
	        return -1
	    return self.binarySearch(nums, target, 0, len(nums)-1)
	    
	def binarySearch(self, nums, target, start, end):
	    if end < start:
	        return -1
	    mid = (start+end)//2
	    if nums[mid] == target:
	        return mid
	    if nums[start] <= target < nums[mid]: # left side is sorted and has target
	        return self.binarySearch(nums, target, start, mid-1)
	    elif nums[mid] < target <= nums[end]: # right side is sorted and has target
	        return self.binarySearch(nums, target, mid+1, end)
	    elif nums[mid] > nums[end]: # right side is pivoted
	        return self.binarySearch(nums, target, mid+1, end)
	    else: # left side is pivoted
	        return self.binarySearch(nums, target, start, mid-1)

if __name__=="__main__":
	print(Solution2().search([4, 5, 6, 7, 0, 1, 2], 5))
	print(Solution2().search([1],1))
	print(Solution2().search([4, 5, 6, 7,8, 0, 1, 2,3],1))