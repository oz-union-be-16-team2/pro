from tortoise import Tortoise, run_async


async def init():
# SQLite을 사용하여 DB db.sqlite3 파일을 생성한다.
    await Tortoise.init(
    db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']}
)

# 스키마를 생성한다.
    await Tortoise.generate_schemas()


# run_async는 async Tortoise scripts를 실행하기 위한 helper function이다.
    run_async(init())