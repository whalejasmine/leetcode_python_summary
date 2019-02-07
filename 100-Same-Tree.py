# Method 1 DFS recursive
# Time:  O(n)
# Space: O(logn)
#
# Given two binary trees, write a function to check if they are equal or not.
# 
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
    	# check both are empty trees
        if p is None and q is None:
            return True
        # check both node exit then check value
        if p is not None and q is not None:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        # otherwise neither node exits
        return False


if __name__ == "__main__":
    root1, root1.left, root1.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root2, root2.left, root2.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print (Solution1().isSameTree(root1, root2))


if __name__ == "__main__":
    root1, root1.left = TreeNode(1), TreeNode(2)
    root2, root2.right = TreeNode(1), TreeNode(2)
    print (Solution1().isSameTree(root1, root2))


# Method 2 DFS + stack
# Time:  O(n)
# Space: O(logn)
#
class Solution2:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        stack=[(p,q)]
        while stack:
            n1,n2=stack.pop()
            # n1 and n2 exit
            if n1 and n2 and n1.val==n2.val:
                stack.append((n1.right,n2.right))
                stack.append((n1.left,n2.left))
            # both n1 and n2 are none
            elif not n1 and not n2:
                continue
            # either node is none or value not same    
            else:
                return False
        return True # as stack pop to empty is true
if __name__ == "__main__":
    root1, root1.left = TreeNode(1), TreeNode(2)
    root2, root2.right = TreeNode(1), TreeNode(2)
    print (Solution2().isSameTree(root1, root2))

# Method 3 BFS + queue
# Time:  O(n) ??
# Space: O(logn)??

class Solution3:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
	    queue = [(p, q)]
	    while queue:
	        node1, node2 = queue.pop(0)
	        if not node1 and not node2:
	            continue
	        elif None in [node1, node2]:
	            return False
	        else:
	            if node1.val != node2.val:
	                return False
	            queue.append((node1.left, node2.left))
	            queue.append((node1.right, node2.right))
	    return True
if __name__ == "__main__":
    root1, root1.left = TreeNode(1), TreeNode(2)
    root2, root2.right = TreeNode(1), TreeNode(2)
    print (Solution3().isSameTree(root1, root2))
