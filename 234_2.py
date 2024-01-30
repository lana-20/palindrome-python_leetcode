# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        # find middle (alow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse 2nd half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check palindrome
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True

# Test Solution
solution = Solution()
print(solution.isPalindrome([1,2,2,1]))
print(solution.isPalindrome([1,2]))
