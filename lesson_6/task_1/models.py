from pydantic import BaseModel, Field


class UserIn(BaseModel):
    user_name: str = Field(..., max_length=30)
    email: str = Field(..., max_length=50)
    password: str = Field(..., min_length=6)


class User(BaseModel):
    id: int
    user_name: str = Field(..., max_length=30)
    email: str = Field(..., max_length=50)
