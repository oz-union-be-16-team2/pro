from tortoise import fields
from tortoise.models import Model


class Diary(Model):
    id = fields.IntField(pk=True)

    title = fields.CharField(max_length=100)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    users = fields.ForeignKeyField(
        "models.User",
        related_name="diaries",
        source_field="users_id",   # DB 컬럼명 그대로
        on_delete=fields.CASCADE,
    )

    class Meta:
        table = "diary"
