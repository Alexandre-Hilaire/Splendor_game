from django.template import loader
from django.http import HttpResponse

def index(request):
    context = { "game_started": False}
    template = loader.get_template("gameState.html")

    return HttpResponse(template.render(context, request))