def is_prime(num=0):
    c = 0
    for i in range(1, 10000):
        if num % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False


def prime_generator(limit=100000):
    primes = []
    for i in range(1, 10000):
        if is_prime(i):
            primes.append(i)

    return primes[-1]


print(prime_generator())
