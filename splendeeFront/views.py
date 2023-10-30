from django.template import loader
from django.http import HttpResponse


def index(request):
    context = dict()
    template = loader.get_template("index.html")

    return HttpResponse(template.render(context, request))


def showGame(request):
    number_player = request.POST['number_player']
    return HttpResponse("game created with " + number_player + " player")
