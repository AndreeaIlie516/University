"""
  Program functionalities module
"""

import ui


def create_complex_number(real_part=0, imaginary_part=0):
    """
    Create a complex number
    :param real_part: The real part of the number
    :param imaginary_part: The imaginary part of the number
    :return: The complex number created (list)
    """
    return [real_part, imaginary_part]


def get_real_part(complex_number):
    """
    Get real part of a complex number
    :param complex_number: The complex number (list)
    :return: The real part of the complex number
    """
    return complex_number[0]


def get_imaginary_part(complex_number):
    """
    Get imaginary part of a complex number
    :param complex_number: The complex number (list)
    :return: The imaginary part of the complex number
    """
    return complex_number[1]


def get_modulo(complex_number):
    """
    Get modulo of a complex number function
    :param complex_number: The complex number
    :return:
    """
    real_part = get_real_part(complex_number)
    imaginary_part = get_imaginary_part(complex_number)
    modulo = real_part * real_part + imaginary_part * imaginary_part
    return modulo


def set_real_part(complex_number, value):
    """
    Set the real part to a complex number function
    :param complex_number: number to set the real part
    :param value: the value of the real part
    :return: the complex number set
    """
    complex_number[0] = value
    return complex_number


def set_imaginary_part(complex_number, value):
    """
    Set the imaginary part to a complex number function
    :param complex_number: number to set the imaginary part
    :param value: the value of the imaginary part
    :return: the complex number set
    """
    complex_number[1] = value
    return complex_number


def split_command_params(user_input):
    """
    Split the command parameters into commands(words) and parameters(numbers)
    :param user_input: The string given as input by the user
    :return: cmd_word - The input split into commands(words)
            cmd_param - The input split into parameters(numbers)
    """
    user_input = user_input.strip()
    cmd_word = []
    cmd_param = []
    index = 0
    tokens = user_input.split()
    length = len(tokens)
    if length > 0:
        cmd_word.append(tokens[index].lower())  # the first value has to be a command
        index += 1
    else:
        cmd_word = None
    if length > 1:
        if tokens[index].isalpha() == 1:  # check if the next value is a command(word)
            cmd_word.append(tokens[index].lower())
            index += 1
        if length > index:
            while index < length:
                if tokens[index] == '<' or tokens[index] == '=' or tokens[index] == '>':
                    # check for a relational character
                    cmd_param.append(tokens[index].lower())
                if tokens[index][0].isdigit() == 1 or tokens[index][0] == '-':  # check for a number
                    cmd_param.append(tokens[index].lower())
                else:
                    if index == 1:
                        cmd_param.append('error_complex_number')
                index += 1
        else:
            cmd_param = None
    else:
        cmd_param = None
    if cmd_word is not None:
        # transform the commands back into a string instead of a list
        cmd_word = ' '.join(cmd_word)
        cmd_word = cmd_word.lower()
    return cmd_word, cmd_param


def extract_complex_number_from_string(complex_number):
    """
    Function to extract a complex number from a string
    :param complex_number: A complex number given as a string
    :return: real_part - the real part of the complex number(int)
             imaginary_part - the imaginary part of the complex number(int)
    """
    is_negative_real = 0
    is_negative_imag = 0
    has_real_part = 1
    real_part = 0
    index = 0
    if complex_number[index] == '-':  # check if the real part is a negative number or not
        complex_number = complex_number[1:]
        if '+' in complex_number or '-' in complex_number:  # check if the imaginary part is a negative number or not
            is_negative_real = 1
        elif 'i' in complex_number:
            is_negative_imag = 1
        else:
            is_negative_real = 1
    complex_number = complex_number.strip()
    tokens = complex_number.split(' ')
    # split the real part and the imaginary part
    if '+' in complex_number:
        tokens = complex_number.split('+')
    elif '-' in complex_number:
        tokens = complex_number.split('-')
        is_negative_imag = 1
    # check if the number is complex or not
    elif 'i' in complex_number:
        has_real_part = 0
        real_part = 0
    # create real part or print error message if not possible
    if has_real_part == 1:
        real_part = tokens[index]
        index += 1
        try:
            real_part = int(real_part)
        except:
            ui.print_error_valid_number()
            return "error_valid_number"
        if is_negative_real == 1:
            real_part *= (-1)
    # create imaginary part or print error message if not possible
    try:
        imaginary_part = tokens[index]
        if imaginary_part != 0:
            if imaginary_part[len(imaginary_part) - 1:] != 'i':
                ui.print_error_complex_number()
                return "error_complex_number"
            imaginary_part = imaginary_part.replace('i', '')
    except:
        imaginary_part = 0
    try:
        imaginary_part = int(imaginary_part)
    except:
        ui.print_error_valid_number()
        return "error_valid_number"
    if is_negative_imag == 1:
        imaginary_part *= (-1)
    return real_part, imaginary_part


def extract_complex_number_from_param(cmd_param):
    """
    Extract a complex number from a parameter by extracting it from a string
    :param cmd_param: The complex number given as a parameter(string)
    :return: complex_number - The complex number or error message if not possible
    """
    cmd_param = ''.join(cmd_param)
    cmd_param = cmd_param.lower()
    try:
        complex_number = extract_complex_number_from_string(cmd_param)
        return complex_number
    except:
        ui.print_error_valid_number()
        return "error_valid_number"


def extract_numbers_from_param(cmd_param):
    """
    Extract two complex numbers from a parameter
    :param cmd_param: The complex numbers given as one parameter
    :return: The two complex numbers or error messages if not possible
    """
    number1 = cmd_param[len(cmd_param) - 2]
    number2 = cmd_param[len(cmd_param) - 1]
    number1 = extract_complex_number_from_param(number1)
    number2 = extract_complex_number_from_param(number2)
    if number1 != "error_valid_number" and number1 != "error_complex_number":
        if number2 != "error_valid_number" and number2 != "error_complex_number":
            return number1, number2
    return "error", "error"


def validate_position(position, length):
    """
    Validate a position by checking if it is a positive integer and it is > 0 and < length of the string
    :param position: the position to be validated
    :param length: the length of the list
    :return: 1 - if the position is good
             error message - otherwise
    """
    try:
        position = int(position)
    except:
        ui.print_error_valid_position()
        return "error_valid_position"
    if 0 > position or position >= length:
        ui.print_error_position_range()
        return "error_position_range"
    return 1


def validate_positions(start_position, end_position, length):
    """
    Validate two positions by checking if they are positive integers and they are  >0 and < length of the string
    and start poaition < end position
    :param start_position: the start position to be validated
    :param end_position: the end position to be validated
    :param length: the length of the list
    :return: 1 - if the positions are good
             error message - otherwise
    """
    try:
        start_position = int(start_position)
    except:
        ui.print_error_valid_position()
        return "error_valid_position"
    try:
        end_position = int(end_position)
    except:
        ui.print_error_valid_position()
        return "error_valid_position"
    if start_position > end_position:
        ui.print_error_start_end_position()
        return "error_start_end_position"
    if 0 > start_position or start_position >= length:
        ui.print_error_start_position()
        return "error_start_position"
    if 0 > end_position or end_position >= length:
        ui.print_error_end_position()
        return "error_end_position"
    return 1


def validate_position_insert(position, length):
    """
    Validate a position for inserting by checking if it is a positive integer and it is > 0 and <= length of the string
    :param position: the position to be validated
    :param length: the length of the list
    :return: 1 - if the position is good
             error message - otherwise
    """
    try:
        position = int(position)
    except:
        ui.print_error_valid_position()
        return "error_valid_position"
    if 0 > position or position > length + 1:
        ui.print_error_position_range()
        return "error_position_range"
    return 1


def extract_position_from_param(cmd_param, length):
    """
    Function to extract a position from a parameter
    :param cmd_param: The position given as a parameter
    :param length: The length of the list
    :return: The position extracted if possible(int) or an error message
    """
    cmd_param = ''.join(cmd_param)
    try:
        position = int(cmd_param)
        return position
    except:
        return "error_valid_position"


def extract_positions_from_param(cmd_param, length):
    """
    Function to extract two positions from a parameter
    :param cmd_param: The positions given as a parameter
    :param length: The length of the list
    :return: The positions extracted if possible(int) or an error message
    """
    try:
        start_position = cmd_param[len(cmd_param) - 2]
        end_position = cmd_param[len(cmd_param) - 1]
        start_position = int(start_position)
        end_position = int(end_position)
        return start_position, end_position
    except:
        return "error_valid_position", "error_valid_position"


def extract_relation_from_param(cmd_param):
    """
    Function to extract a comparison relation from a parameter
    :param cmd_param: The relation given as a parameter
    :return: The relation extracted if possible(char) or an error message
    """
    relation = cmd_param[len(cmd_param) - 2]
    try:
        number_to_compare = int(cmd_param[len(cmd_param) - 1])
    except:
        ui.print_error_valid_number()
        return "error_valid_number"
    if number_to_compare != abs(number_to_compare):
        ui.print_error_valid_number()
        return "error_valid_number"
    if relation not in "<>=":
        ui.print_error_relation()
        return "error_valid_relation"
    return relation, number_to_compare


def create_complex_number_to_print(real_part, imaginary_part):
    """
    Create a printing complex number in a complex form
    :param real_part: The real part of the number (int)
    :param imaginary_part: The imaginary part of the number (int)
    :return: The complex number as a string to be printed
    """
    try:
        real_part = int(real_part)
    except:
        return "error_valid_number"
    try:
        imaginary_part = int(imaginary_part)
    except:
        return "error_valid_number"
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


def add_complex_number_to_list(history, complex_number, list_of_complex_numbers):
    """
    Add a complex number to the list
    :param history: The history list of the  changes in the list of complex numbers
    :param complex_number: The complex number to be added
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the addition
    """
    if "error" not in complex_number:  # if valid number
        real_part = get_real_part(complex_number)
        imaginary_part = get_imaginary_part(complex_number)
        x = create_complex_number()

        set_real_part(x, real_part)
        set_imaginary_part(x, imaginary_part)
        add_list_to_history(history, list_of_complex_numbers)
        list_of_complex_numbers.append(x)
    return list_of_complex_numbers


def insert_complex_number_to_list(history, complex_number, position, list_of_complex_numbers):
    """
    Insert a complex number to the list
    :param history: The history list of the  changes in the list of complex numbers
    :param complex_number: The complex number to be inserted
    :param position: The position in which the complex number has to be inserted
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the insertion
    """
    message = "ok"
    if "error" not in complex_number:
        if validate_position_insert(position, len(list_of_complex_numbers)) == 1:
            add_list_to_history(history, list_of_complex_numbers)
            list_of_complex_numbers.insert(position, complex_number)
        else:
            message = "error"
    else:
        message = "error"
    return list_of_complex_numbers, message


def remove_position_from_list(history, position, list_of_complex_numbers):
    """
    Remove a complex number from a position in the list
    :param history: The history list of the  changes in the list of complex numbers
    :param position: The position from which the complex number has to be removed
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the removing
    """
    if validate_position(position, len(list_of_complex_numbers)) == 1:
        add_list_to_history(history, list_of_complex_numbers)
        del list_of_complex_numbers[position]
        return list_of_complex_numbers
    return "error_valid_position"


def remove_positions_from_list(history, start_position, end_position, list_of_complex_numbers):
    """
    Remove complex numbers from a sequence in the list
    :param history: The history list of the  changes in the list of complex numbers
    :param start_position: The position from which the numbers start to be removed
    :param end_position: The position where the numbers end to be removed
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the removing
    """
    if validate_positions(start_position, end_position, len(list_of_complex_numbers)) == 1:
        index = start_position
        add_list_to_history(history, list_of_complex_numbers)
        while index <= end_position:
            del list_of_complex_numbers[index]
            end_position -= 1
        return list_of_complex_numbers
    return "error_valid_position"


def replace_complex_number_from_list(history, number_to_be_replaced, number_to_replace, list_of_complex_numbers):
    """
    Replace a complex number in the list
    :param history: The history list of the  changes in the list of complex numbers
    :param number_to_be_replaced: The number that has to be replaced
    :param number_to_replace: The number that has to replace the old number
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the replacing
    """
    message = "ok"
    if "error" not in number_to_be_replaced and "error" not in number_to_replace:
        real_part_to_be_replaced = get_real_part(number_to_be_replaced)
        imaginary_part_to_be_replaced = get_imaginary_part(number_to_be_replaced)
        complex_number_to_be_replaced = create_complex_number(real_part_to_be_replaced, imaginary_part_to_be_replaced)
        real_part_to_replace = get_real_part(number_to_replace)
        imaginary_part_to_replace = get_imaginary_part(number_to_replace)
        complex_number_to_replace = create_complex_number(real_part_to_replace, imaginary_part_to_replace)
        length = len(list_of_complex_numbers)
        number_is_found = 0
        add_list_to_history(history, list_of_complex_numbers)
        for index in range(length):
            if list_of_complex_numbers[index] == complex_number_to_be_replaced:
                list_of_complex_numbers[index] = complex_number_to_replace
                number_is_found = 1
        if number_is_found == 0:
            pop_list_from_history(history)
            ui.print_error_not_existing_number()
            message = "error_existing_number"
    else:
        ui.print_error_valid_number()
        message = "error_valid_number"
    return list_of_complex_numbers, message


def is_real(complex_number):
    """
    Check if a number is real or not
    :param complex_number: The complex number to be checked
    :return: 1 - if the number is real
             0 - otherwise
    """
    if get_imaginary_part(complex_number) == 0:
        return 1
    return 0


def create_list_of_real_numbers(list_of_complex_numbers_history, start_position, end_position, list_of_complex_number):
    """
    Create a list with the real numbers from the original list
    :param list_of_complex_numbers_history: The history list of the  changes in the list of complex numbers
    :param start_position: The position from which the numbers start to be checked
    :param end_position: The position where the numbers end to be removed
    :param list_of_complex_number: The list of complex numbers
    :return: list_of_real_numbers : The list with the real numbers
    """
    list_of_real_numbers = []
    numbers_found = 0
    if validate_positions(start_position, end_position, len(list_of_complex_number)):
        index = 0
        for i in list_of_complex_number:
            if start_position <= index <= end_position:
                if is_real(i):
                    numbers_found += 1
                    add_complex_number_to_list(list_of_complex_numbers_history, i, list_of_real_numbers)
            index += 1
        if numbers_found == 0:
            ui.print_error_not_existing_real_number()
            return 0
        return list_of_real_numbers
    return 0


def create_list_modulo(list_of_complex_numbers_history, relation, number_to_compare, list_of_complex_number):
    """
    Create a list with the complex numbers having the modulo with a property given
    :param list_of_complex_numbers_history: The history list of the  changes in the list of complex numbers
    :param relation: The relation to compare the modulo
    :param number_to_compare: The number to compare the modulo
    :param list_of_complex_number: The list of complex numbers
    :return: list_of_modulo_numbers : The list with numbers having the modulo property
    """
    list_of_modulo_numbers = []
    numbers_found = 0
    for i in list_of_complex_number:
        modulo = get_modulo(i)
        if relation == '<':
            if modulo < number_to_compare * number_to_compare:
                numbers_found += 1
                add_complex_number_to_list(list_of_complex_numbers_history, i, list_of_modulo_numbers)
        elif relation == '=':
            if modulo == number_to_compare * number_to_compare:
                numbers_found += 1
                add_complex_number_to_list(list_of_complex_numbers_history, i, list_of_modulo_numbers)
        elif relation == '>':
            if modulo > number_to_compare * number_to_compare:
                numbers_found += 1
                add_complex_number_to_list(list_of_complex_numbers_history, i, list_of_modulo_numbers)
    if numbers_found == 0:
        ui.print_error_not_existing_modulo_number()
        return 0
    return list_of_modulo_numbers


def sum_list(start_position, end_position, list_of_complex_number):
    """
    compute the sum of the numbers in a sequence of the list
    :param start_position: The start position for computing the sum
    :param end_position: The end position for computing the sum
    :param list_of_complex_number: The list of complex numbers
    :return: sum_real_part: The sum of the real parts of the complex numbers
             sum_imaginary_part: The sum of the imaginary parts of the complex numbers
    """
    sum_real_part = 0
    sum_imaginary_part = 0
    if validate_positions(start_position, end_position, len(list_of_complex_number)):
        index = 0
        for i in list_of_complex_number:
            if start_position <= index <= end_position:
                sum_real_part += get_real_part(i)
                sum_imaginary_part += get_imaginary_part(i)
            index += 1
    return sum_real_part, sum_imaginary_part


def product_list(start_position, end_position, list_of_complex_number):
    """
    compute the product of the numbers in a sequence of the list
    :param start_position: The start position for computing the product
    :param end_position: The end position for computing the product
    :param list_of_complex_number: The list of complex numbers
    :return: product_real_part: The product of the real parts of the complex numbers
             product_imaginary_parts: The product of the imaginary parts of the complex numbers
    """
    product_real_part = 1
    product_imaginary_part = 1
    if validate_positions(start_position, end_position, len(list_of_complex_number)):
        index = 0
        for i in list_of_complex_number:
            if start_position <= index <= end_position:
                product_real_part = product_real_part * get_real_part(i) - product_imaginary_part * get_imaginary_part(
                    i)
                product_imaginary_part = product_real_part * get_imaginary_part(
                    i) + product_imaginary_part * get_real_part(i)
            index += 1
    return product_real_part, product_imaginary_part


def filter_real(history, list_of_complex_numbers):
    """
    Filter the real numbers in the list
    :param history: The history list of the changes in the list of complex numbers
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list of complex numbers filtered
    """
    index = 0
    add_list_to_history(history, list_of_complex_numbers)
    while index < len(list_of_complex_numbers):
        if is_real(list_of_complex_numbers[index]) == 0:
            del list_of_complex_numbers[index]
        else:
            index += 1
    return list_of_complex_numbers


def filter_modulo(list_of_complex_numbers_history, relation, number_to_compare, list_of_complex_numbers):
    """
    Filter the numbers in the list by having the modulo with a property given
    :param list_of_complex_numbers_history: The history list of the changes in the list of complex numbers
    :param relation: The relation to compare the modulo
    :param number_to_compare: The number to compare the modulo
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list of complex numbers filtered
    """
    add_list_to_history(list_of_complex_numbers_history, list_of_complex_numbers)
    for index in range(len(list_of_complex_numbers) - 1, -1, -1):
        modulo = get_modulo(list_of_complex_numbers[index])
        if relation == '<':
            if modulo >= number_to_compare * number_to_compare:
                del list_of_complex_numbers[index]
        elif relation == '=':
            if modulo != number_to_compare * number_to_compare:
                del list_of_complex_numbers[index]
        elif relation == '>':
            if modulo <= number_to_compare * number_to_compare:
                del list_of_complex_numbers[index]
        index += 1
    return list_of_complex_numbers


def get_last_item_from_history(history):
    """
    Get the last item from the history list
    :param history: The history list of the changes in the list of complex numbers
    :return: The last item from the history list
    """
    return history[-1]


def add_list_to_history(history, list):
    """
    Add a new element to the history list of changes
    :param history: The history list of changes
    :param list: The new element to be added
    :return:
    """
    history_list = list[:]
    history.append(history_list)


def pop_list_from_history(history):
    history.pop()


def undo_list(list_of_complex_numbers_history, list_of_complex_numbers):
    """
    Function for the undo operation with the list of complex numbers
    :param list_of_complex_numbers_history: The history list of the changes in the list of complex numbers
    :param list_of_complex_numbers: The list of complex numbers
    :return:
    """
    if list_of_complex_numbers_history:
        list_of_complex_numbers.clear()
        new_list = get_last_item_from_history(list_of_complex_numbers_history)[:]
        for item in new_list:
            list_of_complex_numbers.append(item)
        pop_list_from_history(list_of_complex_numbers_history)
    else:
        ui.print_error_undo()
