from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().isPalindrome(head=[1, 2, 2, 1])
    print(solution)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
