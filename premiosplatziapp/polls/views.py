from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

# Create your views here.


def index(request: HttpRequest):
    latest_question_list = Question.objects.all()
    return render(
        request, "polls/index.html", {"latest_question_list": latest_question_list}
    )


def detail(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice_id = request.POST.get("choice")
    try:
        selected_choice = Choice.objects.get(pk=selected_choice_id)
    except (Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            context={
                "question": question,
                "error_message": "You didn't select a valid choice.",
            },
        )

    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
