import datetime

from django.db import models
from django.utils import timezone
from django.db.models import CharField, Model
from django_mysql.models import ListCharField, ListTextField

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Person(Model):
    name = CharField(max_length=30)
    post_nominals = ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=(6 * 11) #6 * 10 character nominals, plus commas
    )