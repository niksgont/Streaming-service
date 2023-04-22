from pydantic import BaseModel
from tortoise.models import Model
from tortoise import fields


class FilmCreate(BaseModel):
    title: str
    director: str
    year: int


class FilmUpdate(FilmCreate):
    id: int


class FilmInDB(FilmUpdate):
    id: int


class Film(FilmInDB):
    pass


class FilmModel(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    director = fields.CharField(max_length=255)
    year = fields.IntField()

    class Meta:
        table = "films"

