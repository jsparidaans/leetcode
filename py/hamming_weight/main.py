class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(str(bin(n)).replace("0b", "").replace("0", ""))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().hammingWeight(0b00000000000000000000000010000000)
    print(solution)
