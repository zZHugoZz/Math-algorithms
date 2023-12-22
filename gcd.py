def gcd(n1: int, n2: int) -> int:
    n1, n2 = n2 if n2 > n1 else n1, n1 if n2 > n1 else n2
    while n1 > 0 and n2 > 0:
        new_n1 = n2
        new_n2 = n1 % n2
        n1, n2 = new_n1, new_n2
    return n1
