class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        n = len(columnTitle) - 1
        for char in columnTitle:
            value = n * (ord(char) - ord('A') * 26)
            print(value)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().titleToNumber("ZY")
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
