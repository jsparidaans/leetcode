from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ""
        for digit in digits:
            result += str(digit)
        return list(str(int(result)+1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().plusOne(digits=[9])
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
