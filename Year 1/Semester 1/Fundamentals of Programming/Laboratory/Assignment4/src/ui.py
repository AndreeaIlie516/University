"""
  User interface module
"""

import functions


def print_error_valid_number():
    print('Not a valid number')


def print_error_complex_number():
    print('Not a complex number')


def print_error_relation():
    print("Not a valid relational operator")


def print_error_valid_position():
    print('Not a valid position')


def print_error_start_position():
    print("The start position is out of range")


def print_error_end_position():
    print("The end position is out of range")


def print_error_start_end_position():
    print("The start and end position are not put in a logical order")


def print_error_position_range():
    print("The position is out of range")


def print_error_not_existing_number():
    print("The number doesn't exist in the list")


def print_error_not_existing_real_number():
    print("There are no real number in the list")


def print_error_not_existing_modulo_number():
    print("There are no number with this modulo in the list")


def print_add_success(complex_number):
    real_part = functions.get_real_part(complex_number)
    imaginary_part = functions.get_imaginary_part(complex_number)
    complex_number = functions.create_complex_number_to_print(real_part, imaginary_part)
    print("You added", complex_number, "successfully!")


def print_insert_success(complex_number):
    real_part = functions.get_real_part(complex_number)
    imaginary_part = functions.get_imaginary_part(complex_number)
    complex_number = functions.create_complex_number_to_print(real_part, imaginary_part)
    print("You inserted", complex_number, "successfully!")


def print_remove_success():
    print("You removed the element(s) successfully!")


def print_replace_success():
    print("You replaced the element(s) successfully!")


def print_sum(real_part, imaginary_part):
    complex_number = functions.create_complex_number_to_print(real_part, imaginary_part)
    print("The sum is ", complex_number)


def print_product(real_part, imaginary_part):
    complex_number = functions.create_complex_number_to_print(real_part, imaginary_part)
    print("The product is ", complex_number)


def print_complex_number(complex_number):
    real_part = functions.get_real_part(complex_number)
    imaginary_part = functions.get_imaginary_part(complex_number)
    print(functions.create_complex_number_to_print(real_part, imaginary_part))


def print_filter_real_success():
    print("You filtered the real numbers successfully!")


def print_filter_modulo_success():
    print("You filtered the numbers by modulo successfully!")


def print_error_undo():
    print("You cannot perform undo operation anymore!")


def print_list(list_of_complex_numbers, start_position=0, end_position=0):
    """
    Print the entire list containing complex numbers
    :param list_of_complex_numbers: The list of complex numbers
    :param start_position: the start position for sequence
    :param end_position: the end position for the sequence
    :return:"
    """
    print("\nThe list is:")
    if end_position != 0:
        index = start_position
    else:
        index = 0
    for i in list_of_complex_numbers:
        # Print each complex number in a complex form
        if end_position != 0:
            if index <= end_position:
                real_part = functions.get_real_part(i)
                imaginary_part = functions.get_imaginary_part(i)
                complex_number = functions.create_complex_number_to_print(real_part, imaginary_part)
                print(complex_number)
                index += 1
        else:
            real_part = functions.get_real_part(i)
            imaginary_part = functions.get_imaginary_part(i)
            complex_number = functions.create_complex_number_to_print(real_part, imaginary_part)
            print(complex_number)
            index += 1
    print('\n')


def print_menu():
    """
    Print the menu
    :return:
    """
    print("(A) Add a number")
    print("\t add <number> -  Add a number")
    print("\t insert <number> at <position> - Insert a number at a specific position")
    print("(B) Modify numbers")
    print("\t remove <position> - Remove a number from a position")
    print("\t remove <start position> to <end position> - Remove the numbers in a range")
    print("\t replace <old number> with <new number> - Replace a number with a new one")
    print("(C) Display numbers having different properties")
    print("\t list - List the whole list")
    print("\t list real <start position> to <end position> - List the real numbers from the list in a range")
    print(
        "\t list modulo [ < | = | > ] <number> - List the number from the"
        " list having modulo with a property given (> = < number) ")
    print("(D) Obtain different characteristics of sub-lists")
    print("\t sum <start position> to <end position> - Compute the sum of numbers in a range")
    print("\t product <start position> to <end position> - Compute the product of numbers in a range")
    print("(E) Filter the list")
    print("\t filter real - Keep only real numbers in the list")
    print(
        "\t filter modulo [ < | = | > ] <number> - Keep only the numbers of the list with "
        "the modulo with a property given (> = < number) ")
    print("(F) Undo")
    print("\t undo - The last operation that modified program data is reversed")
    print("exit - Exit the application")
    print('\n')
