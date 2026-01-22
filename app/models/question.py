from tortoise import fields
from tortoise.models import Model


class Question(Model):
    id = fields.IntField(pk=True)
    question_text = fields.TextField()

    # ✅ 추가
    is_active = fields.BooleanField(default=True)
    category = fields.CharField(max_length=50, null=True)

    class Meta:
        table = "questions"
