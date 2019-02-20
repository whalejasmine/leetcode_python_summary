# Method1 iterative
# Time: O(n)
# Space: O(n)

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        paths = []
        #stack (node,current path)
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            # if node is leaf, update the list of all paths
            if not node.left and not node.right:
                paths.append(path)
            #if node is not leaf
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        
        return paths




# Method2 recursion
# Time: O(n) visit n nodes
# Space: O(n); balanced O(logn)


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path =[]
        paths = []
        def dfs(root):
            if root:
                path.append(str(root.val))
                if root.left == None and root.right == None:
                    paths.append('->'.join(path))
                dfs(root.left)
                dfs(root.right)
                path.pop()
        dfs(root)
        return paths

        return paths