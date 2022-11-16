from src.romanian_digits import Solution

def test_romanToInt():
    test_cases = {
        "III":3,
        "LVIII":58,
        "XLIV":44,
        "MCMXCIV":1994,
    }
    sol = Solution()
    for key,val in test_cases.items():
        assert sol.romanToInt(key) == val
