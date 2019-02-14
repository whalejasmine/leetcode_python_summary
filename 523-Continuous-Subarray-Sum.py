
# Method 1 TLE brute force
# Time:  O(n^3) 
# Space: O(1)
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
class Solution1:



# Method 2 TLE prefixSum
# Time:  O(n^2) 
# Space: O(1)



# Method 3 prefix + hashmap -> two sum store your sum as hashmap's key. {pre_sum:index of computing presum}
# Time:  O(n) 
# Space: O(n)

#For the case when k == 0 , we simply look for 2 consecutive occurences of 0 in nums.
# When k != 0, we try to find 2 indices i and j, such that (sum(nums[0:j]) - sum(nums[0:i])) % k == 0. 
# This can in turn be implemented by maintaining a running sum rs and storing rs % k in a hashset to check for a future occurence of the same number.
class Solution3:
    def checkSubarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        pre_sum=0
        seen={0:-1}
        for i, num in enumerate(nums):
            # k!=0
            if k:
                pre_sum=(pre_sum+num)%k
            else:
                pre_sum+=num
            # record at index i the presum value as key
            if pre_sum not in seen: seen[pre_sum]=i
            # if presum occure again then check there is a sliding window : current i -previous (j) index which has been recored 
            #presum exit or not ( not exit will be equal which mean no sliding window )
            elif i-seen[pre_sum]>1:return True
        return False


if __name__ =="main":
	Solution3().subarraySum([1,1,1],2)