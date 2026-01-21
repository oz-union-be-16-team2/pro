from tortoise import fields
from tortoise.models import Model


class Bookmark(Model):
    id = fields.IntField(pk=True)

    user = fields.ForeignKeyField(
        "models.User",
        related_name="bookmarks",
        on_delete=fields.CASCADE,
    )
    quote = fields.ForeignKeyField(
        "models.Quote",
        related_name="bookmarks",
        on_delete=fields.CASCADE,
    )

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bookmarks"
        # UNIQUE(user_id, quote_id)
        unique_together = (("user", "quote"),)
