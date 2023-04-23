from pydantic import BaseModel
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import PydanticListModel, PydanticModel
from typing import List


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


class GetCategory(PydanticModel):
    category_name: str


class GetCategoryFilms(PydanticModel):
    id: int
    title: str
    director: str
    year: int
    categories: List[GetCategory] = []


class Films(Model):
    id = fields.IntField(pk=True)  # prob unique is extra
    title = fields.CharField(max_length=255)
    director = fields.CharField(max_length=255)
    year = fields.IntField()
    categories: fields.ReverseRelation["Category"]

    # class PydanticMeta:
    #     table = "films"


class Category(Model):
    category_name = fields.CharField(max_length=255, pk=True)
    film: fields.ForeignKeyRelation[Films] = \
        fields.ForeignKeyField("models.Films", related_name='categories')

    # class PydanticMeta:
    #     table = "category"

