from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "bookmarks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "quote_id" INT NOT NULL REFERENCES "quotes" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_bookmarks_user_id_176fbb" UNIQUE ("user_id", "quote_id")
);
        CREATE TABLE IF NOT EXISTS "token_blacklist" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "token" VARCHAR(100) NOT NULL,
    "expired_at" VARCHAR(100) NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "user_questions" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "question_id" INT NOT NULL REFERENCES "questions" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "bookmarks";
        DROP TABLE IF EXISTS "token_blacklist";
        DROP TABLE IF EXISTS "user_questions";"""


MODELS_STATE = (
    "eJztW1tz2jgU/iuMn9KZbid1Qkj3DQhp2TbQJt7dTjsdj7AV48FIxJKbMF3++0ry/VpMob"
    "ETvZlzMTqfdHQ+H9k/lCU2oUNeDTBeLIG7UP7s/FAQWEJ2kdO97ChgtYo1XEDBzBHGs8BK"
    "SMGMUBcYlClugUMgE5mQGK69ojZGTIo8x+FCbDBDG1mxyEP2nQd1ii1I59Bliq9fFY+wK6"
    "a88zCFyrdv7NJGJnyAhOv5z9VCv7WhY6YCsE3uJOQ6Xa+EbIzopTDkfz/TDex4SxQbr9Z0"
    "jlFkbSPKpRZE0AUU8ttT1+Px8OEGsYch+kOPTfwhJnxMeAs8hybi3xIUAyMOKBsNEQFa/F"
    "/+UF+f9k7PT85Oz5mJGEkk6W388OLYfUeBwERTNkIPKPAtBIwxboYLebA6oHn8LpiG2ktY"
    "DGLaMwOmGbi+Ci+y0IZAVmEbCmJw4xW2J3RZDOYUOetg4iqg1MZXoxutf/WRR7Ik5M4REP"
    "W1EdeoQrrOSI/OXnA5ZvnhZ050k86/Y+1dh//sfJlORgJBTKjlin+M7bQvCh8T8CjWEb7X"
    "gZlYY6E0BIZZxhMr8kevlRZJl58nR0NmcC/5EcPGt596qCU8nhNofCe+XRTuKeEWngbwEr"
    "vQttB7uBY4jtmIADJgAW5BMfo7uE3z8NuEayCUxjnpgvuoOiWXBguPBQWpCHDYvxn2L0ZK"
    "PmH3ANun8D7txS25ERUDx1ffDBiLe+CaemoZcg1WcUYS2eZVS3WZlQAELAEAD4MPOoD2wg"
    "buuog3+YpK0mRGJnslTNvyo9WixpbmG0t+xCyoTZ2CrBzOgVuMXeSQgY8NuplJyZb7g+5A"
    "ZNE5+/n6+LgCr3/618N3/esjZpVhNpNApfq6dFFl/0ghKmCYGnwoWYIJl7YAWUUeR5+1FG"
    "8M4Tq66n9+keKOH6aTt6F5At7hh+kgi6qk7k+TunPaQOqTUCJZaJaFEklDM4ujSXTqkwdJ"
    "EHOOUUW6SlJ1F1gdoBMlG0+HJVbh1OmUcYA6zCDnKPlBzA9y+2F5Zmd6HqlUSs/FIPC/fH"
    "8NHRBmZflumczdxk5DbtfcHHarw2LLLdjngqf1qk2OmcgdrnU7XOlTT/nDYwufen7D4yMj"
    "y3Nc0FEsxzH22AnGYKG1H8WdykHqeG/3SpA8S2zesn2UKqDhBUQDh93LsQktKgcZi8q6QL"
    "mtPksZywLRogIhJrBWbzF0kMUhAhE+rGy3pAtWjmTaS8Ipzz/l+ecjnH8+Tt9JAFtQfEPA"
    "y0tu1FOUhbZp+VhVaPm0iesaFSLps5/6cHAUU9Whu01x6JbXhm6uNKwAIfeYJd8ckHkdKH"
    "OOst7KQ7yneIgnH7drP24nc4G/ImPDX8QhehWnpSAUPNXvDka+ndBSVOQRxcGbUylYStjx"
    "dqey+clqDl0e2NYTYsxvVPXkpKcen5ydd097ve75cUSd86oqDj0Yv+U0OlUs5ccDz4q8pN"
    "9FDs7Ya34/kPJ6Tt0g2ULbATTZQtv7JwRxef7lrwjaSJCy6GV2pCY1IfvQtY15EdEKNJUU"
    "C8Q2jaFWT4hXHawT+R26pDBBy7tnCZd29s3UbneLvhmzKu2bCV3mnRCWGjVADMzbCeDv/S"
    "bjr5vppO7bSaZt0M5/ncY3GYrw4/GmaHnu3cvsa5YZvs1vUPPdy/0Xls3/oNmY1A=="
)
