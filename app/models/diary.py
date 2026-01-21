from tortoise import fields
from tortoise.models import Model
from .user import User
from datetime import datetime

class Diary(Model):
    pk = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    users = fields.ForeignKeyField("models.User", related_name="diaries")