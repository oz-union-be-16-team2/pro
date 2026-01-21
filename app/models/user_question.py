from tortoise import fields
from tortoise.models import Model


class UserQuestion(Model):
    id = fields.BigIntField(pk=True)

    user = fields.ForeignKeyField(
        "models.User",
        related_name="user_questions",
        on_delete=fields.CASCADE,
    )
    question = fields.ForeignKeyField(
        "models.Question",
        related_name="user_questions",
        on_delete=fields.CASCADE,
    )

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_questions"
