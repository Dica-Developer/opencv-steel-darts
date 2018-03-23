from os import getenv

import cv2
import django.dispatch
import numpy as numpy
from django.dispatch import receiver

from darts_ui.darts_recognition.BoardRecognition import Board

NO_CAM = getenv('NO_CAM', False)

if NO_CAM:
    from darts_ui.darts_recognition.utils.ReferenceImages import DummyCam
else:
    from darts_ui.darts_recognition.utils.VideoCapture import VideoStream


state = django.dispatch.Signal(providing_args=["status"])


class Darts:
    is_running = False

    def start(self):
        self.sendStatus("initializing")
        if NO_CAM:
            self.cam1 = DummyCam(0)
            self.cam2 = DummyCam(1)
        else:
            self.cam1 = VideoStream(0)
            self.cam2 = VideoStream(1)

        try:
            self.cam1.start()
            self.cam2.start()
        except:
            self.sendStatus("error")
            raise

        self.initBoards()
        self.is_running = True
        self.sendStatus("running")

    def stop(self):
        self.cam1.stop()
        self.cam2.stop()
        self.is_running = False
        self.sendStatus('stopped')

    def initBoards(self):
        self.sendStatus('initialize_boards')
        self.board1 = Board(self.cam1)
        self.board2 = Board(self.cam2)
        self.sendStatus('boards_initialized')

    def isRunning(self):
        return self.is_running

    def sendStatus(self, status):
        state.send(sender=self.__class__, status=status)
