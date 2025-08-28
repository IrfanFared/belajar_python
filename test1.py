# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


# Helper: Convert Python list -> Linked List
def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper: Convert Linked List -> Python list (to check result)
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Example usage:
list1 = build_linked_list([1,2,4])
list2 = build_linked_list([1,3,4])

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)

print(linked_list_to_list(merged))  # Output: [1, 1, 2, 3, 4, 4]
