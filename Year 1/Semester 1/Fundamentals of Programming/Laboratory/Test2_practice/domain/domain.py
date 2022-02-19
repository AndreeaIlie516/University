class Player:
    def __init__(self, player_id, name, strength):
        self._player_id = int(player_id)
        self._name = name
        self._strength = int(strength)

    def __str__(self):
        return "ID: " + str(self._player_id) + "\nName: " + str(self._name) + "\nStrength: " + str(
            self._strength) + '\n'

    def __eq__(self, other):
        return self._player_id == other.player_id

    def to_dict(self):
        return {"player_id": self._player_id, "name": self._name, "strength": self._strength}

    @property
    def player_id(self):
        return self._player_id

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength

    @player_id.setter
    def player_id(self, x):
        self._player_id = x

    @name.setter
    def name(self, x):
        self._name = x

    @strength.setter
    def strength(self, x):
        self._strength = x

