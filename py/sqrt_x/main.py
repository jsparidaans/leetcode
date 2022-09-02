class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if (mid * mid) > x:
                right = mid - 1
            elif (mid * mid) < x:
                left = mid + 1
            else:
                return mid
        return right


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().mySqrt(x=8)
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
