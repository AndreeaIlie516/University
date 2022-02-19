from domain.taxi import Taxi


class TaxiRepository:
    def __init__(self, taxi_list=None):
        if taxi_list is None:
            taxi_list = []
        self._taxi_list = taxi_list

    @property
    def taxis(self):
        return self._taxi_list

    def update_taxi(self, taxi_id, distance, coordinates):
        taxi = self.find_taxi_by_id(taxi_id)
        taxi.total_fare += distance
        taxi.coordinates = coordinates

    @staticmethod
    def filter(iterable, accept):
        new_list = type(iterable)()
        for x in iterable:
            if accept(x):
                new_list.append(x)
        return new_list

    def find_taxi_by_id(self, taxi_id):

        aux = self.filter(self._taxi_list, lambda x: x.taxi_id == taxi_id)
        if len(aux) == 0:
            return None
        else:
            return aux[0]
