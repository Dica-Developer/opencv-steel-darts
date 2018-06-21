from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from darts_ui.models import DartsRecognitionStatus
from darts_ui.darts_recognition.Start import return_status
from datetime import datetime
# Create your views here.

@csrf_exempt
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


@csrf_exempt
def new_game(request):
    return render(request, 'darts_ui/new_game.html', {'message': 'Default'})