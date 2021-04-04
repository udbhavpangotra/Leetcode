# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, val=0, next=None):
        # self.val = val
        # self.next = next
class Solution:
    def swapPairs(self, oldHead: ListNode) -> ListNode:
        head = ListNode(-1)
        head.next = oldHead
        
        current = head
        while current is not None:
            nextNode = current.next
            
            if nextNode is None:
                break
            nextNextNode = nextNode.next
            if nextNextNode is None:
                break
            
            nextNode.next = nextNextNode.next
            nextNextNode.next = nextNode
            current.next = nextNextNode
            
            current = current.next
            
            if current is not None:
                current = current.next
            
        return head.next
            
            
            