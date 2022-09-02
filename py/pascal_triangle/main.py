from typing import List


class Solution:
    def generate(self, num: int) -> List[List[int]]:
        triangle = []
        for i in range(num):
            triangle.append([])
            for j in range(i + 1):
                if i == j:
                    triangle[i].append(1)
                elif j == 0:
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        return triangle


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().generate(30)
    for cell in solution:
        print(cell)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
