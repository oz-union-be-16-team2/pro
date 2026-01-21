from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "quotes" ADD "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "quotes" ALTER COLUMN "content" TYPE TEXT USING "content"::TEXT;
        CREATE UNIQUE INDEX IF NOT EXISTS "uid_quotes_content_8633ba" ON "quotes" ("content", "author");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_quotes_content_8633ba";
        ALTER TABLE "quotes" DROP COLUMN "created_at";
        ALTER TABLE "quotes" ALTER COLUMN "content" TYPE VARCHAR(100) USING "content"::VARCHAR(100);"""


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
    "+QVJR/uUkln4Ei+z/OlRfEVp+CKv8UpHbpFWRhb/SWyBehRyOzRTUVJFXreD61jr2YQOzQ"
    "wf4kIHrCoX4d/SQEYEqWEGsWf5aFKMtiAgmLQkrAhK0+ixmrjXmDaIDswFJfPHyHplCAX5"
    "Cv4OMa2Tn5Kh/JuJeCU53KUKcynuBUxtNUwyWwGcnXBzw/5QZfOlSirdt8LEq0otvkdYkM"
    "EfU5TH6oHMUKSonR1LAGlD4QPvkWgC7KQJlyVPlWbbfVdlttt534aQxxcA/Bn8QhOCDYUB"
    "AydvX7g5EuJzQUFfV1qvLiVAyWHHa821mRdGfVhy5raP6MGPMfnc7JSa9zfHJ23j3t9brn"
    "xwF1TquKOLQ2eitodCxZql+aXhR5if8h4Z38KflXU8zrJVWDVAltD9BUCe3gPzaF6fknkW"
    "smQUqil1iR6lSE7EMbGYssouVpCikWCG1qQ62eEa+qrBL5Hdo0c4LmV88iLs2sm3W63R3q"
    "Ztwqt24mdYnDPnxqlADRM28mgL/2T7G/bifjsmfQTGSw1r+t2hcZsvAT8cZoeeosWvLYWY"
    "Jviwdo5Y7dHj6xbP8DHLQQHA=="
)
