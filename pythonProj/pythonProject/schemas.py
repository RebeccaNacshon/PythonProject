# schemas.py
# Define Pydantic models for validation.

from pydantic import BaseModel, EmailStr
from typing import List

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True  # Updated for Pydantic v2

class PostBase(BaseModel):
    text: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True  # Updated for Pydantic v2
