from django.shortcuts import render, redirect
from django.http import JsonResponse
from profil.models import Profil
from .models import TetrisModel


def tetris(request):
    if request.method == 'POST' and request.user.is_authenticated:
        joueur = Profil.objects.filter(user=request.user)
        joueur.highscore = request.POST['score']
        joueur.save()

    scores = TetrisModel.objects.all().order_by("-score")[:1]

    return render(request, 'tetris.html', locals())


# Create your views here.
def add_score(request):
    score = TetrisModel()
    if "score" not in request.GET:
        return JsonResponse({"status": "error", "reason": "no score given"})
    score.score = request.GET["score"]
    score.user = request.user
    print(score.score)
    # TODO : add CSRF check

    score.save()
    return JsonResponse({"status": "ok"})

def get_scores(request):
    scores = TetrisModel.objects.all().order_by("-score")

    res = []

    for s in scores:
        res.append({
            "score": s.score,
            "user": s.user.id
        })

    return JsonResponse(res, safe=False)