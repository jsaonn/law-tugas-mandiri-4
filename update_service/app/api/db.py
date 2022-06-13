from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine)

from databases import Database
import os

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

person = Table(
    'person',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('npm', Integer)
)

database = Database(DATABASE_URI)