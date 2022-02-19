# Solve the problem from the third set here
# Problem no 13
# Determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,... obtained from the sequence of natural numbers
# by replacing composed numbers with their prime divisors, without memorizing the elements of the sequence.

# Example:
# | 1 | 2 | 3 | 2 | 5 | 2 | 3 | 7 | 2 | 3 | 2 | 5 | 11 | 2 | 3 | 13 | 2 | 7 | 15 |
#   1   2   3   4   5   6   7   8   9  10  11  12   13  14  15   16  17  18   19

# Read the number n and verifies if it's greater or equal to 1
# If the number doesn't satisfy these conditions, the program will try to read another number until the conditions are
# satisfied
def read_number():
    n = int(input("Give the number >= 1: "))
    while n < 1:
        print("Incorrect number!\n")
        n = int(input("Give a number >= 1: "))
        if n >= 1:
            return n
    return n


# Verifies if the number given as a parameter is a prime number and return 1, or return 0 otherwise
def is_prime(number_to_check):
    if number_to_check < 2:
        return 0
    for i in range(2, number_to_check // 2 + 1):
        if number_to_check % i == 0:
            return 0
    return 1


# Searches for the prime divisors of the element and, if the index corresponding to that divisor is equal to the index
# of the element we are looking for, then the function will return that divisor.
# Otherwise, it will return 0. Also, it increases the index depending on the number of the prime divisors and returns it
def prime_divisor(element_of_array, index, index_of_element):
    number_of_prime_divisors = 0  # counts the number of prime divisors of the number ElementOfArray
    for possible_divisor in range(2,
                                  element_of_array // 2 + 1):  # searches for the possible prime divisors of the number
        if element_of_array % possible_divisor == 0:  # if finding a divisor
            number_of_prime_divisors += 1  # increases the variable counting the number of prime divisors
            if number_of_prime_divisors > 1:  # if it's not the first prime divisor
                index += 1  # goes to the next position in the array
            if index == index_of_element:  # if the prime divisor is in the position we are looking for
                return index, possible_divisor  # returns the index and the value of the element
            while element_of_array % possible_divisor == 0:
                element_of_array /= possible_divisor
    return index, 0  # returns the index in the array and 0 because the founded prime divisors aren't in the position
    # we are looking for


def find_element(index_of_element):
    if index_of_element == 1:  # if the position we are looking for is 1, then it returns 1
        return 1
    element_of_array = 2  # counts the original numbers of the sequence (1,2,3,4,5,6,7,8..), starting from 2
    index = 2  # the index for the elements in the 'constructed' array
    while index <= index_of_element:
        if is_prime(element_of_array) == 0:  # verifies if the original number in the sequence has prime divisors
            index, divisor = prime_divisor(element_of_array, index, index_of_element)
            if divisor > 0:  # if the function finds out a prime divisor in the position we are looking for, then it
                # will return the divisor
                return divisor
        else:
            if index == index_of_element:  # if the element is prime, and it is in the position we are looking for,
                # then it will return the element
                return element_of_array
        element_of_array += 1
        index += 1
    return element_of_array


# The main function
if __name__ == '__main__':
    n = read_number()
    print(find_element(n))
