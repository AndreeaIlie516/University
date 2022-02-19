from functions import *


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


def test_get_modulo():
    """
    Test function for getting the modulo of a complex number
    :return:
    """
    assert get_modulo([2, 2]) == 2 ** 2 + 2 ** 2
    assert get_modulo([0, 5]) == 0 ** 2 + 5 ** 2
    assert get_modulo([0, -6]) == 0 ** 2 + (-6) ** 2
    assert get_modulo([3, 0]) == 3 ** 2 + 0 ** 2
    assert get_modulo([-4, 0]) == (-4) ** 2 + 0 ** 2
    assert get_modulo([-2, -3]) == (-2) ** 2 + (-3) ** 2


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


def test_extract_position_from_param():
    """
    Test function for verifying extraction of a position from a parameter
    :return:
    """
    assert extract_position_from_param(['7'], 10) == 7
    assert extract_position_from_param(['9'], 10) == 9
    assert extract_position_from_param(['a'], 10) == "error_valid_position"


def test_extract_positions_from_param():
    """
    Test function for verifying extraction of two positions from two parameters
    :return:
    """
    assert extract_positions_from_param(['remove', '2', '7'], 10) == (2, 7)
    assert extract_positions_from_param(['list real', '3', '9'], 10) == (3, 9)
    assert extract_positions_from_param(['remove', 'a', '9'], 10) == ("error_valid_position", "error_valid_position")
    assert extract_positions_from_param(['remove', '-2', '9'], 10) == (-2, 9)


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


def test_insert_complex_number_to_list():
    """
    Test function for inserting a complex number in the list
    :return:
    """
    list_of_complex_numbers_history = []
    list_of_complex_numbers = [[7, 3], [2, 5]]
    insert_complex_number_to_list(list_of_complex_numbers_history, [12, -6], 1, list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [12, -6], [2, 5]]
    insert_complex_number_to_list(list_of_complex_numbers_history, [-25, 11], 0, list_of_complex_numbers)
    assert list_of_complex_numbers == [[-25, 11], [7, 3], [12, -6], [2, 5]]
    insert_complex_number_to_list(list_of_complex_numbers_history, [-4, -10], 4, list_of_complex_numbers)
    assert list_of_complex_numbers == [[-25, 11], [7, 3], [12, -6], [2, 5], [-4, -10]]
    insert_complex_number_to_list(list_of_complex_numbers_history, "error_complex_number", 1, list_of_complex_numbers)
    assert list_of_complex_numbers == [[-25, 11], [7, 3], [12, -6], [2, 5], [-4, -10]]


def test_remove_position_from_list():
    """
    Test function for removing a complex number on a position in the list
    :return:
    """
    list_of_complex_numbers_history = []
    list_of_complex_numbers = [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]
    remove_position_from_list(list_of_complex_numbers_history, 2, list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [7, 0], [-124, 16]]
    remove_position_from_list(list_of_complex_numbers_history, 0, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [7, 0], [-124, 16]]
    remove_position_from_list(list_of_complex_numbers_history, 2, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [7, 0]]
    remove_position_from_list(list_of_complex_numbers_history, 3, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [7, 0]]
    remove_position_from_list(list_of_complex_numbers_history, -1, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [7, 0]]


def test_remove_positions_from_list():
    """
    Test function for removing a sequence of complex numbers in the list
    :return:
    """
    list_of_complex_numbers_history = []
    list_of_complex_numbers = [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]
    remove_positions_from_list(list_of_complex_numbers_history, 2, 3, list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 5], [-124, 16]]
    remove_positions_from_list(list_of_complex_numbers_history, 0, 0, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [-124, 16]]
    remove_positions_from_list(list_of_complex_numbers_history, -3, 0, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [-124, 16]]
    remove_positions_from_list(list_of_complex_numbers_history, 0, 12, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 5], [-124, 16]]


def test_replace_complex_number_from_list():
    """
    Test function for replacing a complex number in the list with another one
    :return:
    """
    list_of_complex_numbers_history = []
    list_of_complex_numbers = [[7, 3], [2, 5], [4, 2], [7, 0], [-124, 16]]
    replace_complex_number_from_list(list_of_complex_numbers_history, [7, 3], [2, 4], list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 4], [2, 5], [4, 2], [7, 0], [-124, 16]]
    replace_complex_number_from_list(list_of_complex_numbers_history, [2, 5], [-16, -12], list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 4], [-16, -12], [4, 2], [7, 0], [-124, 16]]


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


def test_create_list_of_real_numbers():
    """
    Test function for selecting the real numbers in the list
    :return:
    """
    list_of_complex_numbers_history = []
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    list_of_real_numbers = create_list_of_real_numbers(list_of_complex_numbers_history, 1, 2, list_of_complex_numbers)
    assert list_of_real_numbers == [[2, 0], [4, 0]]
    list_of_real_numbers = create_list_of_real_numbers(list_of_complex_numbers_history, 1, 4, list_of_complex_numbers)
    assert list_of_real_numbers == [[2, 0], [4, 0], [7, 0]]
    list_of_real_numbers = create_list_of_real_numbers(list_of_complex_numbers_history, 0, 0, list_of_complex_numbers)
    assert list_of_real_numbers == 0
    list_of_real_numbers = create_list_of_real_numbers(list_of_complex_numbers_history, -2, 0, list_of_complex_numbers)
    assert list_of_real_numbers == 0


def test_create_list_modulo():
    """
    Test function for selecting the complex numbers having the modulo with a property given
    :return:
    """
    list_of_complex_numbers_history = []
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    list_of_modulo_numbers = create_list_modulo(list_of_complex_numbers_history, '<', 8, list_of_complex_numbers)
    assert list_of_modulo_numbers == [[7, 3], [2, 0], [4, 0], [7, 0]]
    list_of_modulo_numbers = create_list_modulo(list_of_complex_numbers_history, '>', 4, list_of_complex_numbers)
    assert list_of_modulo_numbers == [[7, 3], [7, 0], [-124, 16]]
    list_of_modulo_numbers = create_list_modulo(list_of_complex_numbers_history, '=', 2, list_of_complex_numbers)
    assert list_of_modulo_numbers == [[2, 0]]


def test_sum_list():
    """
    Test function for computing the sum of the complex numbers in a sequence in the list
    :return:
    """
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    assert sum_list(1, 3, list_of_complex_numbers) == (13, 0)
    assert sum_list(1, 2, list_of_complex_numbers) == (6, 0)
    assert sum_list(0, 1, list_of_complex_numbers) == (9, 3)
    assert sum_list(3, 4, list_of_complex_numbers) == (-117, 16)


def test_product_list():
    """
    Test function for computing the product of the complex numbers in a sequence in the list
    :return:
    """
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    assert product_list(1, 3, list_of_complex_numbers) == (56, 56)
    assert product_list(1, 2, list_of_complex_numbers) == (8, 8)
    assert product_list(0, 1, list_of_complex_numbers) == (8, 38)
    assert product_list(3, 4, list_of_complex_numbers) == (-980, -16548)


def test_filter_real():
    """
    Test function for filtering the real numbers in the list
    :return:
    """
    list_of_complex_numbers_history = []
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    list_of_complex_numbers = filter_real(list_of_complex_numbers_history, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 0], [4, 0], [7, 0]]
    list_of_complex_numbers = [[7, 3], [2, 6], [4, 3], [7, 8], [-124, 16]]
    list_of_complex_numbers = filter_real(list_of_complex_numbers_history, list_of_complex_numbers)
    assert list_of_complex_numbers == []


def test_filter_modulo():
    """
    Test function for filtering the complex numbers having the modulo with a property given
    :return:
    """
    list_of_complex_numbers_history = []
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    list_of_complex_numbers = filter_modulo(list_of_complex_numbers_history, '<', 8, list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [2, 0], [4, 0], [7, 0]]
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    list_of_complex_numbers = filter_modulo(list_of_complex_numbers_history, '>', 4, list_of_complex_numbers)
    assert list_of_complex_numbers == [[7, 3], [7, 0], [-124, 16]]
    list_of_complex_numbers = [[7, 3], [2, 0], [4, 0], [7, 0], [-124, 16]]
    list_of_complex_numbers = filter_modulo(list_of_complex_numbers_history, '=', 2, list_of_complex_numbers)
    assert list_of_complex_numbers == [[2, 0]]


def test_add_list_to_history():
    """
    Test function for adding an operation to the history list of the  changes in the list of complex numbers
    :return:
    """
    history_list = []
    list = [[4, 5], [2, 9], [3, 3], [1, 5], [5, -1], [2, 9]]
    filter_modulo(history_list, ">", 10, list)
    assert history_list == [[[4, 5], [2, 9], [3, 3], [1, 5], [5, -1], [2, 9]]]

    history_list = []
    list = [[2, 10], [2, 3], [0, 0], [5, 5], [7, 0], [9, 9]]
    filter_real(history_list, list)
    assert history_list[-1] == [[2, 10], [2, 3], [0, 0], [5, 5], [7, 0], [9, 9]]

    add_complex_number_to_list(history_list, [7, 2], list)
    assert get_last_item_from_history(history_list) == [[0, 0], [7, 0]]

    remove_position_from_list(history_list, 0, list)
    assert get_last_item_from_history(history_list) == [[0, 0], [7, 0], [7, 2]]


def test_pop_list_from_history():
    """
    Test function for popping an operation from the history list of the  changes in the list of complex numbers
    :return:
    """

    history_list = []
    list = [[4, 5], [2, 9], [3, 3], [1, 5], [5, -1], [2, 9]]
    filter_modulo(history_list, ">", 10, list)
    pop_list_from_history(history_list)
    assert history_list == []

    history_list = []
    list = [[7, 2], [5, 5]]
    add_complex_number_to_list(history_list, [6, 2], list)
    add_complex_number_to_list(history_list, [4, 1], list)
    pop_list_from_history(history_list)

    assert history_list[-1] == [[7, 2], [5, 5]]

    history_list = []
    list = [[5, 2], [6, 4], [6, 6]]
    remove_position_from_list(history_list, 0, list)
    add_complex_number_to_list(history_list, [4, 0], list)
    pop_list_from_history(history_list)
    assert history_list[-1] == [[5, 2], [6, 4], [6, 6]]


def test_get_last_item_from_history():
    """
    Test function for getting the last element in the history list of the  changes in the list of complex numbers
    :return:
    """
    history = []
    list = [[4, 5], [2, 9], [3, 3], [1, 0], [5, -1], [2, 9]]
    filter_real(history, list)
    assert get_last_item_from_history(history) == [[4, 5], [2, 9], [3, 3], [1, 0], [5, -1], [2, 9]]

    add_complex_number_to_list(history, [4, 4], list)
    assert get_last_item_from_history(history) == [[1, 0]]

    remove_position_from_list(history, 0, list)
    assert get_last_item_from_history(history) == [[1, 0], [4, 4]]


def test_undo_list():
    """
    Test function for the undo operation
    :return:
    """
    history = []
    list = [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]
    filter_real(history, list)
    undo_list(history, list)
    assert list == [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9]]

    add_complex_number_to_list(history, [4, 4], list)
    remove_position_from_list(history, 0, list)
    undo_list(history, list)
    assert list == [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9], [4, 4]]

    replace_complex_number_from_list(history, [6, 9], [3, 2], list)
    undo_list(history, list)
    assert list == [[5, 10], [6, 0], [0, -1], [5, 5], [0, 0], [6, 9], [4, 4]]


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
    test_sum_list()
    test_product_list()
    test_filter_real()
    test_filter_modulo()
    test_pop_list_from_history()
    test_add_list_to_history()
    test_get_last_item_from_history()
    test_undo_list()
