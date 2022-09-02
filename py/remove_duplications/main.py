import itertools
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for n, m in itertools.pairwise(nums):
            if n != m:
                nums[k] = m
                k += 1
        return k


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
