# Solve the problem from the second set here
# Problem no 8
# Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2], for n > 2,
# larger than the given natural number n. (e.g. for n = 6, m = 8).

# Read the number n and verifies if it's greater or equal to 1
# If the number doesn't satisfy these conditions, the program will try to read another number until the conditions are
# satisfied
def read_number():
    n = int(input("Give the number > 2: "))
    while n <= 2:
        print("Incorrect number!\n")
        n = int(input("Give a number > 2: "))
        if n > 2:
            return n
    return n


#  Determine the smallest number m from the Fibonacci sequence greater than the given number n
def fibonacci(n):
    f1 = 0
    f2 = f3 = 1
    while f3 < n:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    if f3 == n:
        f3 = f1 + f2
    return f3


# Print the smallest number m from the Fibonacci sequence greater than the number n
def print_number(m):
    print(m)


# The main function
if __name__ == '__main__':
    n = read_number()
    print_number(fibonacci(n))
