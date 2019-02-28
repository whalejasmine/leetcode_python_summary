# Method 1 DFS iterative
#Time Complexity: O(N)O(N). We visit every node once.

# Space Complexity: O(N)O(N), the size of our implicit call stack during our depth-first search.

# Any path can be written as two arrows (in different directions) from some node, 
# where an arrow is a path that starts at some node and only travels down to child nodes.

# If we knew the maximum length arrows L, R for each child, then the best path touches L + R + 1 nodes.

# Algorithm

# Let's calculate the depth of a node in the usual way: max(depth of node.left, depth of node.right) + 1. 
# While we do, a path "through" this node uses 1 + (depth of node.left) + (depth of node.right) nodes. 
# Let's search each node and remember the highest number of nodes used in some path. The desired length is 1 minus this number.


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_length=0
        depth = {None:-1}
        stack = [(root,0)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited==0:
                stack.extend([(node,1),(node.left,0),(node.right,0)])
            else:
                left_d=depth[node.left]+1
                right_d=depth[node.right]+1
                depth[node]=max(left_d,right_d)
                max_length=max(max_length,left_d+right_d)
        return max_length

# Method 2 DFS recursive
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
