# routers.py
# Define API endpoints.

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas import UserCreate, User, PostCreate, Post
from services import create_user, authenticate_user, create_token, create_post, get_posts, delete_post, get_current_user
from db import get_db

router = APIRouter()

# User signup
@router.post("/signup", response_model=User)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user

# User login
@router.post("/login")
def login(form_data: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_token(user)
    return {"access_token": access_token, "token_type": "bearer"}

# Add a post
@router.post("/addpost", response_model=Post)
def add_post(post: PostCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_post(db, post, current_user.id)

# Get posts
@router.get("/getposts", response_model=List[Post])
def get_posts(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_posts(db, current_user.id)

# Delete a post
@router.delete("/deletepost/{post_id}")
def delete_post(post_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return delete_post(db, post_id, current_user.id)
