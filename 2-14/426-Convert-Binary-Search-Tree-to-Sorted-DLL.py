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


# Method 2  DFS recursive 
# Time:  O(V+E) c is total content of words
# Space: O(V)
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        head, tail = self.get_linked_list(root)
        head.left = tail
        tail.right = head
        return head
    
    def get_linked_list(self, node):
        ''' Helper function to turn subtree starting at node into linked list. 
        Returns (head, tail) of the linked list.
        '''
        
        # if node has no children, both the head and the tail is itself.
        if not node.left and not node.right:
            return (node, node)
        
        # if a node has a left child, linked list starting at left subtree is predecessor of node.
        # otherwise, the head of the linked list at node is itself.
        lhead, ltail = self.get_linked_list(node.left) if node.left else (node, None)
        
        # if a node has a right child, linked list starting at right subtree is successor of node.
        # otherwise, the tail of the linked list at node is itself.
        rhead, rtail = self.get_linked_list(node.right) if node.right else (None, node)
        
        # perform the correct connections
        node.left, node.right = ltail, rhead
        if ltail:
            ltail.right = node
        if rhead:
            rhead.left = node
            
        # return the head and tail of the linked list with node as the root.
        return (lhead, rtail)


