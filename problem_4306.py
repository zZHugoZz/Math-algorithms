import math


def greatest_odd_divider(n: int) -> int:
    dividers = []
    for i in range (1, math.ceil(n/2) + 1):
        if n % i == 0 and i % 2 != 0:
            dividers.append(i)
    return max(dividers)


def f(n: int) -> int:
    if n % 2 == 0:
        return int(n/2 + n/greatest_odd_divider(n))
    return int(2**((n+1)/2))


def suite(length: int) -> dict[int, int]:
    terms = [1]
    for i in range(length):
        next_term = f(terms[i])
        terms.append(next_term)
    return {i+1: term for i, term in enumerate(terms)}
