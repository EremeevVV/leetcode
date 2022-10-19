import re
from operator import mul,add,sub,floordiv

class Solution:
    """Given a string s which represents an expression, evaluate this expression and return its value.
    The integer division should truncate toward zero.
    You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval()."""
    def calculate(self, s: str) -> int:
        operator_index_dict = {'+':add, '-':sub, '*':mul, '/':floordiv}
        digits_str = re.findall(r'\d+',s)
        operators = re.findall(r'[\+\-\*/]',s)
        for ind in range(len(operators)):
            if operators[ind] =='*':
                digits_str.insert(ind,int(digits_str.pop(ind)) * int(digits_str.pop(ind)))
                operators.pop(ind)
        for ind in range(len(operators)):
            if operators[ind] == '/':
                digits_str.insert(ind,int(digits_str.pop(ind)) // int(digits_str.pop(ind)))
                operators.pop(ind)
        for ind in range(len(operators)):
            if operators[ind] == '+':
                digits_str.insert(ind,int(digits_str.pop(ind)) + int(digits_str.pop(ind)))
                operators.pop(ind)
        for ind in range(len(operators)):
            if operators[ind] == '-':
                digits_str.insert(ind,int(digits_str.pop(ind)) + int(digits_str.pop(ind)))
                operators.pop(ind)
        return digits_str[0]