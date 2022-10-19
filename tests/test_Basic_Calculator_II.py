from src.Basic_Calculator_II import Solution

def test_read():
    s = "32+21*2/ 1"
    result = Solution().calculate(s)
    print(result)

def test1():
    s = "3+2*2"
    expected= 7
    result = Solution().calculate(s)
    assert result == expected

def test2():
    s = " 3/2 "
    expected= 1
    result = Solution().calculate(s)
    assert result == expected

def test3():
    s = " 3+5 / 2 "
    expected = 5
    result = Solution().calculate(s)
    assert result == expected