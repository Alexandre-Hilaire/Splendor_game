from django.db import models


# Create your models here.
class Game(models.Model):
    visible_development_card_lvl_1 = models.IntegerField()
    visible_development_card_lvl_2 = models.IntegerField()
    visible_development_card_lvl_3 = models.IntegerField()
    visible_noble = models.IntegerField()
    gold_coins = models.IntegerField()
    blue_coins = models.IntegerField()
    red_coins = models.IntegerField()
    green_coins = models.IntegerField()
    white_coins = models.IntegerField()
    black_coins = models.IntegerField()


class Player(models.Model):
    blue_coins = models.IntegerField()
    red_coins = models.IntegerField()
    green_coins = models.IntegerField()
    white_coins = models.IntegerField()
    black_coins = models.IntegerField()
    play_on = models.ForeignKey(Game, on_delete=models.CASCADE)
