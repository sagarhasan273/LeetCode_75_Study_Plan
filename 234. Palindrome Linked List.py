# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.forward = ''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        while head:
            self.forward = self.forward + str(head.val)
            head = head.next

        return self.forward == self.forward[::-1]