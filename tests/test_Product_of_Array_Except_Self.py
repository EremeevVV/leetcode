from src.Product_of_Array_Except_Self import Solution

def test_product1():
    nums = [1, 2, 3, 4]
    expected = [24,12,8,6]
    result = Solution().productExceptSelf(nums)
    assert result == expected


def test_product():
    nums = [-1,1,0,-3,3]
    expected = [0,0,9,0,0]
    result = Solution().productExceptSelf(nums)
    assert result == expected