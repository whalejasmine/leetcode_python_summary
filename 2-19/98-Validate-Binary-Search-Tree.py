#Method 1 DFS iterative
#Time O(n)
#Space O(n)

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:

# Input:
#     2
#    / \
#   1   3
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#              is 5 but its right child's value is 4.

# On the first sight, the problem is trivial. 
# Let's traverse the tree and check at each step if node.right.val > node.val and node.left.val < node.val. This approach would even work for some trees 
# The problem is this approach will not work for all cases. Not only the right child should be larger than the node but all the elements in the right subtree. 
# That means one should keep both upper and lower limits for each node while traversing the tree, and compare the node value not with children values but with these limits. 

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        
        stack=[(root,None,None)]
        while stack:
            root, lower_limit, upper_limit = stack.pop()

            if root.right:
                if root.right.val > root.val:
                    if upper_limit and root.right.val >= upper_limit:
                        return False
                    stack.append((root.right, root.val, upper_limit))
                else:
                    return False
            if root.left:
                if root.left.val < root.val:
                    if lower_limit and root.left.val <= lower_limit:
                        return False
                    stack.append((root.left,lower_limit,root.val))
                else:
                    return False
        return True  

#[5,1,6,4,7]

#Method 2 Inorder
#Time O(n) in the worst case when the tree is BST or the "bad" element is a rightmost leaf
#Space O(n)

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        stack,inorder=[],float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <=inorder:
                return False
            inorder=root.val
            root=root.right
        return True

