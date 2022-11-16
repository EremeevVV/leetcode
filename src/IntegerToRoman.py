# Не решил еще

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        digit = 0
        while num>0:
            digit = num % 10
            num //= 10
            for key in roman.keys():
                if digit > key-1:

            print(digit)