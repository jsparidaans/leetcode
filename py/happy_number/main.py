seen = []


class Solution:
    def isHappy(self, n: int) -> bool:
        # split up into digits
        digits = [int(a) for a in str(n)]

        # calculate sum of squares of digits
        sum_squares = sum([a ** 2 for a in digits])

        # if sum_squares is 1 return true else recurse until 1 is found or repetition occurs
        if sum_squares == 1:
            seen.clear()
            return True
        elif sum_squares in seen:
            return False
        else:
            seen.append(sum_squares)
            return self.isHappy(sum_squares)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().isHappy(13)
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
