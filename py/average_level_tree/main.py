# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().averageOfLevels(TreeNode())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
