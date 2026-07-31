def find_factors(n):
    factors = list()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
    return factors

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_prime_factor(factors):
    pf = list()
    for n in factors:
        if is_prime(n):
            pf.append(n)
    return pf

def find_largest_prime_factor(prime_factors):
    return max(prime_factors)


if __name__ == "__main__":
    n = 600851475143
    factors = find_factors(n)
    prime_factors = find_prime_factor(factors)
    largest_prime_factor = find_largest_prime_factor(prime_factors)
    print(largest_prime_factor)
