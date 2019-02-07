# Time:  O(n)
# Space: O(logn)
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more than 1.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
    	#store have been seen is 1, else 0 as stack
    	stack=[(0,root)]
    	#store node as key and depth on that node as dictionary
    	depth = {None:0}
    	while stack:

    		seen, node=stack.pop()
    		# no node continue
    		if node is None:
    			continue
    		# if seen is not none, append node and its children to the stack
    		if not seen:
    			stack.extend([(1,node),(0,node.right),(0,node,left)])
    		# otherwise ????
    		else:
    			if abs(depth[node.left]-depth[node.right]):
    				return False
    			depth[node]=max(depth[node.left],depth[node.right])+1
    

     	return True

class Solution2:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        return (self.getHeight(root)>=0)
    
    
    def getHeight(self,root):
        if root is None:
            return 0
        left_height,right_height=self.getHeight(root.left),self.getHeight(root.right)
        
        if left_height<0 or right_height<0 or abs(left_height-right_height)>1:
            return -1
        return max(left_height,right_height)+1


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    result = Solution().isBalanced(root)
    print result
    
    root.left.left = TreeNode(2)
    result = Solution().isBalanced(root)
    print result
