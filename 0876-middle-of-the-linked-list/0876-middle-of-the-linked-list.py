# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middleNode = head
        currentLength = 0
        while head:
            head = head.next
            currentLength += 1
            if currentLength % 2 == 0:
                middleNode = middleNode.next
        return middleNode