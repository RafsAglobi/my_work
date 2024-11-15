from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import User, CreateUser, UpdateUser  # Замените на ваши модели

app = FastAPI()


@app.get("/", response_model=List[User])
def all_users(db: Session = Depends(get_db)):
    users = db.execute(select(User)).scalars().all()
    return users


@app.get("/user/{user_id}", response_model=User)
def user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


@app.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.execute(select(User).where(User.username == user.username)).scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@app.put("/update/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    existing_user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    for key, value in user.dict().items():
        setattr(existing_user, key, value)

    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@app.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.delete(existing_user)
    db.commit()

    return {'status_code': status.HTTP_204_NO_CONTENT, 'transaction': 'User deleted successfully'}
