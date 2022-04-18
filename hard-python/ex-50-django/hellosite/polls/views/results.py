from django.shortcuts import get_object_or_404, render
from django.views import generic

from ..models import Question


# Class view
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# Function view
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {
        "question": question,
    })