class Solution:
    def reverseBits(self, n: int) -> int:
        string = str(bin(n)).replace('0b', '')
        result = ""
        i = len(string) - 1
        while i >= 0:
            result += string[i]
            i -= 1
        i = len(result)
        while i < 32:
            result += "0"
            i += 1
        return int(result, base=2)


if __name__ == '__main__':
    solution = Solution().reverseBits(n=0b00000010100101000001111010011100)
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
