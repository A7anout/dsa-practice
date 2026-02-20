#solution 1: Iterative (two pointers)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None , head #none is null in python
        while curr: #means while curr pointer is not null meaning we haven't reached the end of the list yet
            temp = curr.next #after curr points to prev. prev is the new next so we need to save old next first
            curr.next = prev #the actual reversing
            prev = curr
            curr = temp
        return prev # at the end prev pointer will point to the end of the list
'''
Time Complexity: O(n)
Space Complexity: O(1)
explanation with example (3 nodes):
the first node (head) points to second node
second node points to third node (last) (tail)
last node points to NULL

so the idea is to make two pointers
the first pointer (called prev) points to NULL (think of it as before the first node)
first node will point to that null

the second pointer (called current) will point to current node
(the one we are we will change it's pointer from next node to prev)

we update both pointers by 1 after each loop

ex: 1 → 2 → 3 → 4 → None
the first goal is to make 1 point at none
Iteration 1:
prev = None
curr = 1
temp = 2
1 → None
prev = 1 → None
curr = 2 → 3 → 4 → None

the goal now is for 2 to point at 1
Iteration 2
prev = 1 → None
curr = 2 → 3 → 4 → None
temp = 3
2 → 1 → None
prev = 2 → 1 → None
curr = 3 → 4 → None

Iteration 3
temp = 4
3 → 2 → 1 → None
prev = 3 → 2 → 1 → None
curr = 4 → None

Iteration 4
temp = None
4 → 3 → 2 → 1 → None
prev = 4 → 3 → 2 → 1 → None
curr = None

basically flipping one arrow at a time until the entire list is reversed.
'''