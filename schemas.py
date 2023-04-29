from pydantic import BaseModel
from tortoise.contrib.pydantic import  PydanticModel
from typing import List


class FilmCreate(BaseModel):
    title: str
    director: str
    year: int
    description: str
    length: int
    rating: str


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
    description: str
    length: int
    rating: str
    categories: List[GetCategory] = []
    cast: List[FilmActor] = []
    image: List[FilmImage] = []

