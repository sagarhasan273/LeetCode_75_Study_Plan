# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count_list = 0
        
        node = head
        while node:
            count_list +=1
            node = node.next
            
        pos = count_list-n
        
        if pos == 0:
            return head.next
        
        node = head
        
        for _ in range(1, pos):
            node = node.next

        node.next = node.next.next
        return head