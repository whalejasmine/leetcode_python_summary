# Method 1 BF
# Intuition & Algorithm

# Traverse all the linked lists and collect the values of the nodes into an array.
# Sort and iterate over this array to get the proper value of nodes.
# Create a new sorted linked list and extend it with the new nodes.
# Time complexity : O(NlogN) where N is the total number of nodes.

# Collecting all the values costs O(N) time.
# A stable sorting algorithm costs O(NlogN) time.
# Iterating for creating the linked list costs O(N) time.
# Space complexity : O(N).

# Sorting cost O(N) space (depends on the algorithm you choose).
# Creating a new linked list costs O(N) space. 

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes=[]
        head=point=ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l=l.next
        for x in sorted(self.nodes):
            point.next=ListNode(x)
            point=point.next
        return head.next

# Method 2 priority queue
# Time: O(Nlogk)
# The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. 
# But finding the node with the smallest value just costs O(1) time.
# There are N nodes in the final linked list.
# Space:O(k)
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """


        head=point=ListNode(0)
        q=PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val,l))
        while not q.empty():
            val,node=q.get()
            point.next=ListNode(val)
            point=point.next
            node=node.next
            if node:
                q.put((node.val,node))
        return head.next        
