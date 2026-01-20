from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlW9r2zAQxr9K8KsOttFm6Vr2Lg2MbWwpdH8YjGEu9sUWkSVXOq8tXb77dLITOY4TWh"
    "i0ZXuXPPecdPdDd76NCp2itC+/WjTRm8FtpKBA92NDfz6IoCyDygLBTHpj5RxegZklAwk5"
    "cQ7SopNStIkRJQmtnKoqKVnUiTMKlQWpUuKywph0hpT7Qn78dLJQKV6jXf0tF/FcoEw36h"
    "Qp3+31mG5Kr71X9NYb+bZZnGhZFSqYyxvKtVq7hSJWM1RogJCPJ1Nx+Vxd0+aqo7rSYKlL"
    "bOWkOIdKUqvdOzJItGJ+rhrrG8z4lhfDo9HJ6PTV69Gps/hK1srJsm4v9F4negLTL9HSx4"
    "GgdniMgRsWIOQ2ukkOpp/dOqGDzxXdxbeC9aD8CriOJaqMcoZ2fLyH1rfxxeTd+OLAuZ5x"
    "L9o94/pxT5vQsI4x0oAwB5tjGpdg7ZU2Pe9wN8ye1L+DdSUErmEWHzVYHvD5ovVUWZhBsr"
    "gCk8ZbET3Uu7zboWJYdBVQkHk83CR30Oy7MRqR5H2bsIns3YUQPP+X4RNahr/cJ4xLuscE"
    "t1L+8cltr0QejXtAbOxPE+DR4eEdADrXToA+tgnQ3UhYz+AmxA+fz6f9EFspHZCpSGjwey"
    "CF3RrqxwF0Dz/ul4surL2UbWwHn8bfu0QnH8/PfP/aUmb8Kf6As4f+sCz/ACltn74="
)
