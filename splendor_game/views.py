from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader

from domain.board.board_repository_memory import BoardRepositoryInMemory
from domain.game.game_repository_memory import GameRepositoryInMemory
from domain.player.player_repository_memory import PlayerRepositoryInMemory
from splendor_game.forms import ThreeCoinsForm
from start_game.startGame import StartGameCommand
from turn.step_1.action_take_3_coins_differents_colors import TakeThreeCoinsCommand


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render(dict(), request))


game_repository = GameRepositoryInMemory()
player_repository = PlayerRepositoryInMemory()
getGamePath = "/splendor/getGame"


def getGame(request):
    game = game_repository.get_game()
    number_of_player = len(game.players)

    template = loader.get_template("get_game.html")
    player_repository.save(game.players)
    context = {"number_of_players": number_of_player,
               "number_card_exposed_per_level": game.board.exposed_development_cards_by_level,
               "number_of_nobles": game.board.number_of_nobles, "gold_coin": game.board.gold,
               "red_coins": game.board.red, "green_coins": game.board.green, "blue_coins": game.board.blue,
               "white_coins": game.board.white, "black_coins": game.board.black,
               "players": [PlayerPresentation(i) for i in range(number_of_player)]}
    return HttpResponse(template.render(context, request))


def take_3_coins(request):
    form = ThreeCoinsForm()

    return render(request, "take3CoinsTMP.html", {"form3Coins": form})


class PlayerPresentation:

    def __init__(self, player_id):
        players = player_repository.get_player()
        self.red_coins = players[player_id].coins_by_color["red"]
        self.green_coins = players[player_id].coins_by_color["green"]
        self.blue_coins = players[player_id].coins_by_color["blue"]
        self.black_coins = players[player_id].coins_by_color["black"]
        self.white_coins = players[player_id].coins_by_color["white"]
        self.gold_coins = players[player_id].coins_by_color["gold"]


def take_coins(request):
    board_repo = BoardRepositoryInMemory()
    player_repo = PlayerRepositoryInMemory()

    game = game_repository.get_game()
    board_repo.save(game.board)
    player_repo.save(game.players[0])
    takes_3_coins = TakeThreeCoinsCommand(board_repository=board_repo, player_repository=player_repo)

    if request.method == "POST":
        form = ThreeCoinsForm(request.POST)
        if form.is_valid():
            colorTrue = []
            for color in form.cleaned_data:
                if form.cleaned_data[color]:
                    colorTrue.append(color)
            if len(colorTrue) == 3:
                board = board_repo.get_board()
                takes_3_coins.execute(player_repo.get_player(), colorTrue[0], colorTrue[1], colorTrue[2], board)

                game.board = board_repo.get_board()
                game.players[0] = player_repo.get_player()

                game_repository.save(game)
                player_repository.save(game.players)
                return redirect("getGame")

    return HttpResponse("Mauvais formulaire (TODO)")


def startGame(request):
    start_game = StartGameCommand(game_repository)

    number_of_player = int(request.POST["nombres_de_joueurs"])
    start_game.execute(number_of_player)
    return redirect("getGame")
