from tortoise import fields
from tortoise.models import Model


class TokenBlacklist(Model):
    id = fields.IntField(pk=True)

    # JWT는 길이가 길 수 있어서 TextField 추천
    token = fields.TextField()

    # 만료시간은 날짜 타입으로 (UTC 기준 저장 추천)
    expired_at = fields.DatetimeField()

    user = fields.ForeignKeyField(
        "models.User",
        related_name="token_blacklist",
        on_delete=fields.CASCADE,
    )

    class Meta:
        table = "token_blacklist"