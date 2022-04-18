import datetime
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase


from ..models import Question


def create_question(question_text, days):
    """Create a question with the given 'q_ext' and published the
    given # of 'days' offset from now (negative for questions
    published in the past, positive for questions that have yet
    to be published).
    """

    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """

        fquestion = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(fquestion.id,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


    def test_past_question(self):
        """The detail view of a question with a pub_date in the past display's
        the question's text.
        """

        pquestion = create_question(question_text="Past question.", days=-5)
        url = reverse("polls:detail", args=(pquestion.id,))

        response = self.client.get(url)

        # The template turns the question_text into Title Case
        self.assertContains(response, str(pquestion.question_text).title())