from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id : int
    name : str
    age : int

@app.post("/add/user/")
def create_user(user:User):
    return f"user created: {user}"