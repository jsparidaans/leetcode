import math


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        n = columnNumber
        while n > 0:
            char = chr(ord('A') + (n - 1) % 26)
            result.insert(0, char)
            n = (n - 1) // 26
        return "".join(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().convertToTitle(29)
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
