from more_itertools import take

from src.algs.primes_generation import generate_primes


def test_primes_generation():
    primes = generate_primes()
    assert take(5, primes) == [2, 3, 5, 7, 11]
