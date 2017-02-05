from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user
    bots = user.bot_set.all()
    return render(request, 'index.html', {
        'bots': bots,
        'user': user,
    })
