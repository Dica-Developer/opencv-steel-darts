from django.contrib import admin
from .models import DartsRecognitionStatus, Player, GameType, Throw, Game
# Register your models here.

admin.site.register(DartsRecognitionStatus)
admin.site.register(Player)
admin.site.register(GameType)
admin.site.register(Throw)
admin.site.register(Game)
