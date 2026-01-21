# app/models/quote.py
from tortoise import fields
from tortoise.models import Model


class Quote(Model):
    id = fields.IntField(pk=True)

    content = fields.TextField()
    author = fields.CharField(max_length=255, null=True)

    # 필터용으로 쓰고 싶으면 유지
    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "quotes"