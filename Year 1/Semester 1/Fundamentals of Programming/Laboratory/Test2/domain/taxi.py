class Taxi:
    def __init__(self, taxi_id, coordinates=None, total_fare=0):
        self._taxi_id = int(taxi_id)
        if coordinates is None:
            self.coordinates = [0, 0]
        else:
            self._coordinates = coordinates
        self._total_fare = total_fare

    def __str__(self):
        return "ID: " + str(self._taxi_id) + "\nCoordinates: " + self._coordinates, "\nTotal fare: " + str(
            self._total_fare)

    def __eq__(self, other):
        return self._taxi_id == other.taxi_id

    @property
    def taxi_id(self):
        return self._taxi_id

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def total_fare(self):
        return self._total_fare

    @taxi_id.setter
    def taxi_id(self, x):
        self._taxi_id = x

    @coordinates.setter
    def coordinates(self, x):
        self._coordinates = x

    @total_fare.setter
    def total_fare(self, x):
        self._total_fare = x
