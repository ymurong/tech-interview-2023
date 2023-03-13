import pytest
from week1.n1_2sum import Solution as Solution1
from week1.n15_3sum import Solution as Solution15


def test_1_2sum():
    _test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]
    solution = Solution1()
    for nums, target, output in _test_cases:
        assert output == solution.two_sum_1(nums, target)
        assert output == solution.two_sum_2(nums, target)


def test_15_3sum():
    _test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]
    solution = Solution15()
    for nums, output in _test_cases:
        assert sorted(output) == sorted(solution.three_sum(nums))
