from django.http import HttpResponse

from game_elements.domain.game import game_repository_memory
from game_elements.start_game import startGame


# Create your views here.
def index(request):
    return HttpResponse("Bienvenu dans le jeu splendor")


def start_game(request):
    game_repository = GameRepositoryInMemory()
    StartGameCommand(game_repository.execute(number_of_players=2))
    return HttpResponse(str(game_repository.get_game()))
