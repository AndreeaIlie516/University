#
# Write the implementation for A2 in this file
#

# Sequence properties:
# 5. Real numbers.
# 9. Consecutive number pairs have equal sum. (e.g. 1+3i, 1-i, 1+3i, 1-i)


import math


# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities

# Read a complex number from the console
def read_complex_number():
    # Read real part and verify if it is a number
    real_part = input("The real part of the number is:")
    try:
        real_part = float(real_part)
    except:
        print('Not a valid number')
        return 0
    # If it is an integer, transform it into integer type
    if real_part == int(real_part):
        real_part = int(real_part)
    else:
        real_part = float(real_part)

    # Read imaginary part and verify if it is a number
    imaginary_part = input("The imaginary part of the number is:")
    try:
        imaginary_part = float(imaginary_part)
    except:
        print('Not a valid number')
        return 0
    # If it is an integer, transform it into integer type
    if imaginary_part == int(imaginary_part):
        imaginary_part = int(imaginary_part)
    return real_part, imaginary_part


# Read the list containing complex numbers
def read_list_of_numbers(list_of_complex_numbers):
    number_of_values = int(input("Number of values to introduce in the list of complex numbers:"))
    list = []
    for index in range(number_of_values):
        real_part, imaginary_part = read_complex_number()
        x = create_complex_number()
        set_real_part(x, real_part)
        set_imaginary_part(x, imaginary_part)
        list.append(x)
    list_of_complex_numbers += list


# Print a complex number in a complex form
def print_complex_number(real_part, imaginary_part):
    complex_number_to_print = ''
    has_real_part = 0

    # If the real part is different from 0
    if real_part != 0:
        complex_number_to_print = str(real_part)
        has_real_part = 1

    # If the real part is different from 0, print it in a complex form
    if imaginary_part != 0:
        if imaginary_part > 0:
            if has_real_part == 1:
                complex_number_to_print += '+'
            if imaginary_part == 1:
                complex_number_to_print += 'i'
            else:
                complex_number_to_print += str(imaginary_part)
                complex_number_to_print += 'i'
        elif imaginary_part == -1:
            complex_number_to_print += '-i'
        else:
            complex_number_to_print += str(imaginary_part)
            complex_number_to_print += 'i'
    elif has_real_part == 0:
        complex_number_to_print += '0'
    return complex_number_to_print


# Print the entire list containing complex numbers
def print_list(list_of_complex_numbers):
    index = 0
    for i in list_of_complex_numbers:
        # Print each complex number in a complex form
        real_part = get_real_part(i)
        imaginary_part = get_imaginary_part(i)
        complex_number = print_complex_number(real_part, imaginary_part)
        print(index, '.', complex_number)
        index += 1
    print('\n')


# Print a sequence having a given property
def print_sequence_with_property(start_of_sequence, end_of_sequence, list_of_complex_numbers):
    if start_of_sequence == -1:
        print("There are no numbers with this property")
    else:
        index = 0
        for i in list_of_complex_numbers:
            if start_of_sequence <= index <= end_of_sequence:
                # Print complex number in a complex form
                real_part = get_real_part(i)
                imaginary_part = get_imaginary_part(i)
                complex_number = print_complex_number(real_part, imaginary_part)
                print(index, '.', complex_number)
            index += 1
    print('\n')


# Print the menu
def print_menu():
    print("1. Read a list of complex numbers")
    print("2. Display the entire list of numbers")
    print("3. Display the longest sequence that consists of real numbers")
    print("4. Display the longest sequence that consists of consecutive number pairs having equal sum")
    print("5. Exit the application")


# Create the menu, which performs until the exit option is selected
def create_menu(list_of_complex_numbers):
    while True:
        print_menu()
        option = int(input('>'))
        if (option == 1):
            read_list_of_numbers(list_of_complex_numbers)
            print('\n')
        elif (option == 2):
            print_list(list_of_complex_numbers)
        elif (option == 3):
            start_of_sequence, end_of_sequence = find_sequence_property_5(list_of_complex_numbers)
            print_sequence_with_property(start_of_sequence, end_of_sequence, list_of_complex_numbers)
        elif (option == 4):
            start_of_sequence, end_of_sequence = find_sequence_property_9(list_of_complex_numbers)
            print_sequence_with_property(start_of_sequence, end_of_sequence, list_of_complex_numbers)
        elif (option == 5):
            print("You exited the application.")
            return 0
        else:
            print('Invalid number. Please select one of the five options!')


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

# Create a complex number
def create_complex_number(real_part=0, imaginary_part=0):
    return [real_part, imaginary_part]


# Get functions
def get_real_part(complex_number):
    return complex_number[0]


def get_imaginary_part(complex_number):
    return complex_number[1]


# Set functions
def set_real_part(complex_number, value):
    complex_number[0] = value


def set_imaginary_part(complex_number, value):
    complex_number[1] = value


# Verify if a number is real. If it is it returns 1 and 0 otherwise
def is_real(complex_number):
    if get_imaginary_part(complex_number) == 0:
        return 1
    return 0


# Find the maximum sequence having property no. 5 (The numbers are real)
def find_sequence_property_5(list_of_complex_numbers):
    start_of_sequence = end_of_sequence = -1
    max_length = -1
    length = 0
    start = -1
    index = 0
    for i in list_of_complex_numbers:
        if is_real(i) == 1:
            if length == 0:
                start = index
            length += 1
        elif length > max_length:
            max_length = length
            start_of_sequence = start
            length = 0
        index += 1
    if length > max_length:
        max_length = length
        start_of_sequence = start + 1
    end_of_sequence = start_of_sequence + max_length - 1
    return start_of_sequence, end_of_sequence


# Compute the sum of 2 complex numbers
def sum_of_consecutive_complex_numbers(real_part_1, imaginary_part_1, real_part_2, imaginary_part_2):
    return real_part_1 + real_part_2, imaginary_part_1 + imaginary_part_2


# Find the maximum sequence having property no. 8 (Consecutive number pairs have equal sum)
def find_sequence_property_9(list_of_complex_numbers):
    start_of_sequence = end_of_sequence = -1
    max_length = -1
    length = 0
    start = -1
    index = 0
    sum_real_1 = sum_real_2 = sum_imaginary_1 = sum_imaginary_2 = -math.inf
    length_of_list = len(list_of_complex_numbers)
    while index < length_of_list - 2:
        # Compute the sum of a pair of numbers
        real_part_1 = get_real_part(list_of_complex_numbers[index])
        imaginary_part_1 = get_imaginary_part(list_of_complex_numbers[index])
        real_part_2 = get_real_part(list_of_complex_numbers[index + 1])
        imaginary_part_2 = get_imaginary_part(list_of_complex_numbers[index + 1])
        sum_real_1, sum_imaginary_1 = sum_of_consecutive_complex_numbers(real_part_1, imaginary_part_1, real_part_2,
                                                                         imaginary_part_2)

        # Compute the sum of the nex pair of numbers
        real_part_1 = real_part_2
        imaginary_part_1 = imaginary_part_2
        real_part_2 = get_real_part(list_of_complex_numbers[index + 2])
        imaginary_part_2 = get_imaginary_part(list_of_complex_numbers[index + 2])
        sum_real_2, sum_imaginary_2 = sum_of_consecutive_complex_numbers(real_part_1, imaginary_part_1, real_part_2,
                                                                         imaginary_part_2)

        # Check if the sums are equal and find the maximum sequence
        if sum_real_1 == sum_real_2 and sum_imaginary_1 == sum_imaginary_2:
            if length == 0:
                length = 3
                start = index
            else:
                length += 1
        elif length > max_length:
            max_length = length
            start_of_sequence = start
            length = 0
        index += 1
    if length > max_length:
        max_length = length
        start_of_sequence = start
    end_of_sequence = start_of_sequence + max_length - 1
    return start_of_sequence, end_of_sequence


# The main function
if __name__ == '__main__':
    list_of_complex_numbers = [
        create_complex_number(7, 3),
        create_complex_number(2, 0),
        create_complex_number(0, 0),
        create_complex_number(8, 0),
        create_complex_number(-2, 16),
        create_complex_number(5, -9),
        create_complex_number(1, 3),
        create_complex_number(1, -1),
        create_complex_number(1, 3),
        create_complex_number(1, -1),
        create_complex_number(-2, 16),
        create_complex_number(2.3, 4),
        create_complex_number(-5, -6.3),
        create_complex_number(4.6, 5.2),
    ]
    create_menu(list_of_complex_numbers)
