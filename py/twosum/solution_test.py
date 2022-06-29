import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_first_example(self):
        solution = Solution().two_sum(nums=[2, 7, 11, 15], target=9)
        self.assertEqual(solution, [0, 1])

    def test_second_example(self):
        solution = Solution().two_sum(nums=[3, 2, 4], target=6)
        self.assertEqual(solution, [1, 2])

    def test_third_example(self):
        solution = Solution().two_sum(nums=[3, 3], target=6)
        self.assertEqual(solution, [0, 1])


if __name__ == '__main__':
    unittest.main()
