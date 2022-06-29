from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:

        for idx, num in enumerate(nums):
            remainder = target - num
            print(remainder)
            res = self.search(remainder, nums, 0, len(nums))
            if res > 0:
                return [idx, res]

    def search(self, target: int, arr: List[int], low: int, high: int):
        if low > high:
            return -1
        else:
            mid = (low + high) // 2
            if target == arr[mid]:
                return mid
            elif target > arr[mid]:
                return self.search(target=target, arr=arr, low=mid + 1, high=high)
            else:
                return self.search(target=target, arr=arr, low=low, high=mid - 1)


if __name__ == '__main__':
    Solution().two_sum(nums=[2, 7, 11, 15], target=9)
