# Time:  O(n) loop all tree node
# Space: O(1)

# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples 1:

# Input: [3,9,20,null,null,15,7]

#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7 

# Output:

# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Examples 2:

# Input: [3,9,8,4,0,1,7]

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7 

# Output:

# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Examples 3:

# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2

# Output:

# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
#]

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None

class Solution:
    def verticalOrder(self, root: 'TreeNode') -> 'List[List[int]]':

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        this problem seemed very hard but actually once you draw a picture on a paper or in your brain, it becomes pretty clear.
        - for the left  node, you set its index as index - 1
        - for the right node, you set its index as index + 1
        - use queue to loop through all the nodes in a tree
        - set index as a key to the hashmap() and value as a list of vals
        - add node.data into hashmap() with index as a key
        - keep track of min and max index and store into solution list and return it
        """

        if not(root): return []
        
        res, MIN,MAX=[],0,0 # why keep track of min and max index (keep track how many columns of the tree in order to loop all index to get result)
        table={} # store as key is index and node value; same index append that node value
        queue=[(root,0)] # in order to pop to get tree node and node's index as the node has leafs
        
        while queue:
            
            node, index=queue.pop(0)
            #print(node)
            #print(index)
            if index not in table:
                table[index]=[node.val]
                #print(table)
            else:
                table[index].append(node.val)
            
            if node.left:
                MIN=min(MIN,index-1)
                queue.append((node.left,index-1))
            if node.right:
                MAX=max(MAX,index+1)
                queue.append((node.right,index+1))
                
        for i in range(MIN,MAX+1):
            #print(i)
            res.append(table[i])
        
        return res


