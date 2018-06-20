from datetime import datetime
from django.db import models
from darts_ui.darts_recognition.Start import kickoff, return_status

import darts_ui.utils.game_types as gt
# Create your models here.


class DartsRecognitionStatus(models.Model):
    is_running = models.BooleanField()
    since = models.DateTimeField('date started')

    def __str__(self):
        return "{}, {}".format(self.is_running, self.since)


    def current_status(self):
        return self.is_running

    def running_since(self):
        return self.since

    # TODO:This always returns true (should be replaced with the kickoff function)
    def start_recognition(self):
        return return_status()


class Player(models.Model):
    name = models.TextField( null=True, help_text="Player name")


class GameType(models.Model):
    CRICKET = 'CR'
    FIVE_OH_ONE = '501'
    THREE_OH_ONE = '301'
    KILLER = 'KR'
    GAME_CHOICES = ((CRICKET, 'Cricket'),
                    (FIVE_OH_ONE, '501'),
                    (THREE_OH_ONE, '301'),
                    (KILLER, 'Killer'))

    type = models.TextField(choices=GAME_CHOICES, max_length=3, null=True, help_text="Choose the type of game.")


class Throw(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True ,help_text="Player_id, for the throw")
    round = models.IntegerField(help_text="Round of the game")
    throw_number = models.IntegerField(help_text="Throw of the round")
    hit = models.IntegerField("The number hit, 25 = BULL, 0 = Not valid")
    modifier = models.IntegerField("Modifier for Doubles and Triples")
    timestamp = models.DateTimeField("Timestamp of the throw")


class Game(models.Model):
    active = models.BooleanField(help_text="Is the game currently active.")
    game_type = models.ForeignKey(GameType, on_delete=models.SET_NULL, null=True, help_text="Type of this game")
    players = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, help_text="Players for this game")
    throws = models.ForeignKey(Throw, on_delete=models.SET_NULL, null=True, help_text="Throws for this game")
    start_time = models.DateTimeField(null=True, help_text="Time the game started")
    end_time = models.DateTimeField(null=True, blank=True, help_text="Time the game ended.")



# class Games(models.Model):
#
#     game_status = models.BooleanField(default=False, help_text="True if the game is currently active, else False.")
#     game_start = models.DateTimeField(null=True, help_text="Date and time when the game started.")
#     game_end = models.DateTimeField(null=True, help_text="Date and time when the game ended.")
#
#     class Meta:
#         # db_table = 'darts_ui_games'
#         verbose_name_plural = 'Games'
#
#     def __str__(self):
#         if self.game_status:
#             state = 'ACTIVE'
#         else:
#             state = 'INACTIVE'
#         return "Game: {}, {}".format(self.id, state)
#
#     def current_status(self):
#         return self.game_status
#
#     def running_since(self):
#         return self.game_start
#
#
# class Players(models.Model):
#     player_name = models.TextField(default='ANON', help_text="Player name")
#
#     class Meta:
#         # db_table = 'darts_ui_players'
#         verbose_name_plural = 'Players'
#
#     def __str__(self):
#         return self.player_name
#
#
# class GameResults(models.Model):
#     CRICKET = 'CR'
#     FIVE_OH_ONE = '501'
#     THREE_OH_ONE = '301'
#     KILLER = 'KR'
#     GAME_CHOICES = (
#         (CRICKET, 'Cricket'),
#         (FIVE_OH_ONE, '501'),
#         (THREE_OH_ONE, '301'),
#         (KILLER, 'Killer')
#     )
#     game_id = models.IntegerField(help_text="This will end up being a foreign key from games model.")
#     # game_id = models.ForeignKey(Games, on_delete=models.SET_DEFAULT, default=-1, help_text="Game ID")
#     game_name = models.TextField(help_text='Provide a name for the game', default="GAME")
#     game_type = models.CharField(choices=GAME_CHOICES, default=CRICKET, max_length=30, help_text="What type of game?")
#     player_id = models.IntegerField(help_text="This will end up being a foreign key from players model.")
#     # player_id = models.ForeignKey(Players, on_delete=models.SET_DEFAULT, default=-1, help_text="Player ID")
#     result = models.TextField(null=True, help_text="The result of the current throw.")
#     timestamp = models.DateTimeField(auto_now=True, help_text="Date and time for a particular result.")
#
#     class Meta:
#         # db_table = 'darts_ui_gameresults'
#         verbose_name_plural = 'GameResults'
#
#
#     def __str__(self):
#         return self.game_name
