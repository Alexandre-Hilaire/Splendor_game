from django.template import loader
from django.http import HttpResponse
from .game_elements.start_game.startGame import StartGameCommand
from .game_elements.domain.game.game_repository_memory import GameRepositoryInMemory


def index(request):
    context = dict()
    template = loader.get_template("index.html")

    return HttpResponse(template.render(context, request))


game_repo = GameRepositoryInMemory()


def showGame(request):
    if request.GET["action"] == "startGame":
        start_game = StartGameCommand(game_repo)

        start_game.execute(int(request.POST['number_player']))

    context = {"game": game_repo.get_game(),
               "coin_color": {
                   "green": "vert",
                   "red": "rouge",
                   "blue": "bleu",
                   "black": "noir",
                   "white": "blanc",
                   "gold": "or"
               }
               }
    template = loader.get_template("gameState.html")

    return HttpResponse(template.render(context, request))
