from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import PersonOut
from app.api import db_manager

person = APIRouter()

@person.get('/', response_model=List[PersonOut])
async def index():
    return await db_manager.get_all_person()

@person.get('/{npm}')
async def get_person(npm):
    response = await db_manager.get_person(int(npm))

    if not response:
        raise HTTPException(
            status_code=404,
            detail='Person with NPM {} not found!'.format(npm)
        )

    return {
        'status': 'OK',
        **response
    }

