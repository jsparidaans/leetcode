class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().hammingWeight(0b00000000000000000000000010000000)
    print(solution)
