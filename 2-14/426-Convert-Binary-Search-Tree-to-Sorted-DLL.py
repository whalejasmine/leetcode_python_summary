# Method 1  DFS inorder 
# Time:  O(V+E) c is total content of words
# Space: O(V)

# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return
        dummy=Node(0,None,None)
        prev=dummy
        stack,node=[],root
        while stack or node:
            # as node is not leaf
            while node:
                stack.append(node)
                #print(node.val)
                #append left most leaf and then right
                node=node.left
                #print(node.val)

            node=stack.pop()
            #create double link and then traverse to to next node (assign prev =node)
            node.left,prev.right,prev=prev,node,node
            #traverse to right
            node=node.right
        #use dummy . to link all
        dummy.right.left,prev.right=prev,dummy.right#????
        return dummy.right