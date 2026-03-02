#solution 1: putting values in a sorted array
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = list1
        while current:
            values.append(current.val)
            current = current.next
        
        current = list2
        while current:
            values.append(current.val)
            current = current.next
        
        values.sort()

        dummy = ListNode(0, None) #dummy is 0 and points to none. the first element in the linked list
        tail = dummy # Now both variables point to the SAME node, tail will always point to the last node in the new list.
        for val in values:
            tail.next = ListNode(val)
            tail = tail.next
        
        return dummy.next
'''
Let:
n = length of list1
m = length of list2
Time Complexity:
1-Collecting values
O(n) for list1
O(m) for list2
Total so far: O(n + m)
2- Sorting the array
O((n + m) log(n + m))
This dominates the runtime.
3-Building the new linked list
O(n + m)
Total: O((n + m) log(n + m))

Space Complexity: 
O(n + m)

not optimal. will do optimal later ISA
'''