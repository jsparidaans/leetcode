from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        values = {}
        for idx, i in enumerate(mat):
            count = 0
            for j in i:
                if j == 1:
                    count += 1
            values[idx] = count
        values = sorted(values.items(), key=lambda x: x[1])
        print(values)
        result = []
        for i in range(k):
            result.append(values[i][0])
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Solution().kWeakestRows(mat=[[1, 1, 0, 0, 0],
                                 [1, 1, 1, 1, 0],
                                 [1, 0, 0, 0, 0],
                                 [1, 1, 0, 0, 0],
                                 [1, 1, 1, 1, 1]],
                            k=3)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
