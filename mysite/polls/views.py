from django.http import HttpResponse
from .models import Question


def index(request):
    http = ""
    for q in Question.objects.all():
        http += q.question_text + "<br>"
    return HttpResponse(http)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
