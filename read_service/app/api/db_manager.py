from app.api.models import PersonIn, PersonOut
from app.api.db import person, database


async def get_all_person():
    query = person.select()
    return await database.fetch_all(query=query)

async def get_person(npm):
    query = person.select(person.c.npm==npm)
    return await database.fetch_one(query=query)
