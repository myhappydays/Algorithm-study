def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

min_input_number = int(input())
max_input_number = int(input())

primes = [num for num in range(min_input_number, max_input_number + 1) if is_prime(num)]

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
