def isprime(n: int):
    if n <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime


class Solution:
    @staticmethod
    def countPrimeSetBits(left: int, right: int) -> int:
        counter = 0
        for num in range(left, right + 1):
            bit_count = num.bit_count()
            if isprime(bit_count):
                counter += 1
        return counter


print(Solution.countPrimeSetBits(6, 10)) # 4
