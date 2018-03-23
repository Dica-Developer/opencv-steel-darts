import cv2
import numpy as numpy
import django.dispatch
from django.dispatch import receiver

from darts_ui.darts_recognition.utils.VideoCapture import VideoStream
from darts_ui.darts_recognition.BoardRecognition import Board


state = django.dispatch.Signal(providing_args=["status"])


class Darts:

    def start(self):
        self.sendStatus("initializing")
        self.cam1 = VideoStream(0)
        self.cam2 = VideoStream(1)
        try:
            self.cam1.start()
            self.cam2.start()
        except:
            self.sendStatus("error")

        self.sendStatus("done")

    def stop(self):
        self.cam1.stop()
        self.cam2.stop()

    def initBoards(self):
        self.board1 = Board(self.cam1)
        self.board2 = Board(self.cam2)

    def sendStatus(self, status):
        state.send(sender=self.__class__, status=status)
