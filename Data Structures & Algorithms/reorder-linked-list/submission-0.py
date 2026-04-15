# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        # 'second' starts after the middle; 'slow.next = None' cuts the list in two
        second = slow.next
        prev = slow.next = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 3. Merge (weave) the two halves
        # 'first' is the start of the 1st half, 'prev' is the start of the reversed 2nd half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
             
        