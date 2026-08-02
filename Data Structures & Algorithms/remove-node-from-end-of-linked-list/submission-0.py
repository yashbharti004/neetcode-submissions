# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            N+=1
            curr = curr.next
        
        Index = N - n
        if Index == 0:
            return head.next
        curr = head
        for i in range(N-1):
            if (i + 1) == Index:
                curr.next = curr.next.next
                print(curr.val)
            curr = curr.next
        return head
