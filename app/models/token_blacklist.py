from tortoise import fields
from tortoise.models import Model

class TokenBlacklist(Model):
    id = fields.IntField(pk=True)
    token = fields.CharField(max_length=100)
    expired_at = fields.CharField(max_length=100)

    user = fields.ForeignKeyField(
        "models.User",
        related_name="token_blacklist",
        on_delete=fields.CASCADE,
    )

    class Meta:
        table = "token_blacklist"

