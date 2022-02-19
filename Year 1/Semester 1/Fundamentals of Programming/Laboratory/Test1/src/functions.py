import random
import ui
import time


def validate_input_number(number):
    if number == 8086:
        return 1
    c4 = number % 10
    number = number // 10
    c3 = number % 10
    number = number // 10
    c2 = number % 10
    number = number // 10
    c1 = number % 10
    if c4 == c3 or c4 == c2 or c4 == c1:
        return 0
    if c3 == c2 or c3 == c1:
        return 0
    if c2 == c1:
        return 0
    if c1 == 0:
        return 0
    return 1


def generate_random_number():
    """
    The functions that generates a valid number having the following conditions:
    -a four digit random number;
    -the first digit is non-zero;
    -all digits are distinct
    :return: Correct 4 digits number generated
    """
    number = 0
    c1 = random.randint(1, 9)
    number = number * 10 + c1
    c2 = c1
    while c2 == c1:
        c2 = random.randint(0, 9)
    number = number * 10 + c2
    c3 = c1
    while c3 == c1 or c3 == c2:
        c3 = random.randint(0, 9)
    number = number * 10 + c3
    c4 = c1
    while c4 == c1 or c4 == c2 or c4 == c3:
        c4 = random.randint(0, 9)
    number = number * 10 + c4
    return number


def number_of_codes_runners(user_number, computer_number):
    codes = 0
    runners = 0
    user_digit1 = user_number % 10
    user_number = user_number // 10
    computer_digit1 = computer_number % 10
    computer_number = computer_number // 10

    user_digit2 = user_number % 10
    user_number = user_number // 10
    computer_digit2 = computer_number % 10
    computer_number = computer_number // 10

    user_digit3 = user_number % 10
    user_number = user_number // 10
    computer_digit3 = computer_number % 10
    computer_number = computer_number // 10

    user_digit4 = user_number % 10
    user_number = user_number // 10
    computer_digit4 = computer_number % 10
    computer_number = computer_number // 10

    if user_digit1 == computer_digit1:
        codes += 1
    if user_digit2 == computer_digit2:
        codes += 1
    if user_digit3 == computer_digit3:
        codes += 1
    if user_digit4 == computer_digit4:
        codes += 1

    if user_digit1 != computer_digit1:
        if user_digit1 == computer_digit2 or user_digit1 == computer_digit3 or user_digit1 == computer_digit4:
            runners += 1
    if user_digit2 != computer_digit2:
        if user_digit2 == computer_digit1 or user_digit2 == computer_digit3 or user_digit2 == computer_digit4:
            runners += 1
    if user_digit3 != computer_digit3:
        if user_digit3 == computer_digit1 or user_digit3 == computer_digit2 or user_digit3 == computer_digit4:
            runners += 1
    if user_digit4 != computer_digit4:
        if user_digit4 == computer_digit1 or user_digit4 == computer_digit2 or user_digit4 == computer_digit3:
            runners += 1

    return codes, runners


def play_game():
    computer_number = generate_random_number()
    while True:
        user_number = ui.read_user_number()
        if user_number == "exit":
            return -1
        user_number = int(user_number)
        if user_number == 8086:
            ui.print_computer_number(computer_number)
        if validate_input_number(user_number) == 0:
            ui.print_errror_valid_number()
            ui.print_loose()
            return 0
        if user_number != 8086:
            codes, runners = number_of_codes_runners(user_number, computer_number)
            print("The number of codes is: " + str(codes))
            print("The number of runners is: " + str(runners))
            if codes == 4:
                ui.print_win()
                return 1
