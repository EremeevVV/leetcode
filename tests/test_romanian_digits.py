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


def test_decrised_syms():
    special = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    sol = Solution()
    assert sol.decrised_symbols() == special


if __name__ == '__main__':
    test_romanToInt()
