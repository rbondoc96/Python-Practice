import pytest
import datetime

from django.urls import reverse
from django.utils import timezone
from django.test import Client, TestCase

from ..models import Question


@pytest.fixture(scope="class")
def question(request):
    request.cls.question = Question.objects.create(
        question_text="Are you hungry?", 
        pub_date=timezone.now()
    )


@pytest.mark.usefixtures("question")
class VotingTests(TestCase):

    def test_vote(self):
        """Tests the POST request sent when selecting a choice
        """
        choice = self.question.choice_set.create(choice_text="Hello")

        response = self.client.get(
            reverse("polls:detail", args=(self.question.id,))
        )
        # assert bytes(question.question_text.title()) in response.content

        response = self.client.post(
            reverse("polls:vote", args=(self.question.id,)),
            data={
                "choice": choice.id             
            },
            follow=True
        )
        self.assertRedirects(
            response, 
            reverse("polls:results", args=(self.question.id,)),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )