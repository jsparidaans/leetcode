from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(a) for a in accounts])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().maximumWealth([[2,8,7],[7,1,3],[1,9,5]])
    print(solution)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
