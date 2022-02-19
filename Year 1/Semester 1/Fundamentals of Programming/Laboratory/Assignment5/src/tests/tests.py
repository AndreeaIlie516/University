from src.services.services import Service
from src.domain.domain import Expense


class Test:
    """
    Test class
    """

    def __init__(self, service):
        self._service = service
        self._service._history = []

    def test_expense(self):
        """
        Function for testing the expense class
        :return:
        """
        expense = Expense(14, 76, "food")
        assert expense.day == 14
        assert expense.amount == 76
        assert expense.type == "food"

        try:
            expense.day = -24
            assert False
        except ValueError as ve:
            assert str(ve) == "Invalid day"

        try:
            expense.amount = -2000
            assert False
        except ValueError as ve:
            assert str(ve) == "Invalid amount"

    def test_add_expense(self):
        """
        Test function for adding an expense
        :return:
        """
        service = Service()
        self._service._expenses = []
        service.add_expense(Expense(20, 4200, "Work"))
        assert len(service.expenses) == 1

    def test_filter_expense(self):
        """
        Test function for filtering the list of expenses by the an amount
        :return:
        """
        service = Service()
        service.add_expense(Expense(20, 4200, "Work"))
        service.add_expense(Expense(15, 5500, "Education"))
        service.add_expense(Expense(27, 7000, "Healthcare"))
        service.filter_expenses(5000)
        assert len(service.expenses) == 2

    def all_tests(self):
        """
        Function for all test functions
        :return:
        """
        self.test_expense()
        self.test_add_expense()
        self.test_filter_expense()
