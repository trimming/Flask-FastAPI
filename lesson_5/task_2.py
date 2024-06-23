import uvicorn
from fastapi import FastAPI
import logging
from pydantic import BaseModel
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Genre(BaseModel):
    id: int
    name: str


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: Genre


movies = [
    Movie(id=1, title='Movie 1', description='', genre=Genre(id=1, name='drama')),
    Movie(id=2, title='Movie 2', description='', genre=Genre(id=2, name='comedy')),
    Movie(id=3, title='Movie 3', description='', genre=Genre(id=3, name='thriller')),
    Movie(id=4, title='Movie 4', description='', genre=Genre(id=4, name='drama')),
    Movie(id=5, title='Movie 5', description='', genre=Genre(id=5, name='trip')),
    Movie(id=6, title='Movie 6', description='', genre=Genre(id=6, name='trip')),
]


@app.get('/movies/', response_model=list[Movie])
async def get_movies(genre_id: int = None, genre_name=None):
    if genre_id is not None:
        return [movie for movie in movies if movie.genre.id == genre_id]
    if genre_name is not None:
        return [movie for movie in movies if movie.genre.name == genre_name]
    return movies


if __name__ == '__main__':
    uvicorn.run('task_2:app', host='localhost', port=8000, reload=True)
