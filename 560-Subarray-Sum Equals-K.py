''
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
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        res=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1])==k: #O(n) slicing -> calculate presum
                    res+=1
        return res


# Method 2 TLE prefixSum
# Time:  O(n^2) 
# Space: O(1)

class Solution2:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        res=0
        for i in range(len(nums)):
            #record prefix sum at i index
            prefixSum=0
            for j in range(i,len(nums)):
                # loop i to j tetting cumulative sum 
                prefixSum+=nums[j]
                if prefixSum==k:
                    res+=1
        return res


# Method 3 prefix + hashmap -> two sum store your sum as hashmap's key. {sum:frequency}
# Time:  O(n) 
# Space: O(n)

class Solution3:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        dic={0:1} # initialize sum is 0 which occure once; just solve duplicates numbers 
        res=pre_sum=0
        for num in nums:
        	#get sum for each iteration
            pre_sum+=num
            res+=dic.get(pre_sum-k,0)  # presum -k?????? not k-presum
            dic[pre_sum]=dic.get(pre_sum,0)+1
        return res


if __name__ =="main":
	Solution3().subarraySum([1,1,1],2)