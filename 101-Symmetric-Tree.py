# Time:  O(n)
# Space: O(logn)
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# 
# For example, this binary tree is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Iterative solution
class Solution1:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
    	# root is none
        if root is None:
            return True
        # stack
        stack=[]
        stack.append(root.left)
        stack.append(root.right)
        while stack:
        	# pop left and right
            p,q=stack.pop(),stack.pop()
            # value and structure same
            if p and q and p.val==q.val:
                stack.append(p.left)
                stack.append(q.right)
                stack.append(p.right)
                stack.append(q.left)
            # neither of p and q exits
            elif not p and not q:
                continue
            else:
                return False
        return True # stack is empty




# Recursive solution
class Solution2:
	
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        return self.isSymmetricRecu(root.left,root.right)

    def isSymmetricRecu(self,left,right):
        if not left and not right:
            return True
        
        if not left or not right or left.val!=right.val:
            return False
        return self.isSymmetricRecu(left.left,right.right) and self.isSymmetricRecu(left.right,right.left)    	



if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.left, root.right.right = TreeNode(3), TreeNode(3)
    root.left.right, root.right.left = TreeNode(4), TreeNode(4)
    print Solution1().isSymmetric(root)