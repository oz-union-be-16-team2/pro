from tortoise import fields
from tortoise.models import Model

class Question(Model):
    id = fields.IntField(pk=True)
    question_text = fields.TextField()

    class Meta:
        table = "questions"
