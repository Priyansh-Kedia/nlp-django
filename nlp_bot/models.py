from django.db import models
from django.db.models.signals import pre_save

from . import response_generator

class Question(models.Model):
    question_text = models.CharField(max_length=30)
    answer_text = models.CharField(max_length=100)
    token = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.question_text

def pre_save_question(sender, instance, *args, **kwargs):
    instance.token = response_generator.tokenize(instance.question_text)


pre_save.connect(pre_save_question, sender=Question)