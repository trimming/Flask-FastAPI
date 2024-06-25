from datetime import datetime, date

from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    first_name: str = Field(..., min_length=2)
    last_name: str = Field(..., min_length=2)
    birthday: date = Field(..., format='%Y-%m-%d')
    email: str = EmailStr
    address: str = Field(..., min_length=5)


class User(UserIn):
    id: int

