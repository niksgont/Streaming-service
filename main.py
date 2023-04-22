from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends, Path
from tortoise.contrib.fastapi import register_tortoise
from typing import List
from schemas import FilmModel, FilmCreate, FilmUpdate, FilmInDB, Film
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # maybe should be rewritten
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_films():
    return await FilmModel.all()


async def get_film(film_id: int):
    film = await FilmModel.get_or_none(id=film_id)
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return film


async def create_film(film: FilmCreate):
    new_film = await FilmModel.create(**film.dict())
    return new_film


async def delete_film(film_id: int):
    film = await FilmModel.get_or_none(id=film_id)
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    await film.delete()
    return {"message": "Film deleted"}


@app.get("/films", response_model=List[Film])
async def read_films():
    return await get_films()


@app.get("/films/{film_id}", response_model=Film)
async def read_film(film_id: int):
    return await get_film(film_id)


@app.post("/films", response_model=Film)
async def create_film_endpoint(film: FilmCreate):
    return await create_film(film)


register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["main"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
