# Solve the problem from the first set here
# Problem no 2
# Given natural number n, determine the prime numbers p1 and p2 such that n = p1 + p2 (check the Goldbach hypothesis).


# Read the number n and verifies if it satisfies Goldbach Theorem conditions(it is an even number, and it is greater
# than 2
# If the number doesn't satisfy these conditions, the program will try to read another number until the conditions
# are satisfied
def read_number():
    n = int(input("Give an even number >2: "))
    while n <= 2 or n % 2 == 1:
        print("Incorrect number!\n")
        n = int(input("Give an even number >2: "))
        if n > 2 and n % 2 == 0:
            return n
    return n


# Verifies if the number given as a parameter is a prime number and return 1, or return 0 otherwise
def is_prime(x):
    if x < 2:
        return 0
    i = 2
    while i <= x // 2:
        if x % i == 0:
            return 0
        i += 1
    return 1


# Resolves the Goldbach theorem
# Goldbach theorem: Every even integer greater than 2 can be expressed as the sum of two primes.
def goldbach(n):
    i = 2
    j = n - i
    while j >= 2:
        if is_prime(i) and is_prime(j):
            print_numbers(i, j)
            break
        i += 1
        j -= 1


# Print the prime numbers obtained by using the Goldbach theorem
def print_numbers(n1, n2):
    print(n1, ' ', n2, '\n')


# The main function
if __name__ == '__main__':
    n = read_number()
    goldbach(n)
