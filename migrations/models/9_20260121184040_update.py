from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "token_blacklist" ALTER COLUMN "expired_at" TYPE TIMESTAMPTZ USING "expired_at"::TIMESTAMPTZ;
        ALTER TABLE "token_blacklist" ALTER COLUMN "token" TYPE TEXT USING "token"::TEXT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "token_blacklist" ALTER COLUMN "expired_at" TYPE VARCHAR(100) USING "expired_at"::VARCHAR(100);
        ALTER TABLE "token_blacklist" ALTER COLUMN "token" TYPE VARCHAR(100) USING "token"::VARCHAR(100);"""


MODELS_STATE = (
    "eJztW1tzmzgU/iseP6Uzu53UiZNs34zjtN4m9jZxu512OowMiq0xlhwQTTxd//eVxB0ENa"
    "5JINEbnAvofLqcTwfxs70kJrSc1xohiyWwF+23rZ9tDJaQXWR0f7TaYLWKNFxAwdQSxlPf"
    "SkjB1KE2MChT3ALLgUxkQsew0YoigpkUu5bFhcRghgjPIpGL0Z0LdUpmkM6hzRTfvrVdh1"
    "0x5Z1LKGx//84uETbhA3S4nt+uFvotgpaZCACZ3EnIdbpeCdkQ0wthyF8/1Q1iuUscGa/W"
    "dE5waI0w5dIZxNAGFPLHU9vl8fDm+rEHIXpNj0y8JsZ8THgLXIvG4t8SFINgDihrjSMCnP"
    "G3/Nl5c3x6fHZ0cnzGTERLQsnpxgsvit1zFAiMJu2N0AMKPAsBY4SbYUMerA5oFr9zpqFo"
    "CeUgJj1TYJq+6+vgIg1tAGQRtoEgAjcaYXtCl8VgjrG19juuAMrJ8GpwM+ld/cMjWTrOnS"
    "Ug6k0GXNMR0nVKenDyissJmx/ezAkf0vp3OHnf4retr+PRQCBIHDqzxRsju8nXNm8TcCnR"
    "MbnXgRkbY4E0AIZZRh0r5o9ealrEXX49OWrSg3uZHxFsfPkph1rM4yWBxlfi24V0TQmW8C"
    "SAF8SGaIY/wLXAcchaBLABJbj5yeiT/5j64bcJxkAgjeakDe7D7BQfGiw8FhSkIsB+76bf"
    "Ox+0sxN2D7B9DJ7TXNziC5EcOD76psBY3APb1BPDkGtIh6QkoW1Wtews0xKAwUwAwMPgjf"
    "ahPUfAXst4k6coJE1maLJXwqT4UbX8iCJqSWZlfw5sOXahQwo+1uh6Tko23B90C+IZnbPb"
    "N4eHBXh97l333/euD5hVitmMfFXH0yWTKnsjhVjCMCfwIWcIxlyaAmQReRx8mSR4YwDXwV"
    "Xvy6sEd7wcj94F5jF4+5djLY2qou7Pk7pz2uCUJ6GOYqFpFuooGpoaHHWiUx9d6PgxZxhV"
    "qCskVXe+VQWVKEWsqiVWQdfplHGAMswg46j4gZwfIEdnswH9kNBXjRALApwzSON+KXCnzL"
    "EqdMMBvG90tfH4MoGuNkzD9+lKGzBaK6BmRshbH7PlIYPFPCPeRm7bHUHcZ6ex6gPzZHuC"
    "7jZbgm7+jqArNgSZVJ2fdFLluMQqnxrIvv/Fh2togSBh5CfyeFqp7QqRSeibarMwEaNdko"
    "L9QlJR/mUmKvk2LvmqDXkVCZdt6uZEUvnOTw2RRyMTQ6fb3SIzMKvc1CB0irZUTltUqej5"
    "lIp2IlLBmQ3WlVMJey3Do+KHROrX2U/CoSZkAbFmsWdZyKEyMpWyKGRVlNvq04SxolcNol"
    "eiA8uQq9BBUSs5tYIPK2TvlMCSns1MYA1JWEHYv/y4oQ7YqAM2j3PA5mk+bAhgJSQgADw/"
    "9YcfrVTCr9t8LEr4vNvEdQa9/L1/3Gc/ab9yFCuoCsdTwwo4zj1hk28OnHkZKDOOTaFRj3"
    "H2Rm391dY/+l3jxW3743OBn8FE8DdxCM96NhQESXVhdzCyZY2GoqI+NFZeJEvAksOOtzv2"
    "k+2s+tBlDc2eEWP+q9M5OjrtHB6dnHWPT0+7Z4chdc6qiji0NnzHaXQiWaq/014UeUn+7O"
    "If4ir5g1rC6yVVg1QJbQfQVAlt7/+oRen5N5FrJkFKo5dakepUhOxBGxlzGdHyNYUUC0Q2"
    "taFWz4hXVVaJ/AFtRzpB86tnMZdm1s0qOYbEp0YJEH3zZgL4uD/9/X0zHpU9Y2gig7b+a9"
    "W+yCDDj8db/EE8/e07xbf5A7RyJ6j3n1g2/wNneaJP"
)
