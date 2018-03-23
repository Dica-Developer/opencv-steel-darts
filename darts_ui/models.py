from datetime import datetime

from django.db import models
from django.dispatch import receiver

from darts_ui.darts_recognition.Darts import Darts, state

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
        self.darts = Darts()
        self.darts.start()
