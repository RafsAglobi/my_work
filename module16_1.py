from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "������� ��������"}


@app.get("/user/admin")
async def admin():
    return {"message": "�� ����� ��� �������������"}


@app.get("/user/{user_id}")
async def user(user_id: int):
    return {"message": f"�� ����� ��� ������������ � {user_id}"}


@app.get("/user")
async def user_info(username: str, age: int):
    return {"message": f"���������� � ������������. ���: {username}, �������: {age}"}