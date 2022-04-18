import datetime
from django.utils import timezone

from ..models import Question

import pytest


def test_was_published_recently_with_future_question():
    ftime = timezone.now() + datetime.timedelta(days=1, seconds=1)
    future_q = Question(pub_date=ftime)

    assert future_q.was_published_recently() == False


def test_was_published_recently_with_old_question():
    otime = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_q = Question(pub_date=otime)

    assert old_q.was_published_recently() == False


def test_was_published_recently_with_recent_question():
    time = timezone.now() - datetime.timedelta(
        hours=23, minutes=50, seconds=59)
    q = Question(pub_date=time)

    assert q.was_published_recently() == True