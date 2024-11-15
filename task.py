from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from models import Task, User
from schemas import CreateTask, TaskResponse
from database import get_db

router = APIRouter()


@router.get("/", response_model=list[TaskResponse])
def all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
def task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_task(create_task: CreateTask, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")

    new_task = Task(create_task.dict(), user_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update")
def update_task(task_id: int, update_task: CreateTask, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in update_task.dict().items():
        setattr(task, key, value)

    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Update Successful"}


@router.delete("/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"status_code": status.HTTP_204_NO_CONTENT}

