from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_users_email_133a6f";
        CREATE TABLE IF NOT EXISTS "diary" (
    "pk" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(100) NOT NULL,
    "content" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "users_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "quotes" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "content" VARCHAR(100) NOT NULL,
    "author" VARCHAR(100)
);
        CREATE TABLE IF NOT EXISTS "questions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "question_text" TEXT NOT NULL
);
        ALTER TABLE "users" ADD "username" VARCHAR(50) NOT NULL UNIQUE;
        ALTER TABLE "users" ADD "password_hash" VARCHAR(100) NOT NULL;
        ALTER TABLE "users" ADD "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "users" DROP COLUMN "hashed_password";
        ALTER TABLE "users" DROP COLUMN "email";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_users_usernam_266d85";
        ALTER TABLE "users" ADD "hashed_password" VARCHAR(255) NOT NULL;
        ALTER TABLE "users" ADD "email" VARCHAR(255) NOT NULL UNIQUE;
        ALTER TABLE "users" DROP COLUMN "username";
        ALTER TABLE "users" DROP COLUMN "password_hash";
        ALTER TABLE "users" DROP COLUMN "created_at";
        DROP TABLE IF EXISTS "quotes";
        DROP TABLE IF EXISTS "questions";
        DROP TABLE IF EXISTS "diary";"""


MODELS_STATE = (
    "eJztmFtP2zAUgP9KlCeQGIKOAtpbKGV0QLtBtiGmKXITN7Ga2CF2KBXrf5/tJM2tKc3EpZ"
    "n6lpxLfM7nyznOk+oRC7p09zuFgfpJeVIx8CB/yMl3FBX4fioVAgaGrjQMuYWUgCFlATAZ"
    "F46ASyEXWZCaAfIZIphLcei6QkhMboiwnYpCjO5DaDBiQ+bIQH795mKELfgIafLqj40Rgq"
    "6VixNZYmwpN9jUl7IeZmfSUIw2NEzihh5Ojf0pcwieWyPMhNSGGAaAQfF5FoQifBFdnGaS"
    "URRpahKFmPGx4AiELsukuyIDk2DBj0dDZYK2GOVDa//g6OD44+HBMTeRkcwlR7MovTT3yF"
    "ES6OvqTOoBA5GFxJhyE9Mmn0v0Og4IFuPL+hQg8tCLEBNk70rRA4+GC7HNHP7a3luC7Id2"
    "3TnXrrfae9siE8KXcrTA+7GmJVWCakrRB5ROSGAZDqBOHZQlx5fhmQhSoOlWfA2i+3urIO"
    "VWlUylLg/VDKBI2QCsTPSUaxjy4GKqec8CUit23U0e1hQwz8EaYHca74YlfPXeVfdG166+"
    "ikw8Su9diUjTu0LTktJpQbp1WJiK+UeUnz39XBGvyt2g35UECWV2IEdM7fQ7VcQEQkYMTC"
    "YGsDIbN5EmYGbi4B6NM0eQEAyBOZ4AvvpzmnQFWAgECNLy9J/EjmcX19AFEm15ouPSdco/"
    "Ml3POZ4lCzeRJnMt4JAWqcJVVnktrygBGNgyajG2GCnHY0GNn4OqLvLW3ORdirw/rlHkI+"
    "NNkecWDDG3VoWfO2zKUVqOCGYQL6hFOnysWIIZl6aAXFZmurd6rsIkuLautNvtXJW5HPQ/"
    "J+YZvJ3LwcmmyP+/RT47sfI+aNS6lmVdnj+312QGX+DoLvVGBYplhGckgMjGF3AqSfZ4SA"
    "Cbi07swv19/QBW9UBcHIDJvAnILQ6eH88KsqiKaTcd7bSrzqo7ytdsp76FRMZRaqcixdJ2"
    "6l6YbH6aNK6fqmwFqjuqBrYCb9BT8QrikKAOx9TjnzDGC635FGvcp1/39IM0JrLgAIx1z5"
    "yBkdXmGGzcMZhMncH4DajOvajk2JQj8S1uR2uyszUYINNZtK9jzdJdDVKbzZZu0JZ+4E12"
    "fGSvWpEzLk3Zxvma3Gq3V6jJ3KqyJktdobPhW6NOWxOZNxPg2/5u+3Iz6NftsS1kMuWP4i"
    "K6pr8RlvAT+S4vLMUaspP/mSM+8O6FZfYXMCdc0A=="
)
