from django.db import models


class Board(models.Model):
    number_of_nobles = models.IntegerField()
    number_of_gold_token = models.IntegerField()
    number_of_red_token = models.IntegerField()
    number_of_green_token = models.IntegerField()
    number_of_blue_token = models.IntegerField()
    number_of_black_token = models.IntegerField()
    number_of_white_token = models.IntegerField()


class DevelopmentCard(models.Model):
    price_of_red_token = models.IntegerField(default=0)
    price_of_green_token = models.IntegerField(default=0)
    price_of_blue_token = models.IntegerField(default=0)
    price_of_black_token = models.IntegerField(default=0)
    price_of_white_token = models.IntegerField(default=0)


class CardPresentInBoard(models.Model):
    development_card = models.ForeignKey(DevelopmentCard, on_delete=models.DO_NOTHING)
    board = models.ForeignKey(Board, on_delete=models.DO_NOTHING)
    is_hidden = models.BooleanField(default=True)
    card_level = models.IntegerField()


class Game(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


class Player(models.Model):
    reserved_development_cards = models.IntegerField(default=0)
    owned_development_card = models.IntegerField(default=0)
    number_of_nobles = models.IntegerField(default=0)
    number_of_gold_token_owned = models.IntegerField(default=0)
    number_of_red_token_owned = models.IntegerField(default=0)
    number_of_green_token_owned = models.IntegerField(default=0)
    number_of_blue_token_owned = models.IntegerField(default=0)
    number_of_black_token_owned = models.IntegerField(default=0)
    number_of_white_token_owned = models.IntegerField(default=0)

    play_in_game = models.ForeignKey(Game, on_delete=models.CASCADE)


class CardPresentInPlayerHand(models.Model):
    development_card = models.ForeignKey(DevelopmentCard, on_delete=models.DO_NOTHING)
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    is_reserved = models.BooleanField(default=False)
