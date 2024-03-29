import random
import math
import time

# deterministic primality test (slow)
def deterministic_prime(n):
    if n < 2:
        return "Not prime"
    for i in range(2, int((n**0.5)+1)):
        if n % i == 0:
            return "Not prime"
    return "Prime"

# probabilistic primality test (faster)
def fermats_prime(n, k=5):
    if n < 2:
        return "Definitely not prime"
    # fermat's little theorem: a^(n-1) ≡ 1 (mod n)
    for _ in range(k):
        a = random.randint(1, n - 1)
        if pow(a, n - 1, n) != 1:
            return "Inconclusive - May not be prime"
    return "Probably prime"  # Indicate the probabilistic nature

prime = 56812873268878613693

start_time = time.time()
print(f"deterministic test of {prime}: {deterministic_prime(prime)}")
print(f"--- {time.time() - start_time} seconds ---")

start_time = time.time()
print(f"fermats test of {prime}: {fermats_prime(prime)}")
print(f"--- {time.time() - start_time} seconds ---")
