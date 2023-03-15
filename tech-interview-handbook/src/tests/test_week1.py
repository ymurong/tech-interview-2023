import pytest
from week1.n1_2sum import Solution as Solution1
from week1.n15_3sum import Solution as Solution15
from week1.n217_contains_duplicate import Solution as Solution217
from week1.n121_best_time_buy_stock_sell_stock import Solution as Solution121
from week1.n238_product_of_array_except_self import Solution as Solution238


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


def test_217_contains_duplicate():
    _test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]
    solution = Solution217()
    for nums, output in _test_cases:
        assert output == solution.contains_duplicate(nums)


def test_121_best_time_buy_stock_sell_stock():
    _test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ]
    solution = Solution121()
    for nums, output in _test_cases:
        assert output == solution.max_profit(nums)


def test_238_product_of_array_except_self():
    _test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ]
    solution = Solution238()
    for nums, output in _test_cases:
        assert output == solution.productExceptSelf(nums)
