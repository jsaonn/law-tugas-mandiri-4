from app.api.models import PersonIn, PersonOut
from app.api.db import person, database


async def add_person(payload: PersonIn):
    status = await check_npm(payload.npm)

    if status == 'OK':
        query = person.insert().values(**payload.dict())
        data = await database.execute(query=query)
        return status

    return status

# ----------- utils -------------

async def check_npm(npm):
    query = person.select(person.c.npm==npm)
    data = await database.fetch_one(query=query)
    if data :
        return 'Person with this NPM already exist!'
    else :
        return 'OK'