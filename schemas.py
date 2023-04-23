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


class FilmActor(PydanticModel):
    first_name: str
    last_name: str


class FilmImage(PydanticModel):
    image_url: str


class GetCategoryFilms(PydanticModel):
    id: int
    title: str
    director: str
    year: int
    categories: List[GetCategory] = []
    cast: List[FilmActor] = []
    image: List[FilmImage] =[]


class Films(Model):
    id = fields.IntField(pk=True)  # prob unique is extra
    title = fields.CharField(max_length=255)
    director = fields.CharField(max_length=255)
    year = fields.IntField()
    categories: fields.ReverseRelation["Category"]
    cast: fields.ReverseRelation["FilmCast"]
    image: fields.ReverseRelation["Images"]

    # class PydanticMeta:
    #     table = "films"


class Category(Model):
    category_name = fields.CharField(max_length=255, pk=True)
    film: fields.ForeignKeyRelation[Films] = \
        fields.ForeignKeyField("models.Films", related_name='categories')

    # class PydanticMeta:
    #     table = "category"


class FilmCast(Model):
    actor_id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    film: fields.ForeignKeyRelation[Films] = fields.ForeignKeyField("models.Films", related_name='cast')

    class Meta:
        unique_together = ("actor_id", "film")


class Images(Model):
    id = fields.IntField(pk=True)
    image_url = fields.CharField(max_length=500)
    film: fields.ForeignKeyRelation[Films] = fields.ForeignKeyField("models.Films", related_name='image')

    # class Meta:
    #     unique = "film"
