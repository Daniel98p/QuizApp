from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    publication_date = models.DateField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100, blank=True)
    answer_int = models.IntegerField(blank=True)

    def __str__(self):
        return self.answer_text
