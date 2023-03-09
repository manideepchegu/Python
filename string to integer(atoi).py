class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        sign = 1
        result = 0
        while i < len(str) and str[i].isspace():
            i += 1
        if i < len(str) and (str[i] == "+" or str[i] == "-"):
            if str[i] == "-":
                sign = -1
            i += 1
        while i < len(str) and str[i].isdigit():
            result = result * 10 + int(str[i])
            i += 1
        result *= sign
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result

