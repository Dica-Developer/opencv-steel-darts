from datetime import datetime
from django.db import models
from darts_ui.darts_recognition.Start import kickoff, return_status
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


class Games(models.Model):
    game_status = models.BooleanField(default=False)
    game_start = models.DateTimeField(default=None)
    game_end = models.DateTimeField(default=None)
    # game_duration = models.IntegerField()


    def __str__(self):
        if self.game_status:
            state = 'ACTIVE'
        else:
            state = 'INACTIVE'
        return "Game: {}, {}".format(self.id, state)


    def current_status(self):
        return self.game_status


    def running_since(self):
        return self.game_start


class GameResults(models.Model):
    CRICKET = 'CR'
    FIVE_OH_ONE = '501'
    THREE_OH_ONE = '301'
    KILLER = 'KR'
    GAME_CHOICES = (
        (CRICKET, 'Cricket'),
        (FIVE_OH_ONE, '501'),
        (THREE_OH_ONE, '301'),
        (KILLER, 'Killer')
    )
    game_id = models.OneToOneField(Games, on_delete=models.SET('DELETED'), default=0)
    game_name = models.TextField(help_text='Provide a name for the game', default='GAME: {}'.format(game_id))
    game_type = models.CharField(choices=GAME_CHOICES, default=CRICKET, max_length=30)
    player_id = models.OneToOneField(to='Players', on_delete=models.SET('DELETED'))
    result = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.game_name


class Players(models.Model):
    pass
    player_id = models.OneToOneField(GameResults, primary_key=True, on_delete=models.SET('DELETED'), default=0)
    player_name = models.TextField(default='Hagbard Celine')


    def __str__(self):
        return self.player_name