from domain.domain import Player
import re
from utils.utils import *

class PlayerService:
    def __init__(self, player_repository):
        self._player_repository = player_repository

    @property
    def players(self):
        return self._player_repository.players

    def search_player_by_strength(self, strength):
        return [player for player in self._player_repository.players
                if re.search(str(strength), str(player.strength), re.IGNORECASE)]

    def order_by_strength(self):
        player_list = self.players
        new_player_list = []
        for player in player_list:
            new_player_list.append(player.to_dict())

        player_list_sorted = []
        player_dict_sorted = gnome_sort(new_player_list, key=lambda x: [x["strength"]], reverse=True)
        for player in player_dict_sorted:
            player_list_sorted.append(
                Player(player["player_id"], player["name"],
                       player["strength"]))
        return player_list_sorted

    def remove_player(self, player_id):
        player = self._player_repository.find_player_by_id(player_id)
        self._player_repository.remove_player(player)

    def update_player(self, player_id):
        self._player_repository.update_player(player_id)
