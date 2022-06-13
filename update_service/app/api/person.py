from typing import List
from fastapi import APIRouter

from app.api.models import PersonIn
from app.api import db_manager

person = APIRouter()

@person.post('/', status_code=201)
async def add_person(payload: PersonIn):
    status_add = await db_manager.add_person(payload)
    response = {
        'status': status_add
    }

    return response
