from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, request, Http404
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from darts_ui.models import DartsRecognitionStatus, Game, GameType, Player
from darts_ui.darts_recognition.Start import return_status
from datetime import datetime
# Create your views here.


def index(request):
    # Try to get the last saved object for the dart recognition (if available), otherwise create one.
    status = DartsRecognitionStatus.objects.last()
    print("Status exists:\n{}".format(status))
    # If there isn't a status in the DB, create an initial one
    if status is None:
        initial_recognition = DartsRecognitionStatus(is_running=False, since=datetime.now())
        initial_recognition.save()
        status = DartsRecognitionStatus.objects.last()
    if request.method == 'POST':
        # try:
        if return_status():
            new_status = DartsRecognitionStatus(is_running=(not status.current_status()), since=datetime.now())
            new_status.save()
            return render(request,
                          'darts_ui/index.html',
                          {"status": new_status.is_running, "since": new_status.since}
                          )
    if status.current_status():
        return render(request, 'darts_ui/index.html', {"status": True, "since": status.since})
    else:
        return render(request, 'darts_ui/index.html', {"status": False, "since": status.since})


def game(request):
    active = [individ_game.__str__() for individ_game in Game.objects.all() if individ_game.active]
    inactive = [individ_game.__str__() for individ_game in Game.objects.all() if not individ_game.active]
    return render(request,
                  'darts_ui/game.html',
                  {'message': 'Not yet implemented - Game list goes here',
                   'active_games': str(active),
                   'inactive_games':str(inactive)})



def new_game(request):
    game_types = [(type.type, type.__str__()) for type in GameType.objects.all()]
    # game_types_db = [type.type for type in GameType.objects.all()]
    players = [(player.id, player.name) for player in Player.objects.all()]
    return render(request, 'darts_ui/new_game.html', {'game_types': game_types,
                                                      'players': players})


def game_id(request, game_id):
    try:
        requested_game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404('The requested game ID - {} - does not exist.'.format(game_id))
    static_message = 'You are looking at the info to game: {}'
    sample = [requested_game.__str__(),
              requested_game.id,
              requested_game.active,
              requested_game.players.__str__(),
              requested_game.start_time,
              requested_game.end_time]
    return render(request,
                  'darts_ui/game_info.html',
                  {'message': static_message.format(requested_game.__str__()),
                   'sample':str(sample)}
                  )