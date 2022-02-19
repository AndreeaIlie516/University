from copy import deepcopy


class Service:
    def __init__(self):
        self._expenses = []
        self._history = []

    def add_expense(self, expense):
        """
        Function for adding an expense
        :param expense: An object of type Expense
        :return:
        """
        self._history.append(deepcopy(self._expenses[:]))
        self._expenses.append(expense)

    def filter_expenses(self, amount):
        """
        Function for filtering the expenses by an amount
        :param amount:
        :return:
        """
        self._history.append(deepcopy(self._expenses[:]))
        self._expenses = list(filter(lambda x: x.amount > amount, self._expenses))

    @property
    def expenses(self):
        return self._expenses

    def undo(self):
        """
        Function for the undo operation
        :return:
        """
        if len(self._history) > 0:
            self._expenses.clear()
            self._expenses.extend(self._history.pop())
        else:
            raise ValueError("You cannot perform undo operation anymore!")
