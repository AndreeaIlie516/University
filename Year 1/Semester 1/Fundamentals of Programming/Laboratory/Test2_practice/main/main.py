from repository.player_repository import PlayerRepository
from service.player_service import PlayerService
from ui.ui import UI

if __name__ == '__main__':
    """
    The main function
    """
    player_repository = PlayerRepository()
    player_service = PlayerService(player_repository)
    ui = UI(player_service)
    ui.create_menu()

