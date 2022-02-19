from src.tests.domain_tests import DomainTest
from src.Service.Service import Service
from src.ui.ui import UI

if __name__ == '__main__':
    test = DomainTest()
    test.all_tests()
    service = Service()
    ui = UI()
    ui.create_menu()
