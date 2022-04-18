try:
    import simplejson as json
except ImportError:
    import json

from django.http import JsonResponse

from polls.models import Question


def get_all(request):
    return JsonResponse({
        q.question_text: q.pub_date for q in Question.objects.all()
    })