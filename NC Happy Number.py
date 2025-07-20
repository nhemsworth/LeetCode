class Solution:
    def isHappy(self, n: int) -> bool:

        def calculate_number(n: int):

            num = n
            sum_n = 0
            while num > 0:
                sum_n += (num % 10)**2
                num = num // 10

            return sum_n

        num_set = set()

        while True:
            num_set.add(n)
            n = calculate_number(n)

            if n == 1:
                return True
            elif n in num_set:
                return False


sol = Solution()
print(sol.isHappy(19))
