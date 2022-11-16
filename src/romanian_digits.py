# not optimal
class Solution:

    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for ind in range(len(s)-1):
            if roman[s[ind]] < roman[s[ind+1]]:
                result -= roman[s[ind]]
            else:
                result += roman[s[ind]]
        return result + roman[s[-1]]

