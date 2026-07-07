class Solution:
    def sumAndMultiply(self, n: int) -> int:

        n = str(n)

        x = 0
        total = 0

        for i in range(len(n)):

            digit = int(n[i])

            if digit != 0:

                x = x * 10 + digit
                total += digit

        return x * total