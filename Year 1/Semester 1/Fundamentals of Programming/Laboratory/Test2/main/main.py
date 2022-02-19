from repository.taxi_repository import TaxiRepository
from service.taxi_service import TaxiService
from ui.ui import UI

if __name__ == '__main__':
    """
    The main function
    """
    taxi_repository = TaxiRepository()
    print("Please insert the number of taxis you want to be generated:")
    number_of_taxis = int(input('>'))
    taxi_service = TaxiService(taxi_repository, number_of_taxis, generate=True)
    ui = UI(taxi_service)
    ui.create_menu()


