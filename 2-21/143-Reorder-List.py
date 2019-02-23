#Method 1 swap???? 
#Time O(n) 
#Space O(1) inplace

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: 'ListNode') -> 'None':
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # find the mid point
        slow = fast=head
        while fast and fast.next: #what does it have fast? meaning? why can find the middle
            slow=slow.next
            fast=fast.next.next
        
        # reverse the second half in place  1->2->3->4->5->6 to 1->2->3->6->5->4
        pre,node=None,slow
        
        while node:
            pre,node.next,node=node,pre,node.next
            
        # Merge in-place; Note : the last node of "first" and "second" are the same ;1->2->3->6->5->4 to 1->6->2->5->3->4
        first, second = head, pre
        while second.next:
            first.next, first=second,first.next
            second.next,second = first,second.next
        return