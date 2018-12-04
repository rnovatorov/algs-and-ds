from itertools import count


def generate_primes():
    primes = [2]
    yield 2

    for n in count(3, 2):
        if all(n % p for p in primes):
            primes.append(n)
            yield n
