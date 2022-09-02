class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words = list(filter(lambda x: x != "", words))
        return len(words[len(words)-1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().lengthOfLastWord("Hello World     ")
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
