from src.services.services import Service
from src.domain.domain import Expense
from src.ui.ui import UI
from src.tests.tests import Test
import random

if __name__ == '__main__':
    type_list = [
        "Food & Drink",
        "Shopping",
        "Transport",
        "Home",
        "Bills & Fees",
        "Entertainment",
        "Car",
        "Travel",
        "Family & Personal",
        "Healthcare",
        "Education",
        "Groceries",
        "Gifts",
        "Sport & Hobbies",
        "Beauty",
        "Work",
        "Other"
    ]
    service = Service()
    test = Test(service)
    test.all_tests()
    for index in range(1, 10):
        day = random.randint(1, 30)
        amount = random.randint(1, 10000)
        type = random.choices(type_list)
        type = ''.join(type)
        service.add_expense(Expense(day, amount, type))
    ui = UI(service)
    ui.create_menu(type_list)
