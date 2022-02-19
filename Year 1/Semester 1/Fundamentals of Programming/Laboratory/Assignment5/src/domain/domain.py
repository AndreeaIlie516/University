class Expense:
    def __init__(self, day, amount, type):
        """
        Create Expense with day(the day of the expense), amount(The amount of the expense),
        type(The type of the expense from a list given)
        :param day: The day of the expense(int, 1<=day<=30)
        :param amount: The amount of the expense (int)
        :param type: The type of the expense from a list given (string)
        """
        if day < 1 or day > 30:
            raise ValueError("Invalid day")
        self._day = day
        self._amount = amount
        self._type = type

    def __str__(self):
        return "Day: " + str(self._day) + ", Amount: " + str(self._amount) + ", Type: " + str(self._type)

    @property
    def day(self):
        return self._day

    @property
    def amount(self):
        return self._amount

    @property
    def type(self):
        return self._type

    @day.setter
    def day(self, value):
        if int(value) < 1 or int(value) > 30:
            raise ValueError("Invalid day")
        self._day = int(value)

    @amount.setter
    def amount(self, value):
        if int(value) < 0:
            raise ValueError("Invalid amount")
        self._amount = int(value)

    @type.setter
    def type(self, value):
        self._type = value
