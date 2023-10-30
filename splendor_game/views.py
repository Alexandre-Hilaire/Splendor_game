from django.http import HttpResponse
from django.template import loader

from domain.game.game_repository_memory import GameRepositoryInMemory
from start_game.startGame import StartGameCommand


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render(dict(), request))


def getGame(request):
    game_repository = GameRepositoryInMemory()
    start_game = StartGameCommand(game_repository)
    start_game.execute(2)
    game = game_repository.get_game()
    template = loader.get_template("get_game.html")
    context = {"number_of_players": 2}
    return HttpResponse(template.render(context, request))
