import unittest
from repository.taxi_repository import TaxiRepository
from service.taxi_service import TaxiService
from domain.taxi import Taxi


class Test(unittest.TestCase):
    def test_add_ride(self):
        taxi_repo = TaxiRepository()
        taxi_service = TaxiService(taxi_repo, 1)
        taxi = Taxi(1234, [12, 15])
        taxi2 = Taxi(1234, [40, 60], 40)
        taxi_repo.update_taxi(1234, 40, [40,60])
        taxi_list = list(taxi_repo.taxis)
        self.assertEqual(taxi_list, [taxi2])


if __name__ == "__main__":
    unittest.main()
