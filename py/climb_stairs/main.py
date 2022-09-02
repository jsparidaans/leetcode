class Solution:
    def climbStairs(self, n: int) -> int:


        if n > 2:
            steps = [0] * (n+1)
            steps[1], steps[2] = 1, 2
            for num in range(3, n+1):
                steps[num] = steps[num - 1] + steps[num - 2]
            return steps[n]
        return n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().climbStairs(40)
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
