import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")

    
    def __str__(self):
        return self.question_text


    def was_published_recently(self):
        now = timezone.now()
        # self.pub_date must fall between the last 24 hours
        return now - datetime.timedelta(days=1) <= self.pub_date <= now