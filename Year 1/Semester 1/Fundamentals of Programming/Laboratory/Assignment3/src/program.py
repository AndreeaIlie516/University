import math

"""
  Write non-UI functions below
"""


def test_create_complex_number():
    """
    Test function for creating a complex number
    :return:
    """
    assert create_complex_number() == [0, 0]
    assert create_complex_number(3) == [3, 0]
    assert create_complex_number(-253) == [-253, 0]
    assert create_complex_number(0, 12) == [0, 12]
    assert create_complex_number(0, -54) == [0, -54]
    assert create_complex_number(3, 4) == [3, 4]
    assert create_complex_number(423, -125) == [423, -125]
    assert create_complex_number(-534, 52) == [-534, 52]
    assert create_complex_number(-253, -45) == [-253, -45]


def create_complex_number(real_part=0, imaginary_part=0):
    """
    Create a complex number
    :param real_part: The real part of the number
    :param imaginary_part: The imaginary part of the number
    :return: The complex number created (list)
    """
    return [real_part, imaginary_part]


def test_get_real_part():
    """
    Test function for getting the real part of a complex number
    :return:
    """
    assert get_real_part([0, 0]) == 0
    assert get_real_part([12, 0]) == 12
    assert get_real_part([-532, 0]) == -532
    assert get_real_part([0, 1]) == 0
    assert get_real_part([45, 253]) == 45
    assert get_real_part([-53, 12]) == -53
    assert get_real_part([17, -24]) == 17
    assert get_real_part([-241, -15]) == -241


def get_real_part(complex_number):
    """
    Get real part of a complex number
    :param complex_number: The complex number (list)
    :return: The real part of the complex number
    """
    return complex_number[0]


def test_get_imaginary_part():
    """
    Test function for getting the imaginary part of a complex number
    :return:
    """
    assert get_imaginary_part([0, 0]) == 0
    assert get_imaginary_part([12, 0]) == 0
    assert get_imaginary_part([-532, 0]) == -0
    assert get_imaginary_part([0, 1]) == 1
    assert get_imaginary_part([45, 253]) == 253
    assert get_imaginary_part([-53, 12]) == 12
    assert get_imaginary_part([17, -24]) == -24
    assert get_imaginary_part([-241, -15]) == -15


def get_imaginary_part(complex_number):
    """
    Get imaginary part of a complex number
    :param complex_number: The complex number (list)
    :return: The imaginary part of the complex number
    """
    return complex_number[1]


def test_get_modulo():
    """
    Test function for getting the modulo of a complex number
    :return:
    """
    assert get_modulo([2, 2]) == math.sqrt(2 ** 2 + 2 ** 2)
    assert get_modulo([0, 5]) == math.sqrt(0 ** 2 + 5 ** 2)
    assert get_modulo([0, -6]) == math.sqrt(0 ** 2 + (-6) ** 2)
    assert get_modulo([3, 0]) == math.sqrt(3 ** 2 + 0 ** 2)
    assert get_modulo([-4, 0]) == math.sqrt((-4) ** 2 + 0 ** 2)
    assert get_modulo([-2, -3]) == math.sqrt((-2) ** 2 + (-3) ** 2)


def get_modulo(complex_number):
    """
    Get modulo of a complex number function
    :param complex_number: The complex number
    :return:

    """
    real_part = get_real_part(complex_number)
    imaginary_part = get_imaginary_part(complex_number)
    modulo = math.sqrt(real_part * real_part + imaginary_part * imaginary_part)
    return modulo


def test_set_real_part():
    """
    Test function for setting the real part of a complex number
    :return:
    """
    assert set_real_part([0, 0], 3) == [3, 0]
    assert set_real_part([0, 0], -12) == [-12, 0]
    assert set_real_part([0, 7], 25) == [25, 7]
    assert set_real_part([0, 7], -25) == [-25, 7]
    assert set_real_part([0, -25], 17) == [17, -25]
    assert set_real_part([0, -25], -17) == [-17, -25]


def set_real_part(complex_number, value):
    """
    Set the real part to a complex number function
    :param complex_number: number to set the real part
    :param value: the value of the real part
    :return: the complex number set
    """
    complex_number[0] = value
    return complex_number


def test_set_imaginary_part():
    """
    Test function for setting the imaginary part of a complex number
    :return:
    """
    assert set_imaginary_part([0, 0], 7) == [0, 7]
    assert set_imaginary_part([0, 0], -7) == [0, -7]
    assert set_imaginary_part([25, 0], 16) == [25, 16]
    assert set_imaginary_part([25, 0], -16) == [25, -16]
    assert set_imaginary_part([-53, 0], 125) == [-53, 125]
    assert set_imaginary_part([-53, 0], -125) == [-53, -125]


def set_imaginary_part(complex_number, value):
    """
    Set the imaginary part to a complex number function
    :param complex_number: number to set the imaginary part
    :param value: the value of the imaginary part
    :return: the complex number set
    """
    complex_number[1] = value
    return complex_number


def test_split_command_params():
    """
    The function for splitting the commands given as a parameter
    :return:
    """
    assert split_command_params('exit') == ('exit', None)
    assert split_command_params('eXiT') == ('exit', None)
    assert split_command_params('list') == ('list', None)
    assert split_command_params('LisT') == ('list', None)
    assert split_command_params('add 2+5i') == ('add', ['2+5i'])
    assert split_command_params("ADD 2+5i") == ("add", ['2+5i'])
    assert split_command_params("insert 2+56i at 4") == ("insert", ['2+56i', '4'])
    assert split_command_params("   insert 2+56i at 4") == ("insert", ['2+56i', '4'])
    assert split_command_params("remove 5") == ("remove", ['5'])
    assert split_command_params("remove     5") == ("remove", ['5'])
    assert split_command_params("remove 3 to 6") == ("remove", ['3', '6'])
    assert split_command_params("replace 3+6i with 2+7i") == ("replace", ['3+6i', '2+7i'])
    assert split_command_params("list real 1 to 5") == ("list real", ['1', '5'])
    assert split_command_params("list modulo = 10") == ("list modulo", ['=', '10'])
    assert split_command_params('add -2+5i') == ('add', ['-2+5i'])
    assert split_command_params("ADD   -2") == ("add", ['-2'])
    assert split_command_params("ADD   a+bi") == ("add", ['error_complex_number'])


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
        cmd_word.append(tokens[index].lower())
        index += 1
    else:
        cmd_word = None
    if length > 1:
        if index != length - 1:
            if tokens[index].isalpha() == 1 and index != length - 1:
                cmd_word.append(tokens[index].lower())
                index += 1
        if length > index:
            while index < length:
                if tokens[index] == '<' or tokens[index] == '=' or tokens[index] == '>':
                    cmd_param.append(tokens[index].lower())
                if tokens[index][0].isdigit() == 1 or tokens[index][0] == '-':
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
        cmd_word = ' '.join(cmd_word)
        cmd_word = cmd_word.lower()
    return cmd_word, cmd_param


def test_extract_complex_number_from_string():
    """
    Test function for verifying extraction of a complex number from a string
    :return:
    """
    assert extract_complex_number_from_string('2+5i') == (2, 5)
    assert extract_complex_number_from_string('-12+5i') == (-12, 5)
    assert extract_complex_number_from_string('-2-5i') == (-2, -5)
    assert extract_complex_number_from_string('2-5i') == (2, -5)
    assert extract_complex_number_from_string('-2') == (-2, 0)
    assert extract_complex_number_from_string('24') == (24, 0)
    assert extract_complex_number_from_string('5i') == (0, 5)
    assert extract_complex_number_from_string('109i') == (0, 109)
    assert extract_complex_number_from_string('5+9') == "error_complex_number"
    assert extract_complex_number_from_string('5+a') == "error_complex_number"
    assert extract_complex_number_from_string('a+bi') == "error_valid_number"


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
    if complex_number[index] == '-':
        complex_number = complex_number[1:]
        if '+' in complex_number or '-' in complex_number:
            is_negative_real = 1
        elif 'i' in complex_number:
            is_negative_imag = 1
        else:
            is_negative_real = 1
    complex_number = complex_number.strip()
    tokens = complex_number.split(' ')
    if '+' in complex_number:
        tokens = complex_number.split('+')
    elif '-' in complex_number:
        tokens = complex_number.split('-')
        is_negative_imag = 1
    elif 'i' in complex_number:
        has_real_part = 0
        real_part = 0
    if has_real_part == 1:
        real_part = tokens[index]
        index += 1
        try:
            real_part = int(real_part)
        except:
            print_error_valid_number()
            return "error_valid_number"
        if is_negative_real == 1:
            real_part *= (-1)
    try:
        imaginary_part = tokens[index]
        if imaginary_part != 0:
            if imaginary_part[len(imaginary_part) - 1:] != 'i':
                print_error_complex_number()
                return "error_complex_number"
            imaginary_part = imaginary_part.replace('i', '')
    except:
        imaginary_part = 0
    try:
        imaginary_part = int(imaginary_part)
    except:
        print_error_valid_number()
        return "error_valid_number"
    if is_negative_imag == 1:
        imaginary_part *= (-1)
    return real_part, imaginary_part


def test_extract_complex_number_from_param():
    """
    Test function for verifying extraction of a complex number from a parameter
    :return:
    """
    assert extract_complex_number_from_param(['2+5i']) == (2, 5)
    assert extract_complex_number_from_param(['-2+5i']) == (-2, 5)
    assert extract_complex_number_from_param(['-2-5i']) == (-2, -5)
    assert extract_complex_number_from_param(['2-5i']) == (2, -5)
    assert extract_complex_number_from_param(['-2']) == (-2, 0)
    assert extract_complex_number_from_param(['24']) == (24, 0)
    assert extract_complex_number_from_param(['5i']) == (0, 5)
    assert extract_complex_number_from_param(['109i']) == (0, 109)
    assert extract_complex_number_from_param(['5+9']) == "error_complex_number"
    assert extract_complex_number_from_param(['5+a']) == "error_complex_number"
    assert extract_complex_number_from_param(['a+bi']) == "error_valid_number"


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
        print_error_valid_number()
        return "error_valid_number"


def test_extract_numbers_from_param():
    """
    Test function for verifying extraction of two complex numbers from two parameters
    :return:
    """
    assert extract_numbers_from_param(['2+7i', '5+12i']) == ((2, 7), (5, 12))
    assert extract_numbers_from_param(['12-3i', '5+12i']) == ((12, -3), (5, 12))
    assert extract_numbers_from_param(['7i', '5-12i']) == ((0, 7), (5, -12))
    assert extract_numbers_from_param(['2', '12i']) == ((2, 0), (0, 12))
    assert extract_numbers_from_param(['2+7i', '0']) == ((2, 7), (0, 0))
    assert extract_numbers_from_param(['0', '5+12i']) == ((0, 0), (5, 12))


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


def test_validate_position():
    """
    Test function for validating a position in a list
    :return:
    """
    assert validate_position(2, 4) == 1
    assert validate_position(0, 12) == 1
    assert validate_position(9, 10) == 1
    assert validate_position('a', 12) == "error_valid_position"
    assert validate_position(-2, 4) == "error_position_range"
    assert validate_position(10, 10) == "error_position_range"


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
        print_error_valid_position()
        return "error_valid_position"
    if 0 > position or position >= length:
        print_error_position_range()
        return "error_position_range"
    return 1


def test_validate_positions():
    """
    Test functions for validating 2 positions in a list
    :return:
    """
    assert validate_positions(0, 9, 10) == 1
    assert validate_positions(0, 5, 10) == 1
    assert validate_positions(3, 9, 10) == 1
    assert validate_positions(2, 7, 10) == 1
    assert validate_positions(0, 'b', 10) == "error_valid_position"
    assert validate_positions('a', 7, 10) == "error_valid_position"
    assert validate_positions('a', 'b', 10) == "error_valid_position"
    assert validate_positions(7, 3, 10) == "error_start_end_position"
    assert validate_positions(-1, 7, 10) == "error_start_position"
    assert validate_positions(12, 23, 10) == "error_start_position"
    assert validate_positions(0, 13, 10) == "error_end_position"
    assert validate_positions(0, 10, 10) == "error_end_position"


def validate_positions(start_position, end_position, length):
    """
    Validate two positions by checking if they are positive integers and they are  >0 and < length of the string
    and start position < end position
    :param start_position: the start position to be validated
    :param end_position: the end position to be validated
    :param length: the length of the list
    :return: 1 - if the positions are good
             error message - otherwise
    """
    try:
        start_position = int(start_position)
    except:
        print_error_valid_position()
        return "error_valid_position"
    try:
        end_position = int(end_position)
    except:
        print_error_valid_position()
        return "error_valid_position"
    if start_position > end_position:
        print_error_start_end_position()
        return "error_start_end_position"
    if 0 > start_position or start_position >= length:
        print_error_start_position()
        return "error_start_position"
    if 0 > end_position or end_position >= length:
        print_error_end_position()
        return "error_end_position"
    return 1


def test_validate_position_insert():
    """
    Test functions for validating a position in a list for the insert function
    :return:
    """
    assert validate_position_insert(2, 4) == 1
    assert validate_position_insert(0, 12) == 1
    assert validate_position_insert(9, 10) == 1
    assert validate_position_insert('a', 12) == "error_valid_position"
    assert validate_position_insert(-2, 4) == "error_position_range"
    assert validate_position_insert(10, 10) == 1


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
        print_error_valid_position()
        return "error_valid_position"
    if 0 > position or position > length + 1:
        print_error_position_range()
        return "error_position_range"
    return 1


def test_extract_position_from_param():
    """
    Test function for verifying extraction of a position from a parameter
    :return:
    """
    assert extract_position_from_param(['7'], 10) == 7
    assert extract_position_from_param(['9'], 10) == 9
    assert extract_position_from_param(['a'], 10) == "error_valid_position"


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


def test_extract_positions_from_param():
    """
    Test function for verifying extraction of two positions from two parameters
    :return:
    """
    assert extract_positions_from_param(['remove', '2', '7'], 10) == (2, 7)
    assert extract_positions_from_param(['list real', '3', '9'], 10) == (3, 9)
    assert extract_positions_from_param(['remove', 'a', '9'], 10) == ("error_valid_position", "error_valid_position")
    assert extract_positions_from_param(['remove', '-2', '9'], 10) == (-2, 9)


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


def test_extract_relation_from_param():
    """
    Test function for verifying extraction of a relational character from a parameter
    :return:
    """
    assert extract_relation_from_param(['<', '10']) == ('<', 10)
    assert extract_relation_from_param(['>', '5']) == ('>', 5)
    assert extract_relation_from_param(['=', '15']) == ('=', 15)
    assert extract_relation_from_param(['=', '5.19']) == "error_valid_number"
    assert extract_relation_from_param(['=', '-5']) == "error_valid_number"
    assert extract_relation_from_param((['&', '8'])) == "error_valid_relation"


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
        print_error_valid_number()
        return "error_valid_number"
    if number_to_compare != abs(number_to_compare):
        print_error_valid_number()
        return "error_valid_number"
    if relation not in "<>=":
        print_error_relation()
        return "error_valid_relation"
    return relation, number_to_compare


def test_create_complex_number_to_print():
    """
    Test function to verifying a complex number transformed in a string
    :return:
    """
    assert create_complex_number_to_print(0, 0) == '0'
    assert create_complex_number_to_print(24, 0) == '24'
    assert create_complex_number_to_print(-152, 0) == '-152'
    assert create_complex_number_to_print(0, 12) == '12i'
    assert create_complex_number_to_print(0, -152) == '-152i'
    assert create_complex_number_to_print(13, 20) == '13+20i'
    assert create_complex_number_to_print(-15, 43) == '-15+43i'
    assert create_complex_number_to_print(-20, -16) == '-20-16i'


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


def test_add_complex_number_to_list():
    """
    Test function for adding a complex number in the list
    :return:
    """
    list_of_complex_numbers = [[7, 3], [2, 5]]
    add_complex_number_to_list([4, 2], list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [4, 2]]
    add_complex_number_to_list([7, 0], list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [4, 2], [7, 0]]
    add_complex_number_to_list([-124, 16], list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]
    add_complex_number_to_list([124, 'a'], list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]
    add_complex_number_to_list(['alb', 16], list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]
    add_complex_number_to_list(['ala', 'bala'], list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]


def add_complex_number_to_list(complex_number, list_of_complex_numbers):
    """
    Add a complex number to the list
    :param complex_number: The complex number to be added
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the addition
    """
    if "error" not in complex_number:
        real_part = get_real_part(complex_number)
        imaginary_part = get_imaginary_part(complex_number)
        x = create_complex_number()

        set_real_part(x, real_part)
        set_imaginary_part(x, imaginary_part)
        list_of_complex_numbers.append(x)
    return list_of_complex_numbers


def test_insert_complex_number_to_list():
    """
    Test function for inserting a complex number in the list
    :return:
    """
    list_of_complex_numbers = [[7, 3], [2, 5]]
    insert_complex_number_to_list([12, -6], 1, list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [12, -6], [2, 5]]
    insert_complex_number_to_list([-25, 11], 0, list_of_complex_numbers)
    assert list_of_complex_numbers == [[-25, 11], [7, 3], [12, -6], [2, 5]]
    insert_complex_number_to_list([-4, -10], 4, list_of_complex_numbers)
    assert list_of_complex_numbers == [[-25, 11], [7, 3], [12, -6], [2, 5], [-4, -10]]
    insert_complex_number_to_list("error_complex_number", 1, list_of_complex_numbers)
    assert list_of_complex_numbers == [[-25, 11], [7, 3], [12, -6], [2, 5], [-4, -10]]


def insert_complex_number_to_list(complex_number, position, list_of_complex_numbers):
    """
    Insert a complex number to the list
    :param complex_number: The complex number to be inserted
    :param position: The position in which the complex number has to be inserted
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the insertion
    """
    message = "ok"
    if "error" not in complex_number:
        if validate_position_insert(position, len(list_of_complex_numbers)) == 1:
            list_of_complex_numbers.insert(position, complex_number)
        else:
            message = "error"
    else:
        message = "error"
    return list_of_complex_numbers, message


def test_remove_position_from_list():
    """
    Test function for removing a complex number on a position in the list
    :return:
    """
    list_of_complex_numbers = [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]
    remove_position_from_list(2, list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [7, 0], [-124, 16]]
    remove_position_from_list(0, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [7, 0], [-124, 16]]
    remove_position_from_list(2, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [7, 0]]
    remove_position_from_list(3, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [7, 0]]
    remove_position_from_list(-1, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [7, 0]]


def remove_position_from_list(position, list_of_complex_numbers):
    """
    Remove a complex number from a position in the list
    :param position: The position from which the complex number has to be removed
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the removing
    """
    if validate_position(position, len(list_of_complex_numbers)) == 1:
        del list_of_complex_numbers[position]
        return list_of_complex_numbers
    return "error_valid_position"


def test_remove_positions_from_list():
    """
    Test function for removing a sequence of complex numbers in the list
    :return:
    """
    list_of_complex_numbers = [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]
    remove_positions_from_list(2, 3, list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [-124, 16]]
    remove_positions_from_list(0, 0, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [-124, 16]]
    remove_positions_from_list(-3, 0, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [-124, 16]]
    remove_positions_from_list(0, 12, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [-124, 16]]


def remove_positions_from_list(start_position, end_position, list_of_complex_numbers):
    """
    Remove complex numbers from a sequence in the list
    :param start_position: The position from which the numbers start to be removed
    :param end_position: The position where the numbers end to be removed
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the removing
    """
    if validate_positions(start_position, end_position, len(list_of_complex_numbers)) == 1:
        index = start_position

        while index <= end_position:
            del list_of_complex_numbers[index]
            end_position -= 1
        return list_of_complex_numbers
    return "error_valid_position"


def test_replace_complex_number_from_list():
    """
    Test function for replacing a complex number in the list with another one
    :return:
    """
    list_of_complex_numbers = [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]
    replace_complex_number_from_list([7, 3], [2, 4], list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 4], [2, 5], [4, 2], [7, 0], [-124, 16]]
    replace_complex_number_from_list([2, 5], [-16, -12], list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 4], [-16, -12], [4, 2], [7, 0], [-124, 16]]


def replace_complex_number_from_list(number_to_be_replaced, number_to_replace, list_of_complex_numbers):
    """
    Replace a complex number in the list
    :param number_to_be_replaced: The number that has to be replaced
    :param number_to_replace: The number that has to replace the old number
    :param list_of_complex_numbers: The list of complex numbers
    :return: list_of_complex_numbers: The list after the replacing
    """
    message = "ok"
    if "error" not in number_to_be_replaced and "error" not in number_to_replace:
        real_part_to_be_replaced = get_real_part(number_to_be_replaced)
        imaginary_part_to_be_replaced = get_imaginary_part(number_to_be_replaced)
        real_part_to_replace = get_real_part(number_to_replace)
        imaginary_part_to_replace = get_imaginary_part(number_to_replace)
        length = len(list_of_complex_numbers)
        number_is_found = 0
        for index in range(length):
            real_part = get_real_part(list_of_complex_numbers[index])
            imaginary_part = get_imaginary_part(list_of_complex_numbers[index])
            if real_part == real_part_to_be_replaced and imaginary_part == imaginary_part_to_be_replaced:
                set_real_part(list_of_complex_numbers[index], real_part_to_replace)
                set_imaginary_part(list_of_complex_numbers[index], imaginary_part_to_replace)
                number_is_found = 1
        if number_is_found == 0:
            print_error_not_existing_number()
            message = "error_existing_number"
    else:
        print_error_valid_number()
        message = "error_valid_number"
    return list_of_complex_numbers, message


def test_is_real():
    """
    Test function for verifying if a complex number is real or not
    :return:
    """
    assert is_real([0, 0]) == 1
    assert is_real([0, 1]) == 0
    assert is_real([12, 0]) == 1
    assert is_real([253, 25]) == 0
    assert is_real([-222, 0]) == 1
    assert is_real([-253, -45]) == 0


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


def test_create_list_of_real_numbers():
    """
    Test function for selecting the real numbers in the list
    :return:
    """
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    list_of_real_numbers = create_list_of_real_numbers(1, 2, list_of_complex_numbers)
    assert list_of_real_numbers == [[2, 0], [4, 0]]
    list_of_real_numbers = create_list_of_real_numbers(1, 4, list_of_complex_numbers)
    assert list_of_real_numbers == [[2, 0], [4, 0], [7, 0]]
    list_of_real_numbers = create_list_of_real_numbers(0, 0, list_of_complex_numbers)
    assert list_of_real_numbers == 0
    list_of_real_numbers = create_list_of_real_numbers(-2, 0, list_of_complex_numbers)
    assert list_of_real_numbers == 0


def create_list_of_real_numbers(start_position, end_position, list_of_complex_number):
    """
    Create a list with the real numbers from the original list
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
                    add_complex_number_to_list(i, list_of_real_numbers)
            index += 1
        if numbers_found == 0:
            print_error_not_existing_real_number()
            return 0
        return list_of_real_numbers
    return 0


def test_create_list_modulo():
    """
    Test function for selecting the complex numbers having the modulo with a property given
    :return:
    """
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    list_of_modulo_numbers = create_list_modulo('<', 8, list_of_complex_numbers)
    assert list_of_modulo_numbers == [[7, 3], [2, 0], [4, 0], [7, 0]]
    list_of_modulo_numbers = create_list_modulo('>', 4, list_of_complex_numbers)
    assert list_of_modulo_numbers == [[7, 3], [7, 0], [-124, 16]]
    list_of_modulo_numbers = create_list_modulo('=', 2, list_of_complex_numbers)
    assert list_of_modulo_numbers == [[2, 0]]


def create_list_modulo(relation, number_to_compare, list_of_complex_number):
    """
    Create a list with the complex numbers having the modulo with a property given
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
            if modulo < number_to_compare:
                numbers_found += 1
                add_complex_number_to_list(i, list_of_modulo_numbers)
        elif relation == '=':
            if modulo == number_to_compare:
                numbers_found += 1
                add_complex_number_to_list(i, list_of_modulo_numbers)
        elif relation == '>':
            if modulo > number_to_compare:
                numbers_found += 1
                add_complex_number_to_list(i, list_of_modulo_numbers)
    if numbers_found == 0:
        print_error_not_existing_modulo_number()
        return 0
    return list_of_modulo_numbers


def non_ui_tests():
    test_create_complex_number()
    test_get_real_part()
    test_get_imaginary_part()
    test_get_modulo()
    test_set_real_part()
    test_set_imaginary_part()
    test_split_command_params()
    test_extract_complex_number_from_string()
    test_extract_complex_number_from_param()
    test_extract_numbers_from_param()
    test_validate_position()
    test_validate_positions()
    test_validate_position_insert()
    test_extract_position_from_param()
    test_extract_positions_from_param()
    test_extract_relation_from_param()
    test_create_complex_number_to_print()
    test_insert_complex_number_to_list()
    test_remove_position_from_list()
    test_remove_positions_from_list()
    test_replace_complex_number_from_list()
    test_is_real()
    test_create_list_of_real_numbers()
    test_create_list_modulo()


"""
  Write the command-driven UI below
"""


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
    real_part = get_real_part(complex_number)
    imaginary_part = get_imaginary_part(complex_number)
    complex_number = create_complex_number_to_print(real_part, imaginary_part)
    print("You added", complex_number, "successfully!")


def print_insert_success(complex_number):
    real_part = get_real_part(complex_number)
    imaginary_part = get_imaginary_part(complex_number)
    complex_number = create_complex_number_to_print(real_part, imaginary_part)
    print("You inserted", complex_number, "successfully!")


def print_remove_success():
    print("You removed the element(s) successfully!")


def print_replace_success():
    print("You replaced the element(s) successfully!")


def print_complex_number(complex_number):
    real_part = get_real_part(complex_number)
    imaginary_part = get_imaginary_part(complex_number)
    print(create_complex_number_to_print(real_part, imaginary_part))


def print_list(list_of_complex_numbers, start_position=0, end_position=0):
    """
    Print the entire list containing complex numbers
    :param list_of_complex_numbers: The list of complex numbers
    :param start_position: the start position for sequence
    :param end_position: the end position for the sequence
    :return:
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
                real_part = get_real_part(i)
                imaginary_part = get_imaginary_part(i)
                complex_number = create_complex_number_to_print(real_part, imaginary_part)
                print(complex_number)
                index += 1
        else:
            real_part = get_real_part(i)
            imaginary_part = get_imaginary_part(i)
            complex_number = create_complex_number_to_print(real_part, imaginary_part)
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
    print("\t list real <start position> to <end position> List the real numbers from the list in a range")
    print(
        "\t list modulo [ < | = | > ] <number> - List the numbers from the list having "
        "the modulo with a property given (> = < number) ")

    print("exit - Exit the application")
    print('\n')


# Create the menu
def create_menu(list_of_complex_numbers):
    """
    Create the principal menu
    :param list_of_complex_numbers: The list of complex numbers
    :return:
    """
    while True:
        cmd_param = []
        print("Please select one of the following options:")
        print_menu()
        # Read the option
        user_input = str(input(">"))
        cmd_word, cmd_param = split_command_params(user_input)
        if cmd_word == 'add':
            complex_number = extract_complex_number_from_param(cmd_param)
            add_complex_number_to_list(complex_number, list_of_complex_numbers)
            if "error" not in complex_number:
                print_add_success(complex_number)
        elif cmd_word == 'insert':
            complex_number = extract_complex_number_from_param(cmd_param[0])
            position = extract_position_from_param(cmd_param[1], len(list_of_complex_numbers))
            list_of_complex_numbers, message = insert_complex_number_to_list(complex_number, position,
                                                                             list_of_complex_numbers)
            if "error" not in message:
                print_insert_success(complex_number)
        elif cmd_word == 'remove' and len(cmd_param) == 1:
            position = extract_position_from_param(cmd_param, len(list_of_complex_numbers))
            message = remove_position_from_list(position, list_of_complex_numbers)
            if "error" not in message:
                print_remove_success()
        elif cmd_word == 'remove' and len(cmd_param) == 2:
            start_position, end_position = extract_positions_from_param(cmd_param, len(list_of_complex_numbers))
            message = remove_positions_from_list(start_position, end_position, list_of_complex_numbers)
            if "error" not in message:
                print_remove_success()
        elif cmd_word == 'replace':
            number_to_be_replaced, number_to_replace = extract_numbers_from_param(cmd_param)
            list_of_complex_numbers, message = replace_complex_number_from_list(number_to_be_replaced,
                                                                                number_to_replace,
                                                                                list_of_complex_numbers)
            if "error" not in message:
                print_replace_success()
        elif cmd_word == 'list':
            print_list(list_of_complex_numbers)
        elif cmd_word == 'list real':
            start_position, end_position = extract_positions_from_param(cmd_param, len(list_of_complex_numbers))
            list_of_real_numbers = create_list_of_real_numbers(start_position, end_position, list_of_complex_numbers)
            if list_of_real_numbers != 0:
                print_list(list_of_real_numbers)
        elif cmd_word == 'list modulo':
            relation, number_to_compare = extract_relation_from_param(cmd_param)
            list_of_modulo_numbers = create_list_modulo(relation, number_to_compare, list_of_complex_numbers)
            if list_of_modulo_numbers != 0:
                print_list(list_of_modulo_numbers)
        elif cmd_word == "exit":
            print("You exited the application.")
            return 0
        else:
            print('Invalid command. Please select one of the options!')
        print('\n')


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
        create_complex_number(-8, 14),
        create_complex_number(25, 17),
    ]
    # non_ui_tests()
    create_menu(list_of_complex_numbers)
