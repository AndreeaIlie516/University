from domain.domain import Player


class PlayerRepository:
    def __init__(self, player_list=None):
        if player_list is None:
            player_list = []
        self._player_list = player_list
        self.file_name = "../repository/players.txt"
        file = open(self.file_name, "r")
        for line in file.readlines():
            line = line.strip(" \n")
            stuff = line.split(",")
            self.add_player(Player(int(stuff[0]), str(stuff[1]), str(stuff[2])))
        file.close()

    @property
    def players(self):
        return self._player_list

    def add_player(self, player):
        self._player_list.append(player)

    def remove_player(self, player):
        self._player_list.remove(player)

    def update_player(self, player_id):
        player = self.find_player_by_id(player_id)
        player.strength += 1

    @staticmethod
    def filter(iterable, accept):
        new_list = type(iterable)()
        for x in iterable:
            if accept(x):
                new_list.append(x)
        return new_list

    def find_player_by_id(self, player_id):

        aux = self.filter(self._player_list, lambda x: x.player_id == player_id)
        if len(aux) == 0:
            return None
        else:
            return aux[0]
