import math

def main():
    n = int(input())
    print (is_prime(n))


def is_prime(n):
    if n == 2:
        return "composite"
    if n % 2 == 0 or n <= 1:
        return "prime"

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return "prime"
    return "composite"

main()
