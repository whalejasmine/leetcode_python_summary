# Method 1 Bit maniputation. ???
# Time:  O(2^n)
# Space: O(1)
#
# Given a set of distinct integers, nums, return all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
# 
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#

class Solution1:
	# @param nums, a list of integer
	# @return a list of lists of integer
	def subsets(self,nums):
		elem_num=len(nums)
		subset_num=1<<len(nums)
		subset_set=[[] for i in range(subset_num)]
		for i in range(elem_num):
			for j in range(subset_num):
				if (j>>i) & 1:
					subset_set[j].append(nums[i])

		return subset_set
if __name__ == "__main__":
    print (Solution1().subsets([1, 2, 3]))




# Method 2 Iteratively
# Time:  O(n^2)
# Space: O(n)


class Solution2:
	# @param nums, a list of integer
	# @return a list of lists of integer
	def subsets(self,nums):
		res=[[]]
		for num in sorted(nums):
			res+=[item+[num] for item in res]
		return res 
if __name__ == "__main__":
    print (Solution2().subsets([1, 2, 3]))


# Method 3 DFS
# Time:  ?? O(V+E)
# Space: O(n)


class Solution3:
	# @param nums, a list of integer
	# @return a list of lists of integer
	def subsets(self,nums):
		res=[]
		self.dfs(sorted(nums),0,[],res)
		return res 
	def dfs(self,nums,index,path,res):
		res.append(path)
		for i in range(index,len(nums)): #iterate all vertex and gerate path
			self.dfs(nums,i+1,path+[nums[i]],res)
if __name__ == "__main__":
    print (Solution3().subsets([1, 2, 3]))
