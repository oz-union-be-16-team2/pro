# app/models/quote.py
from tortoise import fields
from tortoise.models import Model


class Quote(Model):
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=100)
    author = fields.CharField(max_length=100, null=True)

    class Meta:
        table = "quotes"
