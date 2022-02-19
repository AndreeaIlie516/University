import functions


def print_exit():
    print("You exited the game")


def print_win():
    print("You won the game")


def print_gamed_end():
    print("The time is gone. The game is ended")


def print_errror_valid_number():
    print("Your number is invalid")


def print_loose():
    print("You lost the game")


def read_user_number():
    user_number = str(
        input("Please insert a 4 digits number having the first digit is non-zero and all digits distinct:"))
    return user_number


def print_computer_number(computer_number):
    print(computer_number)
