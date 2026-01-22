from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_quotes_content_8633ba";
        ALTER TABLE "quotes" ADD "is_active" BOOL NOT NULL DEFAULT True;
        ALTER TABLE "quotes" ALTER COLUMN "author" TYPE VARCHAR(255) USING "author"::VARCHAR(255);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "quotes" DROP COLUMN "is_active";
        ALTER TABLE "quotes" ALTER COLUMN "author" TYPE VARCHAR(100) USING "author"::VARCHAR(100);
        CREATE UNIQUE INDEX IF NOT EXISTS "uid_quotes_content_8633ba" ON "quotes" ("content", "author");"""


MODELS_STATE = (
    "eJztW1tz2jgU/isMT+nMbiclIWT3DRPSsk2gTehup52OR9gKaDASseQmTJf/vpJ8vy6muL"
    "ETvdnnYut8upxPx/KP9oqY0KKvNUKWK2Av23+2frQxWEF+kdL91mqD9TrUCAEDM0sazzwr"
    "KQUzymxgMK64AxaFXGRCathozRDBXIodyxJCYnBDhOehyMHo3oE6I3PIFtDmiq9f2w7lV1"
    "x57xAG29++8UuETfgIqdCL2/VSv0PQMmMBIFM4SbnONmspG2F2KQ3F62e6QSxnhUPj9YYt"
    "CA6sEWZCOocY2oBB8XhmOyIe0Vwvdj9Et+mhidvEiI8J74BjsUj8O4JiECwA5a2hMsC5eM"
    "vvnTenvdPzk7PTc24iWxJIels3vDB211EiMJ62t1IPGHAtJIwhboYNRbA6YGn8LriGoRXM"
    "BjHumQDT9Fxf+xdJaH0gi7D1BSG44Qg7ELo8BnOCrY3XcQVQTkfXw9tp//qDiGRF6b0lIe"
    "pPh0LTkdJNQnp09krICZ8f7swJHtL6ZzR91xK3rS+T8VAiSCib2/KNod30S1u0CTiM6Jg8"
    "6MCMjDFf6gPDLcOOlfNHLzUtoi7/Pzlq0oMHmR8hbGL5KYdaxOMlgSZW4rtl5priL+FxAC"
    "+JDdEcv4cbieOItwhgA2bg5iWjT95j6off1h8DvjSckzZ4CLJTdGjw8HhQkMkAB/3bQf9i"
    "2E5P2APA9tF/TnNxiy5E2cCJ0TcDxvIB2KYeG4ZCQzokIQls06pVZ5WUAAzmEgARhmi0B+"
    "0FAvYmize5ikLSZAYmByVMih9Vy48YYlbGrBwsgJ2NXeCQgI83up6Tkg/3R92CeM4W/PbN"
    "8XEBXn/3bwbv+jdH3CrBbMaequPq4kmVv5FBnMEwp/AxZwhGXJoCZBF5HH6exnijD9fRdf"
    "/zqxh3vJqM3/rmEXgHVxMtiaqi7s+TugvaQMuTUKpYaJKFUkVDE4OjTnTqowOpF3OKUQW6"
    "QlJ171lVUIlSxKpaYuV3nc44ByjDDFKOih9k8wNEdT4b0PcM+qoRYkGAcwZp1C8B7ow7Vo"
    "VuMIAPja42mVzF0NVGSfg+XWtDTmsl1NwIuetjujxk8JjnxN3I7bojiPrsNVY9YJ5sT9Dd"
    "ZUvQzd8RdOWGIJWq85NOohwXW+UTA9nzv3x/Ay3gJ4z8RB5NK7VdIVIJfVttFiZytGekYK"
    "+QVJR/uYlKvo1LvmpDXkXC5Zu6BcmofOenhtCjkYmh0+3ukBm4VW5qkDpFWyqnLapU9HxK"
    "RXsRqdiZjf05VPSASP06+kn405QsIdYs/iwLUZZFpBIWhYyKCVt9FjNW1KpB1Ep2YKkPRr"
    "5DU2jVL/hgBB/XyM7JV/lIxr0UnOpQizrU8gSHWp7mY4IENiP5+oDnp9zgQ5FKtHWbj0WJ"
    "VnSbvC6RIaI+h8kPlaNYQSU2mhrWgNIHwiffAtBFGShTjirfqu222m6r7bYTP8wizj0i+J"
    "M4BOcrGwpCxq5+fzDS5YSGoqI+7lVenIrBksOOdztqk+6s+tBlDc2fEWP+o9M5Oel1jk/O"
    "zrunvV73/DigzmlVEYfWRm8FjY4lS/VH2IsiL/EfTLyDUyV/Cot5vaRqkCqh7QGaKqEd/L"
    "+wMD3/JHLNJEhJ9BIrUp2KkH1oI2ORRbQ8TSHFAqFNbajVM+JVlVUiv0ObZk7Q/OpZxKWZ"
    "dbNKjv6IqVECRM+8mQD+2h/t/rqdjMue6zORwVr/tmpfZMjCT8Qbo+Wp833Jo3wJvi0eoJ"
    "U7tXz4xLL9DzVWdX8="
)
