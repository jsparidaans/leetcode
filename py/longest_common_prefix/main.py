from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            temp = ""
            for idx, letter in enumerate(prefix):
                if idx + 1 > len(word):
                    break
                if letter == word[idx]:
                    temp += letter
                else:
                    break
            prefix = temp
        return prefix


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().longestCommonPrefix(["flower", "flow", "flight"])
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
