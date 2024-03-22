def prime_generator(limit=1000):
    counter = 0
    primes = []
    for i in range(1, limit):
        counter = 0
        for j in range(1, limit):
            if i % j == 0:
                counter += 1
        if counter == 2:
            primes.append(i)
    return primes


def factorer(num=1):
    primes = prime_generator(1000)
    factors = []
    for i in range(0, len(primes)):
        for j in range(0, len(primes)):
            if num % primes[i] == 0:
                num = num / primes[i]
                factors.append(primes[i])
    return factors


def mmc():
    primes = [2, 3, 5, 7, 9, 11, 13, 17, 19]
    print(2*3*5*7*9*11*13*17*19)


mmc()

