from django.http import HttpResponse
from django.template import loader

from domain.game.game_repository_memory import GameRepositoryInMemory
from domain.player.player_repository_memory import PlayerRepositoryInMemory
from start_game.startGame import StartGameCommand


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render(dict(), request))


game_repository = GameRepositoryInMemory()
player_repository = PlayerRepositoryInMemory()


def getGame(request):
    # game_repository = GameRepositoryInMemory()
    start_game = StartGameCommand(game_repository)
    start_game.execute(2)
    game = game_repository.get_game()
    template = loader.get_template("get_game.html")
    player_repository.save(game.players)
    context = {"number_of_players": 2, "number_card_exposed_per_level": game.board.exposed_development_cards_by_level,
               "number_of_nobles": game.board.number_of_nobles, "gold_coin": game.board.gold,
               "red_coins": game.board.red, "green_coins": game.board.green, "blue_coins": game.board.blue,
               "white_coins": game.board.white, "black_coins": game.board.black}
    return HttpResponse(template.render(context, request))


def seeHand(request, player_id):
    players = player_repository.get_player()
    player = players[player_id]

    return HttpResponse(player)
