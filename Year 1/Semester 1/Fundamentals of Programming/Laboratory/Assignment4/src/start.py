import functions
import test
import ui

"""
  Start the program by running this module
"""

"""
  !!! It works. DO NOT TOUCH !!! 
"""


def create_menu(list_of_complex_numbers_history, list_of_complex_numbers):
    """
    Create the principal menu
    :param list_of_complex_numbers_history: The history list of the changes in the list of complex numbers
    :param list_of_complex_numbers: The list of complex numbers
    :return:
    """
    print("Please select one of the following options:")
    ui.print_menu()

    while True:
        cmd_param = []
        # Read the option
        user_input = str(input(">"))
        cmd_word, cmd_param = functions.split_command_params(user_input)
        if cmd_word == 'add':
            complex_number = functions.extract_complex_number_from_param(cmd_param)
            functions.add_complex_number_to_list(list_of_complex_numbers_history, complex_number,
                                                 list_of_complex_numbers)
            if "error" not in complex_number:
                ui.print_add_success(complex_number)
        elif cmd_word == 'insert':
            complex_number = functions.extract_complex_number_from_param(cmd_param[0])
            position = functions.extract_position_from_param(cmd_param[1], len(list_of_complex_numbers))
            list_of_complex_numbers, message = functions.insert_complex_number_to_list(list_of_complex_numbers_history,
                                                                                       complex_number, position,
                                                                                       list_of_complex_numbers)
            if "error" not in message:
                ui.print_insert_success(complex_number)
        elif cmd_word == 'remove' and len(cmd_param) == 1:
            position = functions.extract_position_from_param(cmd_param, len(list_of_complex_numbers))
            message = functions.remove_position_from_list(list_of_complex_numbers_history, position,
                                                          list_of_complex_numbers)
            if "error" not in message:
                ui.print_remove_success()
        elif cmd_word == 'remove' and len(cmd_param) == 2:
            start_position, end_position = functions.extract_positions_from_param(cmd_param,
                                                                                  len(list_of_complex_numbers))
            message = functions.remove_positions_from_list(list_of_complex_numbers_history, start_position,
                                                           end_position,
                                                           list_of_complex_numbers)
            if "error" not in message:
                ui.print_remove_success()
        elif cmd_word == 'replace':
            number_to_be_replaced, number_to_replace = functions.extract_numbers_from_param(cmd_param)
            list_of_complex_numbers, message = functions.replace_complex_number_from_list(
                list_of_complex_numbers_history,
                number_to_be_replaced,
                number_to_replace,
                list_of_complex_numbers)
            if "error" not in message:
                ui.print_replace_success()
        elif cmd_word == 'list':
            ui.print_list(list_of_complex_numbers)
        elif cmd_word == 'list real':
            list = []
            start_position, end_position = functions.extract_positions_from_param(cmd_param,
                                                                                  len(list_of_complex_numbers))
            list_of_real_numbers = functions.create_list_of_real_numbers(list, start_position, end_position,
                                                                         list_of_complex_numbers)
            if list_of_real_numbers != 0:
                ui.print_list(list_of_real_numbers)
        elif cmd_word == 'list modulo':
            list = []
            relation, number_to_compare = functions.extract_relation_from_param(cmd_param)
            list_of_modulo_numbers = functions.create_list_modulo(list, relation, number_to_compare,
                                                                  list_of_complex_numbers)
            if list_of_modulo_numbers != 0:
                ui.print_list(list_of_modulo_numbers)
        elif cmd_word == "sum":
            start_position, end_position = functions.extract_positions_from_param(cmd_param,
                                                                                  len(list_of_complex_numbers))
            sum_real_part, sum_imaginary_part = functions.sum_list(start_position, end_position,
                                                                   list_of_complex_numbers)
            ui.print_sum(sum_real_part, sum_imaginary_part)
        elif cmd_word == "product":
            start_position, end_position = functions.extract_positions_from_param(cmd_param,
                                                                                  len(list_of_complex_numbers))
            product_real_part, product_imaginary_part = functions.product_list(start_position, end_position,
                                                                               list_of_complex_numbers)
            ui.print_product(product_real_part, product_imaginary_part)
        elif cmd_word == 'filter real':
            functions.filter_real(list_of_complex_numbers_history, list_of_complex_numbers)
            ui.print_filter_real_success()
        elif cmd_word == 'filter modulo':
            relation, number_to_compare = functions.extract_relation_from_param(cmd_param)
            functions.filter_modulo(list_of_complex_numbers_history, relation, number_to_compare,
                                    list_of_complex_numbers)
            ui.print_filter_modulo_success()
        elif cmd_word == 'undo':
            functions.undo_list(list_of_complex_numbers_history, list_of_complex_numbers)
        elif cmd_word == "exit":
            print("You exited the application.")
            return 0
        else:
            print('Invalid command. Please select one of the options!')
        print('\n')


# The main function
if __name__ == '__main__':
    list_of_complex_numbers = [
        functions.create_complex_number(7, 3),
        functions.create_complex_number(2, 0),
        functions.create_complex_number(0, 0),
        functions.create_complex_number(8, 0),
        functions.create_complex_number(-2, 16),
        functions.create_complex_number(5, -9),
        functions.create_complex_number(1, 3),
        functions.create_complex_number(1, -1),
        functions.create_complex_number(-8, 14),
        functions.create_complex_number(25, 17)
    ]
    list_of_complex_numbers_history = []
    test.non_ui_tests()
    create_menu(list_of_complex_numbers_history, list_of_complex_numbers)
