class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, base=2) + int(b, base=2))[2:]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().addBinary(a="11", b="1")
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
