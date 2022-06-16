import cProfile

n = 50
primes = [2]
i = 1
while i < n:
    x = primes[-1]
    while True:
        for div in primes:
            if not x % div:
                break
        else:
            primes.append(x)
            break
        x += 1
    i += 1
print(primes[-1])


def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n
    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break
