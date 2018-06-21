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
    name = models.TextField(null=True, help_text="Player name")

    def __str__(self):
        return self.name


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

    def __str__(self):
        types = {'CR': 'Cricket', '501': '501', '301': '301', 'KR': 'Killer'}
        return '{}'.format(types[self.type])


class Throw(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, help_text="Player_id, for the throw")
    round = models.IntegerField(help_text="Round of the game")
    throw_number = models.IntegerField(help_text="Throw of the round")
    hit = models.IntegerField("The number hit, 25 = BULL, 0 = Not valid")
    modifier = models.IntegerField("Modifier for Doubles and Triples")
    timestamp = models.DateTimeField("Timestamp of the throw")

    def __str__(self):
        modifiers = {1: 'S', 2: 'D', 3: 'T'}
        return '{}: {}.{} - {} {}'.format(self.player.name,
                                          self.round,
                                          self.throw_number,
                                          modifiers[self.modifier],
                                          self.hit)


class Game(models.Model):
    active = models.BooleanField(help_text="Is the game currently active.")
    game_type = models.ForeignKey(GameType, on_delete=models.SET_NULL, null=True, help_text="Type of this game")
    players = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, help_text="Players for this game")
    throws = models.ForeignKey(Throw, on_delete=models.SET_NULL, null=True, help_text="Throws for this game")
    start_time = models.DateTimeField(null=True, help_text="Time the game started")
    end_time = models.DateTimeField(null=True, blank=True, help_text="Time the game ended.")

    def __str__(self):
        return 'GAME {}: {}'.format(self.id, self.game_type)
