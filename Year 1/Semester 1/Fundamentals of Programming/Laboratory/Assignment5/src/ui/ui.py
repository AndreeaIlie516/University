from src.domain.domain import Expense


class UI:
    def __init__(self, service):
        self._service = service
        self._service._history = []

    def ui_add_expense(self, type_list):
        """
        UI function for reading and adding an expense
        :param type_list: The list containing the types of expenses allowed
        :return:
        """
        print("Please add an expense:")
        day = input("The day of the expense is:")
        try:
            day = int(day)
        except ValueError:
            print("Invalid day")
            return
        amount = input("The amount of the expense is:")
        try:
            amount = int(amount)
        except ValueError:
            print("Invalid amount")
            return
        print("Please select one of teh following types:")
        print(type_list)
        type = input("The type of the expense is:")
        if type not in type_list:
            print("Invalid type")
            return
        try:
            self._service.add_expense(Expense(day, amount, type))
            print("You added an expense successfully\n")
        except Exception as ve:
            print(ve)

    def ui_filter_expense(self):
        """
        UI function for reading the amount and filtering the list of expenses by the amount
        :return:
        """
        amount = input("The amount for filtering the list is: ")
        try:
            amount = int(amount)
        except ValueError:
            print("Invalid amount")
        self._service.filter_expenses(amount)
        print("You filtered the expenses successfully\n")

    def print_expenses(self):
        """
        UI function for printing the list of expenses
        :return:
        """
        print("The list of expenses is:")
        number_of_expenses = 0
        for i in self._service.expenses:
            number_of_expenses += 1
            print(i)
        if number_of_expenses == 0:
            print("The list is empty")
        print('\n')

    def ui_undo(self):
        """
        UI function for the undo operation
        :return:
        """
        try:
            self._service.undo()
            print("You undid the operation successfully\n")
        except ValueError as ve:
            print(ve)
            print('\n')

    @staticmethod
    def print_menu():
        """
        Print the menu
        :return:
        """
        print("Please select one of the following options:")
        print("1.Add an expense")
        print("2.Display the list of expenses")
        print("3.Filter the list so that it contains only expenses above a certain value read from the console.")
        print("4.Undo the last operation that modified program data")
        print("5.Exit the application")
        print()

    def create_menu(self, type_list):
        """
        Create the menu-driven console user interface
        :param type_list: The list containing the types of expenses allowed
        :return:
        """
        while True:
            UI.print_menu()
            option = int(input('>'))
            if option == 1:
                self.ui_add_expense(type_list)
            elif option == 2:
                self.print_expenses()
            elif option == 3:
                self.ui_filter_expense()
            elif option == 4:
                self.ui_undo()
            elif option == 5:
                print("You exited the application.")
                return 0
            else:
                print('Invalid number. Please select one of the five options!')
