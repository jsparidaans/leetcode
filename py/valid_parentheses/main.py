class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for c in s:
            print(stack)
            if len(stack) > 0:
                if c in [')', '}', ']']:
                    if stack[-1] == '(' and c == ')':
                        stack.pop()
                    elif ord(c) - 2 == ord(stack[-1]):
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack) == 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().isValid("{{}[][[[]]]}")
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
