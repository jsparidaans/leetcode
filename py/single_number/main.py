from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            if num not in hash.keys():
                hash[num] = 1
            else:
                hash[num] = hash[num] + 1
        return min(hash, key=hash.get)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().singleNumber([2, 2, 1])
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
