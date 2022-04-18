from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from ..models import Question


# Class view version
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    # Defaults context var to <model_name>_list, this overrides it
    context_object_name = "latest_question_list"

    # Alternative to the get_queryset() function, if there are no
    # other things to do when getting queryset
    queryset = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by("-pub_date")[:5]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Method", self.request.method)

        name = self.request.GET.get("name", None)
        if name:
            context["name"] = name
        return context


    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by("-pub_date")[:5]


# function view version
def index(request):
    latest_question_list = Question.objects.order_by(
        "-pub_date")[:5]

    context = {
        "latest_question_list": latest_question_list
    }

    return render(request, "polls/index.html", context)