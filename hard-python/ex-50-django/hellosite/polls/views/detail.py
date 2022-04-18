from django.shortcuts import render
from django.http import Http404
from django.views import generic
from django.utils import timezone

from ..models import Question


# Class view version
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """

        return Question.objects.filter(pub_date__lte=timezone.now())


# function view version
def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return Http404("Question does not exist.")

    return render(request, "polls/detail.html", {
        "question": question
    })