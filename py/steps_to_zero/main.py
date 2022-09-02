class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            num = (num / 2) if num % 2 == 0 else (num - 1)
            steps += 1
        return steps


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().numberOfSteps(123)
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
