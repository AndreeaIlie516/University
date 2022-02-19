from domain.taxi import Taxi
from repository.taxi_repository import TaxiRepository
import random


class TaxiService:
    def __init__(self, taxi_repository, number_of_taxis=0, generate=False):
        self._taxi_repository = taxi_repository
        if generate:
            self._taxi_repository = TaxiRepository(self.generate_taxis(number_of_taxis))

    @property
    def taxis(self):
        return self._taxi_repository.taxis

    @staticmethod
    def generate_taxis(number_of_taxis):
        taxis = []
        for i in range(0, number_of_taxis):
            coordinates = []
            taxi_id = random.randint(1000, 9999)
            while taxi_id in [x.taxi_id for x in taxis]:
                taxi_id = random.randint(1000, 9999)
            city_x = random.randint(0, 100)
            city_y = random.randint(0, 100)
            coordinates = [city_x, city_y]
            taxis.append(Taxi(taxi_id, coordinates))
        return taxis

    def add_ride(self, start_point, end_point):
        """
        Method for adding a ride
        :param start_point: the starting point for the ride
        :param end_point: the ending point for the ride
        :return:
        """
        minimum = 100000
        for i in self.taxis:
            distance = abs(i.coordinates[0]-start_point[0]) + abs(i.coordinates[1]-start_point[1])
            if distance < minimum:
                minimum = distance
                taxi_chosen = i.taxi_id
        self.update_taxi(taxi_chosen, minimum, end_point)

    def update_taxi(self, taxi_id, distance, coordinates):
        self._taxi_repository.update_taxi(taxi_id, distance, coordinates)
