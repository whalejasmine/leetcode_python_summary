# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element 
# is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.

class Solution1:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last0=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[i],nums[last0]=nums[last0],nums[i]
                last0+=1
        return nums
if __name__=="__main__":
	print(Solution1().moveZeroes([0,1,0,3,12]))


# Sort
# Time:  O(nlogn)
# Space: O(n)
#

class Solution2:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key= lambda x: 1 if x == 0 else 0)
        return nums


                
if __name__=="__main__":
    print(Solution2().moveZeroes([0,1,0,3,12]))

# remove method
# Time:  ??
# Space: O(n)
#
class Solution3:
    def moveZeroes(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            for i in range(0,nums.count(0)):
                nums.remove(0)
                nums.append(0)
            return nums
if __name__=="__main__":
    print(Solution3().moveZeroes([0,1,0,3,12]))