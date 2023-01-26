from django.db import models


# Class Question
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="question's text")
    published_date = models.DateTimeField(
        auto_now_add=True, verbose_name="date published"
    )

    def __str__(self):
        return self.question_text


# Class Choice
class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question_choices"
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
