"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible
"""



def arrayPairSum(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	return sum(sorted(nums)[::2])