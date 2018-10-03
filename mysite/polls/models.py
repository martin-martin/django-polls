from django.db import models
import datetime
from django.utils import timezone

# how does this look like in SQLite directly
# different schemas for different apps?
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        one_day = datetime.timedelta(days=1)
        if (self.pub_date >= now - one_day) and (self.pub_date <= now):
            return True
        return False

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
