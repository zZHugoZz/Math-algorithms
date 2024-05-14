def is_prime(n: int) -> bool:
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(ceil: int) -> list[int]:
    primes = []
    for i in range(2, ceil + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def prime_decomposition(n: int) -> list[int]:
    primes = find_primes(math.floor(n))
    decomposition = []

    if n == 1:
        return [n]

    for prime in primes:
        while n % prime == 0:
            decomposition.append(prime)
            n /= prime
        if is_prime(n):
            decomposition.append(int(n))
            break

    return decomposition if len(decomposition) > 0 else [n]
