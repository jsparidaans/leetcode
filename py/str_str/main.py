class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().strStr(haystack="hello", needle="lo")
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
